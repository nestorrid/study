from __future__ import annotations
from typing import Optional, List

import pytest
from sqlalchemy import create_engine
from sqlalchemy import String, ForeignKey, Table, Column, Integer
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, Session
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship, backref


class Base(DeclarativeBase):

    @declared_attr.directive
    def __pk__(cls):
        return f'{cls.__tablename__}.id'

    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):

    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String(30))
    address: Mapped[List[Address]] = relationship(
        back_populates='user',
        cascade='save-update, merge, delete'
    )
    profile: Mapped[UserProfile] = relationship(
        back_populates='user', cascade='all')


class UserProfile(Base):

    __tablename__ = 'user_profiles'

    user_id: Mapped[int] = mapped_column(ForeignKey(User.__pk__))
    nickname: Mapped[Optional[str]] = mapped_column(String(30), default=None)
    user: Mapped[User] = relationship(
        back_populates='profile')


class Address(Base):

    __tablename__ = 'addresses'

    street: Mapped[str] = mapped_column(String(300))
    user_id: Mapped[int] = mapped_column(ForeignKey(User.__pk__))
    user: Mapped[User] = relationship(back_populates='address')


role_permission = Table(
    'role_permissions',
    Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id')),
    Column('permission_id', Integer, ForeignKey('permissions.id'))
)


class Role(Base):

    __tablename__ = 'roles'

    name: Mapped[str] = mapped_column(String(20))
    permissions: Mapped[List[Permission]] = relationship(
        secondary=role_permission,
        back_populates='roles',
        # cascade='all, delete'
    )


class Permission(Base):

    __tablename__ = 'permissions'

    name: Mapped[str] = mapped_column(String(20))
    roles: Mapped[List[Role]] = relationship(
        secondary=role_permission,
        back_populates='permissions',
        # cascade='all, delete'
    )


class Parent(Base):

    __tablename__ = 'parents'

    name: Mapped[str] = mapped_column(String(20))
    children: Mapped[List[Child]] = relationship(
        back_populates='parent',
        cascade='all, delete-orphan'
    )


class Child(Base):

    __tablename__ = 'children'
    name: Mapped[str] = mapped_column(String(20))
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey(Parent.__pk__))
    parent: Mapped[Parent] = relationship(back_populates='children')


engine = create_engine('sqlite:///cascade.sqlite')


@pytest.fixture(scope='module', autouse=True)
def init_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    users = [User(name=f'user-{i}') for i in range(10)]
    for user in users:
        user.address = [Address(street=f'street-{i}') for i in range(3)]
        user.profile = UserProfile(nickname='nick name')
    with Session(engine) as session:
        session.add_all(users)
        session.commit()


def test_delete_orphan(session):
    parent = Parent(name='parent')
    for i in range(3):
        parent.children.append(Child(name=f'child {i}'))
    session.add(parent)
    session.flush()

    child: Child = session.get(Child, 1)
    child.parent = None
    session.flush()


@pytest.fixture
def session():
    with Session(engine) as session:
        with session.begin():
            yield session


def test_success():
    assert True


def test_add_user_will_also_add_associated_address(session):
    user = User(name='john')
    user.address.append(Address(street='street'))
    session.add(user)
    session.flush()
    assert user.id > 0
    assert user.address[0].user_id == user.id


def test_delete_user_will_also_delete_associated_address_and_profile(session):

    addrs = session.scalars(
        select(Address).where(Address.user_id == 1)
    ).all()
    assert len(addrs) == 3

    profile = session.scalar(
        select(UserProfile).where(UserProfile.user_id == 1)
    )
    assert profile.user_id == 1

    user = session.get(User, 1)
    session.delete(user)
    session.flush()

    addrs = session.scalars(
        select(Address).where(Address.user_id == 1)
    ).all()

    assert addrs == []

    profile = session.scalar(
        select(UserProfile).where(UserProfile.user_id == 1)
    )
    assert profile is None


def test_add_address_associated_to_user_should_also_add_user(session):
    user = User(name='john')
    addr = Address(street='street')
    user.address.append(addr)
    session.add(addr)
    session.flush()
    assert user.id > 0
    assert addr.user_id == user.id


def test_add_address_not_not_associated_to_user(session):
    user = User(name='john smith')
    addr = Address(street='street 1')
    addr.user = user
    session.add(addr)
    session.flush()


@pytest.fixture(name='init_m2m')
def init_role_permissions(session):
    permissins = [Permission(name='permission-%d' % i) for i in range(5)]
    roles = [
        Role(name='role-%d' % i, permissions=permissins)
        for i in range(5)
    ]
    session.add_all(roles)


@pytest.mark.usefixtures('init_m2m')
def test_delete_many_to_many(session):
    role = session.get(Role, 1)
    session.delete(role)
