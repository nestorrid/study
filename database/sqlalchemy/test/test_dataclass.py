from typing import Optional
from dataclasses import dataclass, field
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass


class Base(DeclarativeBase, MappedAsDataclass):
    """subclasses will be converted to dataclasses"""
    pass


class FieldMixin(MappedAsDataclass):
    pass


class ContactMixin(FieldMixin):

    mail: Mapped[Optional[str]] = mapped_column(init=False)
    tel: Mapped[Optional[str]] = mapped_column(init=False)


class User(Base, ContactMixin):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    temp: Mapped[str] = mapped_column(default=None)


def test_dataclass_user():
    u = User(name='aaa')
    print(u)
