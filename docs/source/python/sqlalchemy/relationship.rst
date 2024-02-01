关系处理
================================================

在数据库关系的定义中有两个重点:

ForeignKey()
    用来定义外键字段, 该字段会保存在数据库之中, 用来关系表的主键. 接收一个字符串参数, 格式为`'表名.主键字段名'`

    .. code-block:: python
    
        parent_id: Mapped[int] = mapped_column(ForeignKey("parent.id"))

relationship()
    定义映射对象的关系查询字段, 仅在对象操作中用来直接查询关系对象, 不会在数据库中保存字段. 
    
    通过在两端添加 `relationship()` 字段, 同时添加 `back_populates` 属性实现双向查询.

    .. code-block:: python

        children: Mapped[List[Child]] = relationship(back_populates='parent')
    

对于关系的定义, 基本上通过`Mapped`对象来进行定义:

* `Mapped[Child]`: 对一
* `Mapped[Optional[Child]]`: 对一, 可以为空
* `Mapped[List[Child]]`: 对多, 同时也可以使用`Set`或者其他集合类型.

一对多关系
------------------------------------------------

.. code-block:: python

    
    from __future__ import annotations
    from typing import List

    from sqlalchemy import ForeignKey
    from sqlalchemy import Integer
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Mapped
    from sqlalchemy.orm import mapped_column
    from sqlalchemy.orm import DeclarativeBase
    from sqlalchemy.orm import relationship
    from sqlalchemy.orm import declared_attr


    class Base(DeclarativeBase):

        @declared_attr.directive
        def __pk__(cls):
            return f'{cls.__tablename__}.id'

        id: Mapped[int] = mapped_column(primary_key=True)


    class Parent(Base):

        __tablename__ = 'parent'

        children: Mapped[List[Child]] = relationship(back_populates='parent')
        name: Mapped[str]


    class Child(Base):

        __tablename__ = 'child'

        parent_id: Mapped[int] = mapped_column(ForeignKey(Parent.__pk__))
        parent: Mapped[Parent] = relationship(back_populates='chidren')

一对一关系
------------------------------------------------

.. code-block:: python

    class Parent(Base):
        __tablename__ = "parent_table"

        id: Mapped[int] = mapped_column(primary_key=True)
        child: Mapped["Child"] = relationship(back_populates="parent")


    class Child(Base):
        __tablename__ = "child_table"

        id: Mapped[int] = mapped_column(primary_key=True)
        parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
        parent: Mapped["Parent"] = relationship(back_populates="child", single_parent=True)
        
        __table_args__ = (UniqueConstraint("parent_id"),)

默认情况下, 在一对一关系中,  当`parent`设置了新的`child`时, 旧的`child.parent_id`会被设置为`NULL`. 可以通过`cascade`设置更改这一行为.

多对多关系
------------------------------------------------

多对多关系通过一个中间表建立.

.. code-block:: python

    from __future__ import annotations

    from sqlalchemy import Column
    from sqlalchemy import Table
    from sqlalchemy import ForeignKey
    from sqlalchemy import Integer
    from sqlalchemy.orm import Mapped
    from sqlalchemy.orm import mapped_column
    from sqlalchemy.orm import DeclarativeBase
    from sqlalchemy.orm import relationship


    class Base(DeclarativeBase):
        pass


    # note for a Core table, we use the sqlalchemy.Column construct,
    # not sqlalchemy.orm.mapped_column
    # 此处不能使用 `mapped_column`
    association_table = Table(
        "association_table",
        Base.metadata,
        Column("left_id", ForeignKey("left_table.id"), primary_key=True),
        Column("right_id", ForeignKey("right_table.id"), primary_key=True),
    )


    class Parent(Base):
        __tablename__ = "left_table"

        id: Mapped[int] = mapped_column(primary_key=True)
        children: Mapped[List[Child]] = relationship(secondary=association_table)


    class Child(Base):
        __tablename__ = "right_table"

        id: Mapped[int] = mapped_column(primary_key=True)

在中间表中同时设置两个id字段为主键相当于设置了一个联合主键, 保证两个id的组合不会重复.

如果希望实现双向多对多, 那么在两边添加 `relationship()` 字段, 并添加 `back_populates` 属性即可.

自连接
------------------------------------------------

链接自身的的模式, 类似于职工表, 可以包含一个主管字段, 是另外一个员工的ID

.. code-block:: python

    class Node(Base):
        __tablename__ = "node"
        id = mapped_column(Integer, primary_key=True)
        parent_id = mapped_column(Integer, ForeignKey("node.id"))
        data = mapped_column(String(50))
        children = relationship("Node")

cascasdes
------------------------------------------------

默认值为`save-updat, merge`.

可以直接在 `relationship()` 中设置, 也可以通过 `relationship()` 的 `backref` 属性进行反向设置

.. code-block:: python

    class Order(Base):
        __tablename__ = "order"

        items = relationship("Item", cascade="all, delete-orphan")
        customer = relationship("User", cascade="save-update")
        
    class Item(Base):
        __tablename__ = "item"

        order = relationship(
            "Order", backref=backref("items", cascade="all, delete-orphan")
        )

cascade选项
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`save-update`
    当添加数据时, 关联数据会被一同添加.

`delete`
    当父元素删除时, 子元素一同删除, 如果没有该选项, 子元素的外键字段会被设置为空

`delete`
    在多对多关系中: 有三种情况:

    * 没有添加`delete`: 在删除时, 仅删除中间表的数据
    * 添加`delete`: 删除中间表数据的同时, 删除子元素表中的数据
    * 在两边同时添加`delete`: 递归删除, 删除中间表, 子表, 子表关联的其他父表数据.

`delete-orphan`
    删除没有父元素的数据. 假设`Parent`和`Child`两个表存在一对多关系. 
    
    如果没有`delete-orphan`设置, 那么在`Child`中的父外键设置为NULL时该元素便会被删除. 
    
    如果仅是设置了`delete`, 没有`delete-orphan`, 那么删除父元素时所有的子元素都会被删除. 但是子元素清空父元素时自身不会被删除.

.. note:: 

    通常来说, 对于必须包含父元素的情况, 可以直接使用`all, delete-orphan`

