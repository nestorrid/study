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
import pytest


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


def test_create_table():
    engine = create_engine('sqlite:///relation.sqlite', echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def test_pk():
    assert Parent.__pk__ == 'parent.id'
