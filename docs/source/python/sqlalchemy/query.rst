数据操作
================================================

链接数据库
------------------------------------------------

sqlalchemy 链接数据库的方式基本相同, 区别在于链接字符串

链接Sqlite
    .. code-block:: python

        from sqlalchemy import create_engine

        engine = create_engine('sqlite:///test.db', echo=True)
        connection = engine.connect()

链接Mysql
    如果使用mysql数据库, 需要安装依赖`mysqlclient`

    .. code-block:: bash

        pip install mysqlclient


    .. code-block:: python

        from sqlalchemy import create_engine
        engine = create_engine('mysql://user:pwd@url/db', echo=True)
        connection = engine.connect()

创建, 删除数据表
------------------------------------------------

通过引擎和`MetaData`来创建表, 无论通过何种方式进行了数据模型的定义, 只要通过对应的`metadata`进行创建表即可

.. code-block:: python

    engine = create_engine("sqlite:///db.sqlite", echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

ORM查询
------------------------------------------------

select语句
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

基础查询, 通过 `select` 对象创建查询, 然后通过 `session` 的 `execute` 执行即可获得结果.

.. code-block:: python

    
    from sqlalchemy import select
    stmt = select(User).where(User.name == "spongebob")

    result = session.execute(stmt)
    for user_obj in result.scalars():
        print(f"{user_obj.name} {user_obj.fullname}")

在使用 `execute` 方法获得的是一个row对象, 本质是一个元组, 仅包含一个实体对象

.. code-block:: python

    result.all()
    """
    [(User(id=1, name='spongebob', fullname='Spongebob Squarepants'),),
    (User(id=2, name='sandy', fullname='Sandy Cheeks'),),
    (User(id=3, name='patrick', fullname='Patrick Star'),),
    (User(id=4, name='squidward', fullname='Squidward Tentacles'),),
    (User(id=5, name='ehkrabs', fullname='Eugene H. Krabs'),)]
    """

对于查询具体的实体对象, 可以直接跳过生成Row对象, 而获得具体的实体对象. 直接使用 `session.scalars()` 方法进行查询, 便可以获得具体的实体对象.

.. code-block:: python

    session.scalars(select(User).order_by(User.id)).all()
    """
    [User(id=1, name='spongebob', fullname='Spongebob Squarepants'),
    User(id=2, name='sandy', fullname='Sandy Cheeks'),
    User(id=3, name='patrick', fullname='Patrick Star'),
    User(id=4, name='squidward', fullname='Squidward Tentacles'),
    User(id=5, name='ehkrabs', fullname='Eugene H. Krabs')]
    """

同时查询多个表
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    stmt = select(User, Address).join(User.addresses).order_by(User.id, Address.id)
    for row in session.execute(stmt):
        print(f"{row.User.name} {row.Address.email_address}")

查询特定的属性
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    result = session.execute(
        select(User.name, Address.email_address)
        .join(User.addresses)
        .order_by(User.id, Address.id)
    )

使用原生SQL语句查询
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from sqlalchemy import text
    textual_sql = text("SELECT id, name, fullname FROM user_account ORDER BY id")

    orm_sql = select(User).from_statement(textual_sql)
    for user_obj in session.execute(orm_sql).scalars():
        print(user_obj)


子查询
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

可以通过`subquery()`方法创建子查询

.. code-block:: python

    inner_stmt = select(User).where(User.id < 7).order_by(User.id)
    subq = inner_stmt.subquery()
    aliased_user = aliased(User, subq)
    stmt = select(aliased_user)
    for user_obj in session.execute(stmt).scalars():
        print(user_obj)
    
    """
    SELECT anon_1.id, anon_1.name, anon_1.fullname
    FROM (SELECT user_account.id AS id, user_account.name AS name, user_account.fullname AS fullname
    FROM user_account
    WHERE user_account.id < ? ORDER BY user_account.id) AS anon_1
    [generated in ...] (7,)

    User(id=1, name='spongebob', fullname='Spongebob Squarepants')
    User(id=2, name='sandy', fullname='Sandy Cheeks')
    User(id=3, name='patrick', fullname='Patrick Star')
    User(id=4, name='squidward', fullname='Squidward Tentacles')
    User(id=5, name='ehkrabs', fullname='Eugene H. Krabs')
    """

集合操作
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如通过 `union_all()` 将多个查询的结果集进行合并等

.. code-block:: python

    from sqlalchemy import union_all
    u = union_all(
        select(User).where(User.id < 2), select(User).where(User.id == 3)
    ).order_by(User.id)
    stmt = select(User).from_statement(u)
    for user_obj in session.execute(stmt).scalars():
        print(user_obj)
        
    """
    SELECT user_account.id, user_account.name, user_account.fullname
    FROM user_account
    WHERE user_account.id < ? UNION ALL SELECT user_account.id, user_account.name, user_account.fullname
    FROM user_account
    WHERE user_account.id = ? ORDER BY id
    [generated in ...] (2, 3)
    """    

Join子句
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: text

    在SQLAlchemy2.0以后得版本中, 使用 `select().join()` 来进行关联查询. `Query().join()` 属于1.x版本的使用方式.

.. code-block:: python

    stmt = select(User).join(User.addresses)
    print(stmt)

    """
    SELECT user_account.id, user_account.name, user_account.fullname
    FROM user_account JOIN address ON user_account.id = address.user_id
    """

`join()` 子句可以包含多种形式:

`join(User.address)`
    直接使用查询表的关系字段, 相当于 `User.id = Address.user_id`

`join(Address)`
    直接使用关联表的实体, 此时会默认根据两个实体的外键关系进行查询

`join(Address, User.id == Address.user_id)`
    显示的指定`on`子句, 可读性最高

`join(subquery)`
    关联子查询

    .. code-block:: python
    
        subq = select(Address).where(Address.email_address == "pat999@aol.com").subquery()
        stmt = select(User).join(subq, User.id == subq.c.user_id)
        print(stmt)
        
        """
        SELECT user_account.id, user_account.name, user_account.fullname
        FROM user_account
        JOIN (SELECT address.id AS id,
        address.user_id AS user_id, address.email_address AS email_address
        FROM address
        WHERE address.email_address = :email_address_1) AS anon_1
        ON user_account.id = anon_1.user_id
        """

同时 `join()` 子句可以进行连用, 即关联多个表:

.. code-block:: python

    stmt = select(User).join(User.orders).join(Order.items).join(User.addresses)
    print(stmt)

    """
    SELECT user_account.id, user_account.name, user_account.fullname
    FROM user_account
    JOIN user_order ON user_account.id = user_order.user_id
    JOIN order_items AS order_items_1 ON user_order.id = order_items_1.order_id
    JOIN item ON item.id = order_items_1.item_id
    JOIN address ON user_account.id = address.user_id
    """



练习代码
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    
    import pytest

    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import Session

    from .models import Base, User, Address


    engine = create_engine('sqlite:///select.sqlite', echo=True)


    @pytest.fixture(scope='module', autouse=True)
    def init_database():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        with Session(engine) as session:
            address = Address(street='some street', zipcode='1111')
            user = User(name='test user')
            user.address = [address]
            session.add(user)
            user = User(name='noaddress user')
            session.add(user)
            session.commit()


    @pytest.fixture
    def session():
        with Session(engine) as session:
            with session.begin():
                yield session

    def test_select_join(session):
        stmt = select(User).join(User.address)
        results = session.scalars(stmt).all()
        print(stmt)
        print(results)
        assert results[0].name == 'test user' and results[0].address[0].street == 'some street'


    def test_select_join_entity(session):
        stmt = select(User).join(Address)
        results = session.scalars(stmt).all()
        print(stmt)
        print(results)
        assert results[0].name == 'test user' and results[0].address[0].street == 'some street'


    def test_select_join_entity_with_on_clause(session):
        stmt = select(User).join(Address, User.id == Address.user_id)
        results = session.scalars(stmt).all()
        print(stmt)
        print(results)
        assert results[0].name == 'test user' and results[0].address[0].street == 'some street'


    def test_select_where(session):
        stmt = select(User).where(User.address.any(Address.zipcode.contains('11')))
        results = session.scalars(stmt).all()
        assert len(results) == 1


    def test_select_users_without_address(session):
        result = session.scalars(
            select(User).where(~User.address.any())
        ).first()
        assert result.name == 'noaddress user'


    def test_select_user_by_id(session):
        user = session.get(User, 1)
        print(user)
        assert user.name == 'test user'

insert语句
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

与 `select()` 语句相同, 插入语句同样可以通过 `Session().execute()` 来执行

插入单条数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

对于单条数据的插入, 可以简单的通过 `session().add()` 来直接进行添加

.. code-block:: python

    def test_insert_single_user(session):
        user = User(name='single user')
        session.add(user)
        assert session.query(User).count() == 1


插入多条数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SQLAlchemy在插入数据时可以省略对象的创建, 直接通过json格式的数据进行数据的插入. 

可以直接通过 `insert().values()` 方法直接插入, 或者通过 `session().execute()` 的 `param` 参数指定数据.

.. code-block:: python

    
    def test_insert_multiple_users_with_params(session):
        resultset = session.execute(insert(User).returning(User), [
            {'name': f'user-{i}'}
            for i in range(10)
        ])
        print(resultset)
        print(resultset.all())


    def test_insert_multiple_users_with_values(session):
        resultset = session.execute(insert(User).values([
            {'name': f'user-{i}'}
            for i in range(10)
        ]).returning(User))
        print(resultset)
        print(resultset.all())

获取返回数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当需要使用新插入的数据的或者其中的某个字段时可以通过 `returning()` 方法来获取. 可以通过指定实体来获得完整行数据, 也可以单独指定所需要的字段.

.. code-block:: python

    
    def test_get_insert_user(session):
        result = session.scalar(
            insert(User).values({'name': 'John'}).returning(User)
        )
        print(result, result.id)
        assert result.name == 'John'


    def test_get_insert_user_id(session):
        user_id = session.execute(
            insert(User).values({'name': 'John'}).returning(User.id)
        ).one().id
        print(user_id)
        assert user_id > 0

插入拥有相同字段的值的多条数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当插入多条记录, 而所有记录的某些字段具有相同属性时, 可以通过 `insert().values()` 来设置相同的字段, 
然后通过 `session().execute()` 的 `param` 参数来指定每条记录具体的数据.

.. code-block:: python

    def test_insert_mutiple_address_for_same_user(session):
        user_id = session.execute(insert(User).values(
            {'name': 'multiple addr user'}).returning(User.id)).one().id

        list_addr = [
            {
                'street': f'street {i}',
                'zipcode': f'{i}' * 5,
            }
            for i in range(10)
        ]
        results = session.execute(
            insert(Address).values(user_id=user_id).returning(Address),
            list_addr
        )
        print(results.all())

关联数据插入
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当需要同时插入多个表的数据时, 比如一对多关系的 `User` 和 `Address` 表. 

可以先通过 `insert()` 语句插入用户, 并获取其id, 然后再批量插入address.

或者通过创建实体对象, 并直接使用 `Session().add()` 方法一次性插入设置完成的user对象. 便可以同时完成关联表的数据插入.

.. code-block:: python

    def test_insert_user_with_multiple_address(session):
        user = User(name='john')
        user.address = [
            Address(street=f'street {i}', zipcode=f'{i}' * 5)
            for i in range(10)
        ]
        session.add(user)

update, delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

基于id更新单条数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def test_update_user_by_id(session):
        result = session.execute(
            update(User).where(User.id == 1).values({
                'name': 'new name'
            })
        )
        user = session.get(User, 1)
        assert user.id == 1
        assert user.name == 'new name'
        assert result.rowcount == 1

批量修改数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def test_update_user_with_id_lt_10(session):
        result = session.execute(
            update(User).where(User.id < 10).values({
                'name': User.name + ' test update'
            })
        )
        print(result.rowcount)
        assert result.rowcount > 0


获取影响数据的行数
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在执行 `update` 和 `delete` 语句时, `session.execute()` 方法返回的结果会包含一个 `rowcount` 属性, 记录了影响的数据行数.

获取影响的数据
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

也可以使用 `returning` 语句获取受影响的数据或者特定的字段

.. code-block:: python

    def test_get_updated_user_id(session):
        result = session.scalars(
            update(User).where(User.name.contains('user')).values(
                {'name': 'new user name' + User.id}
            ).returning(User.id)
        ).all()
        print(result)
        assert len(result) > 0

























