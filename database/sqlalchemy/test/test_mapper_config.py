from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

import pytest

from sqlalchemy import create_engine, String, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, column_property, mapped_column, Session, MappedAsDataclass
from sqlalchemy.orm import declared_attr
from models.types import intpk, str_15


class Base(MappedAsDataclass, DeclarativeBase):

    @declared_attr.directive
    def __pk__(cls) -> str:
        return f"{cls.__tablename__}.id"

    id: Mapped[intpk] = mapped_column(init=False, repr=False)


class Equipment(Base):
    __tablename__ = 'equipment'

    name: Mapped[str] = mapped_column()


def test_dataclass_model():
    equip = Equipment(name='aaa')
    print(equip)


class MixinFields(MappedAsDataclass):
    pass


class EmailFields(MixinFields):

    email: Mapped[Optional[str]] = mapped_column(
        String(50), unique=True, init=False)


class User(Base, EmailFields):
    __tablename__ = 'users'

    firstname: Mapped[str] = mapped_column(String(15))
    lastname: Mapped[str] = mapped_column(String(15))
    fullname: Mapped[str] = column_property(firstname + ' ' + lastname)


engine = create_engine('sqlite:///demos.sqlite', echo=False)


@pytest.fixture
def session():
    with Session(engine) as session:
        with session.begin():
            yield session


@pytest.fixture(scope='module', autouse=True)
def init_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    users = [User(firstname='John', lastname='Smith') for _ in range(5)]

    with Session(engine) as session:
        session.add_all(users)
        session.commit()


def test_success():
    assert True


def test_select_users_will_get_five_rows(session):
    users = session.query(User).all()
    assert len(users) == 5


def test_user_result_will_have_right_full_name(session):
    user: User = session.query(User).first()
    assert user.fullname == 'John Smith'


def test_dict():
    d = dict(
        a=1,
        b=2
    )
    print(d)


def test_pk_attr_will_get_tablename_dot_id():
    assert User.__pk__ == 'users.id'
