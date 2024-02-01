import string
from random import choice

import pytest
import sqlalchemy
from sqlalchemy import create_engine, Engine, select, insert
from sqlalchemy.orm import Session
from models import *


def random_str(len=5):
    chars = string.ascii_letters + string.digits
    return "".join([choice(chars) for _ in range(len)])


def count_rows(session, model):
    return session.query(model).count()


engine = create_engine('sqlite:///test_db.sqlite', echo=False)


@pytest.fixture
def session():
    with Session(engine) as session:
        with session.begin():
            yield session


@pytest.fixture(scope='module', name='stmts')
def fake_data_statements():
    return [
        fake_records_statements()
    ]


def fake_records_statements():
    return insert(Record).values([
        {'name': f'fake_name_{i}'}
        for i in range(10)
    ])


@pytest.fixture(scope='module', autouse=True)
def init_database(stmts):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with engine.connect() as conn:
        for stmt in stmts:
            conn.execute(stmt)
        conn.commit()
        conn.close()


def test_init_database_contains_ten_records(session):
    results = session.query(Record).all()
    assert len(results) >= 10


def test_insert_record(session):
    before = session.query(Record).count()
    session.add(Record(name='test name'))
    session.flush()
    after = session.query(Record).count()
    assert after - before == 1


def test_sample_select(session):
    query = select(Record).where(Record.name.contains('fake'))
    results = session.scalars(query).fetchall()
    assert len(results) > 0


def test_insert_record_with_json_data(session, names):
    before = count_rows(session, Record)
    values = [{'name': name} for name in names]
    result = session.execute(
        insert(Record).values(values)
    )
    session.flush()

    assert count_rows(session, Record) - before == len(names)


def test_session_query(session):
    results = session.query(Record).filter(Record.id < 10)
    assert results.count() > 0


@pytest.fixture(name='init_depart')
def init_department_data(session):
    query = insert(Departments).values([
        {'name': f'depart-{i}'}
        for i in range(10)
    ])
    session.execute(query)


@pytest.mark.usefixtures('init_depart')
def test_query_departments_should_have_results(session):
    stmt = select(Departments)
    results = session.scalars(stmt).all()
    assert len(results) > 0


def test_insert_department(session):
    query = insert(Departments).values([
        {"name": "develop", "description": "test description"},
        {"name": "sales", "description": "test description"},
    ])
    session.execute(query)
    assert session.query(Departments).count() >= 2


def test_insert_enum_column(session):
    query = insert(EnumDemo).values({
        "name": "test enum",
        'status': Status.PENDING
    })
    session.execute(query)
    row = session.scalar(select(EnumDemo))
    assert row.name == 'test enum'
    assert row.status == Status.PENDING


def test_insert_row_with_default_value_column(session):
    row = DemoDefault()
    query = insert(DemoDefault)
    session.execute(query)
