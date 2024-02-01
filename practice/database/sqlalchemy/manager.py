import threading
from typing import Type, TypeVar, Sequence

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.exc import OperationalError

_SQLAlchemyBaseModel = TypeVar('BASE', bound=DeclarativeBase)


class SingletonMeta(type):

    __instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with SingletonMeta.__instance_lock:
                if not hasattr(cls, '_instance'):
                    obj = object.__new__(cls)
                    cls.__init__(obj, *args, **kwargs)
                    cls._instance = obj
        return cls._instance


1


class ModelManager(metaclass=SingletonMeta):

    def __init__(
            self,
            base_model: Type[_SQLAlchemyBaseModel],
            *,
            database='sqlite:///test_db.sqlite',
            echo=False
    ):
        self.echo = echo
        self.database = database
        self._engine = create_engine(self._database, echo=self.echo)
        self._base_model = base_model

    def execute(self, stmts: Sequence[Type[any]]):
        with Session(self.engine) as session, session.begin():
            for stmt in stmts:
                session.execute(stmt)

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, value):
        self._database = value
        self._engine = create_engine(self._database, echo=self.echo)

    @property
    def engine(self):
        return self._engine

    @staticmethod
    def instance():
        return ModelManager()

    def create_table(self, model: Type[_SQLAlchemyBaseModel] = None):
        base = model if model else self._base_model
        try:
            base.metadata.create_all(self.engine)
        except OperationalError:
            pass

    def drop_table(self, model: Type[_SQLAlchemyBaseModel] = None):
        base = model if model else self._base_model
        try:
            base.metadata.drop_all(self.engine)
        except OperationalError:
            pass
