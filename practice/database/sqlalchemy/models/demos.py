from __future__ import annotations

from typing import Optional
from datetime import datetime
from decimal import Decimal
from enum import Enum

from typing_extensions import Annotated

import sqlalchemy
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, column_property

from .types import *
from .base import Base


class Status(Enum):
    PENDING = "pending"
    RECEIVED = "received"
    COMPLETED = "completed"


class EnumDemo(Base):

    __tablename__ = 'enum_demo'

    name: Mapped[str_15]
    status: Mapped[Status]


class DemoDefault(Base):

    __tablename__ = 'demo_default'

    name: Mapped[str] = mapped_column(default="default")


class TypeMapping(Base):
    """
CREATE TABLE type_mapping (
        s1 VARCHAR(30) NOT NULL, 
        s2 VARCHAR(50) NOT NULL, 
        d1 NUMERIC(16, 4) NOT NULL, 
        d2 NUMERIC(6, 2) NOT NULL, 
        last_edit DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL, 
        created DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL, 
        id INTEGER NOT NULL, 
        PRIMARY KEY (id)
)
    """

    __tablename__ = 'type_mapping'

    s1: Mapped[str_30]
    s2: Mapped[str_50]
    d1: Mapped[dec_16_4]
    d2: Mapped[dec_6_2]
    last_edit: Mapped[update_timestamp]
    created: Mapped[timestamp]


class Record(Base):
    __tablename__ = 'records'

    name: Mapped[str_50] = mapped_column(unique=True)
    count: Mapped[Optional[int]] = mapped_column(insert_default=0)

    def __repr__(self):
        return f'<Records(name={self.name!r})>'


class Departments(Base):

    __tablename__ = 'departments'

    name: Mapped[str_50] = mapped_column(unique=True)
    description: Mapped[Optional[str]]

    def __repr__(self):
        return f'<Deptments(id={self.id!r}, name={self.name!r}, create_date={self.create_date!r})>'


class Employee(Base):

    __tablename__ = 'employees'

    firstname: Mapped[str_30]
    lastname: Mapped[str_30]
    mail: Mapped[Optional[str_30]] = mapped_column(unique=True)
    salary: Mapped[Optional[dec_16_4]]
