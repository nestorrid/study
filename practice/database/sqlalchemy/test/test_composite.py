import dataclasses

from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import composite, mapped_column


@dataclasses.dataclass
class Point:
    x: int
    y: int


class Base(DeclarativeBase):
    pass


class Vertex(Base):
    __tablename__ = "vertices"

    id: Mapped[int] = mapped_column(primary_key=True)

    start: Mapped[Point] = composite(mapped_column("x1"), mapped_column("y1"))
    end: Mapped[Point] = composite(mapped_column("x2"), mapped_column("y2"))

    def __repr__(self):
        return f"Vertex(start={self.start}, end={self.end})"


@dataclasses.dataclass
class FullName:
    firstname: str
    lastname: str


class User(Base):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)

    fullname: Mapped[FullName] = composite(
        mapped_column('firstname', String(15)), mapped_column('lastname', String(15)))


def test_create_table():
    engine = create_engine('sqlite:///composite.sqlite', echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
