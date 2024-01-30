from __future__ import annotations
from typing import Optional, List

from sqlalchemy import select, create_engine
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Session
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm import declared_attr


class Base(DeclarativeBase, MappedAsDataclass):

    @declared_attr.directive
    def __pk__(cls):
        return f'{cls.__tablename__}.id'

    id: Mapped[int] = mapped_column(primary_key=True, init=False, repr=False)


class User(Base):

    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String(20))
    address: Mapped[List[Address]] = relationship(
        init=False, repr=False, back_populates='user')


class Address(Base):

    __tablename__ = 'addresses'

    user_id: Mapped[int] = mapped_column(ForeignKey(User.__pk__), init=False)
    street: Mapped[str] = mapped_column(String(50))
    zipcode: Mapped[str] = mapped_column(String(15))
    user: Mapped[User] = relationship(init=False, back_populates='address')
