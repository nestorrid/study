ORM
================================================

定义数据模型
------------------------------------------------

sqlalchemy通过`MetaData`对象来存储表结构的信息, 以此来批量的完成对数据模型的操作.

直接定义表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

也可以直接通过对象来定义表

.. code-block:: python

    
    import sqlalchemy
    from sqlalchemy import String, Integer

    meta = sqlalchemy.MetaData()

    records = sqlalchemy.Table(
        'records', meta,
        sqlalchemy.Column('record_id', Integer, primary_key=True),
        sqlalchemy.Column('name', String(50), unique=True, nullable=False)
    )


.. note:: 

    直接通过 `Table` 类创建表是一种比较基础的定义形式, 在2.0之后通常使用类来进行模型定义

    但是对于某些不需要创建类的表同样也可以使用此种方式来进行定义, 比如在多对多关系里的中间关系表

定义式数据模型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

通过一个继承自 `DeclarativeBase` 的类来作为所有模型类的基类.

该类内置了一个 `metadata` 对象, 每一个子类都使用该对象来作为自身的 `metadata` , 每个子类是一张表, 在子类中进行对于表的定义即可.

.. code-block:: python

    
    import sqlalchemy
    from sqlalchemy import Column, String, Integer, create_engine
    from sqlalchemy.orm import DeclarativeBase


    class Base(DeclarativeBase):
        pass


    class Record(Base):
        __tablename__ = 'records'

        id = Column('record_id', Integer, primary_key=True)
        name = Column('name', String(50), unique=True)

计算字段
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

column_property()
    定义计算属性, 该字段不会出现在数据库中, 但是可以通过对象直接访问

.. code-block:: python
    
    class User(Base):
        __tablename__ = "user"
    
        # ...
        firstname: Mapped[str] = mapped_column(String(50))
        lastname: Mapped[str] = mapped_column(String(50))
        # 数据库中不会出现该字段, 但是可以直接通过映射对象操作
        fullname: Mapped[str] = column_property(firstname + " " + lastname)

抽象表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__abstract__
    bool值, 设置基类是否为抽象类, 如果为True, 那么在建表时不会创建该表. 比如可以创建多个不同的Base, 用以对表进行分组.

    .. code-block:: python
    
        class Base(DeclarativeBase):
            pass
        
        class DefaultBase(Base):
            __abstract__ = True
            metadata = MetaData()
        
        
        class OtherBase(Base):
            __abstract__ = True
            metadata = MetaData()
            
        DefaultBase.metadata.create_all(some_engine)
        OtherBase.metadata.create_all(some_other_engine)    

类型映射
------------------------------------------------

通过 `Mapped` 类可以将python类型映射为数据库类型, 在定义字段时可以直接声明字段类型. 如果存在更多的字段约束, 则可以通过 `mapped_column` 进行赋值. 

.. note::

    `mapped_column` 是2.0版本新增加的功能, 取代了直接使用 `Column()` 对象的方式, 提供了一些增强的配置功能.

对添加了 `Mapped` 类型的字段, 可以不进行赋值, 框架会自动为其添加一个 `mapped_column()`.

.. code-block:: python

    
    class Base(DeclarativeBase):
        pass


    class User(Base):
        __tablename__ = "user"

        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(50))
        fullname: Mapped[Optional[str]]
        nickname: Mapped[Optional[str]] = mapped_column(String(30))

.. note:: 可用的类型映射包括:

    .. code-block:: python
            
        type_map: Dict[Type[Any], TypeEngine[Any]] = {
            bool: types.Boolean(),
            bytes: types.LargeBinary(),
            datetime.date: types.Date(),
            datetime.datetime: types.DateTime(),
            datetime.time: types.Time(),
            datetime.timedelta: types.Interval(),
            decimal.Decimal: types.Numeric(),
            float: types.Float(),
            int: types.Integer(),
            str: types.String(),
            uuid.UUID: types.Uuid(),
        }

自定义类型映射
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

如果希望将python类型映射为其他类型, 而不是默认的类型, 可以通过内置变量 `type_annotation_map` 来进行自定义.

