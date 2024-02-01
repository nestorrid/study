import pytest

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session

from .models import Base, User, Address


engine = create_engine('sqlite:///insert.sqlite', echo=True)


@pytest.fixture(scope='module', autouse=True)
def init_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.fixture
def session():
    with Session(engine) as session:
        with session.begin():
            yield session


def test_success():
    pass


def test_insert_single_user_with_add(session):
    user = User(name='single user')
    session.add(user)
    assert session.query(User).count() == 1


def test_insert_single_user_with_execute(session):
    result = session.execute(insert(User).values({'name': 'execute user'}))
    print(result.inserted_primary_key)


def test_insert_multiple_users_with_params(session):
    resultset = session.execute(insert(User).returning(User), [
        {'name': f'user-{i}'}
        for i in range(10)
    ])
    print(resultset)
    print(resultset.all())


def test_insert_multiple_users_with_values(session):
    resultset = session.execute(insert(User).values([
        {'name': f'user-{i}'}
        for i in range(10)
    ]).returning(User))
    print(resultset)
    print(resultset.all())


def test_get_insert_user(session):
    result = session.scalar(
        insert(User).values({'name': 'John'}).returning(User)
    )
    print(result, result.id)
    assert result.name == 'John'


def test_get_insert_user_id(session):
    user_id = session.execute(
        insert(User).values({'name': 'John'}).returning(User.id)
    ).one().id
    print(user_id)
    assert user_id > 0


def test_insert_multiple_users_return_ids(session):
    data = [{'name': f'user-{i}'} for i in range(10)]
    results = session.execute(
        insert(User).returning(User.id, sort_by_parameter_order=True),
        data
    ).all()
    print(results)
    assert len(results) == 10


def test_insert_mutiple_address_for_same_user(session):
    user_id = session.execute(insert(User).values(
        {'name': 'multiple addr user'}).returning(User.id)).one().id

    list_addr = [
        {
            'street': f'street {i}',
            'zipcode': f'{i}' * 5,
        }
        for i in range(10)
    ]
    results = session.execute(
        insert(Address).values(user_id=user_id).returning(Address),
        list_addr
    )
    print(results.all())


def test_insert_user_with_multiple_address(session):
    user = User(name='john')
    user.address = [
        Address(street=f'street {i}', zipcode=f'{i}' * 5)
        for i in range(10)
    ]
    session.add(user)
