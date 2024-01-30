from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .types import intpk


class UserBase(DeclarativeBase):

    id: Mapped[intpk]


class User(UserBase):

    __tablename__ = 'test_user'
    name: Mapped[Optional[str]]