.. code-block:: python

    class Base(DeclarativeBase):
        type_annotation_map = {
            int: BIGINT,
            datetime.datetime: TIMESTAMP(timezone=True),
            str: String().with_variant(NVARCHAR, "mssql"),
        }


    class SomeClass(Base):
        __tablename__ = "some_table"

        id: Mapped[int] = mapped_column(primary_key=True)
        date: Mapped[datetime.datetime]
        status: Mapped[str]

使用类型注解
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

也可以通过类型注解进行常用类型的定义, 使其包含更多的信息, 方便重用.

.. code-block:: python

    from decimal import Decimal
    from typing_extensions import Annotated

    str_30 = Annotated[str, 15]
    str_50 = Annotated[str, 50]
    dec_16_4 = Annotated[Decimal, 16]
    dec_6_2 = Annotated[Decimal, 6]


    class Base(DeclarativeBase):

        type_annotation_map = {
            str_30: String(30),
            str_50: String(50),
            dec_16_4: Numeric(16, 4),
            dec_6_2: Numeric(6, 2),
        }

        id: Mapped[int] = mapped_column(primary_key=True)


    class TypeMapping(Base):
        """
        create table main.type_mapping
        (
            s1 VARCHAR(30)    not null,
            s2 VARCHAR(50)    not null,
            d1 NUMERIC(16, 4) not null,
            d2 NUMERIC(6, 2)  not null,
            id INTEGER        not null
                primary key
        );
        """

        __tablename__ = 'type_mapping'

        s1: Mapped[str_30]
        s2: Mapped[str_50]
        d1: Mapped[dec_16_4]
        d2: Mapped[dec_6_2]

同样, 也可以通过类型注解来映射整个字段定义

.. code-block:: python

    intpk = Annotated[int, mapped_column(primary_key=True)]

    timestamp = Annotated[
        datetime,
        mapped_column(nullable=False, server_default=func.current_timestamp())
    ]

    update_timestamp = Annotated[
        datetime,
        mapped_column(
            nullable=False,
            server_default=func.now(),
            server_onupdate=func.now()
        ),
    ]

非空约束
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`mapped_column()` 会根据 `Mapped` 类型来自动获取类型和非空设置, 对于没有`Optional`注解的字段则为必填, 否则为允许空值. 

但如果显示的指定了是否可以为空, 则以 `mapped_column()` 的参数为准.

.. code-block:: python

    class SomeClass(Base):
        __tablename__ = "some_table"

        # primary_key=True, therefore will be NOT NULL
        id: Mapped[int] = mapped_column(primary_key=True)

        # not Optional[], therefore will be NOT NULL
        data: Mapped[str]

        # Optional[], therefore will be NULL
        additional_info: Mapped[Optional[str]]

.. note:: 

    对象的字段定义和数据库字段的非空定义可以不同. 
    
    对象的字段定义会在创建python对象时进行验证, 而数据库字段的设置则始终以`mapped_column()`参数为准.

    .. code-block:: python

        
        class SomeClass(Base):
            # will be String() NOT NULL, but can be None in Python
            data: Mapped[Optional[str]] = mapped_column(nullable=False)
            
        class SomeClass(Base):
            # will be String() NULL, but type checker will not expect
            # the attribute to be None
            data: Mapped[str] = mapped_column(nullable=True)    

mapped_column() 常用参数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

字段表名称
    首个字符串参数, 将作为字段在数据库中的名称

    .. code-block:: python
    
        class User(Base):
            __tablename__ = "user"
        
            id: Mapped[int] = mapped_column("user_id", primary_key=True)
            name: Mapped[str] = mapped_column("user_name")

deferred
    当为True时, 该字段默认不会直接加载, 而是仅在访问时进行加载. 通常来说对于储存在数据库中的大文件可以通过该参数提升效率

    .. code-block:: python

        class User(Base):
            __tablename__ = "user"
        
            id: Mapped[int] = mapped_column(primary_key=True)
            name: Mapped[str]
            bio: Mapped[str] = mapped_column(Text, deferred=True)

使用枚举类型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SQLAlchemy中可以直接使用python内建的 `Enum` 类来进行枚举类型的定义.

