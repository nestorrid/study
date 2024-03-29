使用Session进行ORM数据操作
================================================

添加数据
------------------------------------------------

直接通过 `session().add()` 方法即可添加数据, 如果包含关系数据, 会被一同添加

通过 `new` 属性可以查看新增的数据, 在 `commit()` 之后 `new` 属性便会被清空.

.. code-block:: python

    squidward = User(name="squidward", fullname="Squidward Tentacles")
    krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")
    session = Session(engine)
    session.add(squidward)
    session.add(krabs)
    session.new

    # IdentitySet(
    #	[User(id=None, name='squidward', fullname='Squidward Tentacles'), 
    #   User(id=None, name='ehkrabs', fullname='Eugene H. Krabs')]
    # )

基本操作
------------------------------------------------

`session.get(User, 1)`
    获取id为1的User对象

`session.add_all(list)`
    批量添加对象

`session.delete(entity)`
    删除对象

`session.deleted`
    当前会话中被删除的对象

`session.dirty`
    当前会话中被修改的对象

`session.flush()`
    将当前会话中的修改写入数据库, 但不进行提交. flush之后, session中的对象会直接获得最终的id

    .. code-block:: python
    
        def test_model_should_have_pk_after_session_flush(session):
            u = User(name='new user')
            session.add(u)
            assert u.id is None
            session.flush()
            assert u.id > 0

`session.commit()`
    提交会话

`session.rollback()`
    数据回滚

`session.close()`
    如果没有使用 `with` 需要手动关闭会话