.. code-block:: python

    class Status(Enum):
        PENDING = "pending"
        RECEIVED = "received"
        COMPLETED = "completed"

    class EnumDemo(Base):

        __tablename__ = 'enum_demo'

        name: Mapped[str_15]
        status: Mapped[Status]

.. note:: 

    对于不同的底层数据库生成的DDL语句并不相同

添加约束
------------------------------------------------

SQLAlchemy定义模型类时有两个变量可以用来进行配置

`__tablename__`
    设置表名

`__table_args__`
    添加表的约束, 如主外键, 唯一约束, 索引等等.

    可以接受词典或者元组类型的参数.

.. code-block:: python
    
    class MyClass(Base):
        __tablename__ = "sometable"
        __table_args__ = {"mysql_engine": "InnoDB"}

    class MyClass(Base):
        __tablename__ = "sometable"
        __table_args__ = (
            ForeignKeyConstraint(["id"], ["remote_table.id"]),
            UniqueConstraint("foo"),
        )

    class MyClass(Base):
        __tablename__ = "sometable"
        __table_args__ = (
            ForeignKeyConstraint(["id"], ["remote_table.id"]),
            UniqueConstraint("foo"),
            {"autoload": True},
        )    

添加字段验证
------------------------------------------------

.. code-block:: python

    from sqlalchemy.orm import validates
    from sqlalchemy.orm import DeclarativeBase


    class Base(DeclarativeBase):
        pass


    class EmailAddress(Base):
        __tablename__ = "address"

        id = mapped_column(Integer, primary_key=True)
        email = mapped_column(String)

        @validates("email")
        def validate_email(self, key, address):
            if "@" not in address:
                raise ValueError("failed simple email validation")
            return address

组合字段
------------------------------------------------

可以将多个数据库字段组合成为一个对象字段

.. code-block:: python

    
    import dataclasses
        
    from sqlalchemy.orm import DeclarativeBase, Mapped
    from sqlalchemy.orm import composite, mapped_column

    @dataclasses.dataclass
    class Point:
        x: int
        y: int

    class Vertex(Base):
        __tablename__ = "vertices"

        id: Mapped[int] = mapped_column(primary_key=True)

        start: Mapped[Point] = composite(mapped_column("x1"), mapped_column("y1"))
        end: Mapped[Point] = composite(mapped_column("x2"), mapped_column("y2"))
        
    @dataclasses.dataclass
    class FullName:
        firstname: str
        lastname: str


    class User(Base):

        __tablename__ = 'users'

        fullname: Mapped[FullName] = composite(
            mapped_column('firstname', String(15)), mapped_column('lastname', String(15)))      


如果使用了组合字段, 那么便可以在对象操作时直接使用组合字段内进行对象的初始化

.. code-block:: python

    v = Vertex(start=Point(3, 4), end=Point(5, 6))
    session.add(v)
    session.commit()

    """
    BEGIN (implicit)
    INSERT INTO vertices (x1, y1, x2, y2) VALUES (?, ?, ?, ?)
    [generated in ...] (3, 4, 5, 6)
    COMMIT
    """

反射数据库
------------------------------------------------

从已有的数据库中得到模型类, 无需逐个字段进行定义. 在对现有项目进行逆向工程, 或者对数据库进行独立维护时作用就很大.

.. code-block:: python

    from sqlalchemy import create_engine
    from sqlalchemy import Table
    from sqlalchemy.orm import DeclarativeBase

    engine = create_engine("postgresql+psycopg2://user:pass@hostname/my_existing_database")


    class Base(DeclarativeBase):
        pass


    class MyClass(Base):
        __table__ = Table(
            "mytable",
            Base.metadata,
            autoload_with=engine,
        )

也可以直接对整个数据库进行反射, 然后用更为简单的方式来进行对象映射

.. code-block:: python

    from sqlalchemy import create_engine
    from sqlalchemy.orm import DeclarativeBase

    engine = create_engine("postgresql+psycopg2://user:pass@hostname/my_existing_database")


    class Base(DeclarativeBase):
        pass


    Base.metadata.reflect(engine)


    class MyClass(Base):
        __table__ = Base.metadata.tables["mytable"]