import pytest

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from .models import Base, User, Address


engine = create_engine('sqlite:///select.sqlite', echo=True)


@pytest.fixture(scope='module', autouse=True)
def init_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        address = Address(street='some street', zipcode='1111')
        user = User(name='test user')
        user.address = [address]
        session.add(user)
        user = User(name='noaddress user')
        session.add(user)
        session.commit()


@pytest.fixture
def session():
    with Session(engine) as session:
        with session.begin():
            yield session


def test_success():
    pass


def test_select_join(session):
    stmt = select(User).join(User.address)
    results = session.scalars(stmt).all()
    print(stmt)
    print(results)
    assert results[0].name == 'test user' and results[0].address[0].street == 'some street'


def test_select_join_entity(session):
    stmt = select(User).join(Address)
    results = session.scalars(stmt).all()
    print(stmt)
    print(results)
    assert results[0].name == 'test user' and results[0].address[0].street == 'some street'


def test_select_join_entity_with_on_clause(session):
    stmt = select(User).join(Address, User.id == Address.user_id)
    results = session.scalars(stmt).all()
    print(stmt)
    print(results)
    assert results[0].name == 'test user' and results[0].address[0].street == 'some street'


def test_select_where(session):
    stmt = select(User).where(User.address.any(Address.zipcode.contains('11')))
    results = session.scalars(stmt).all()
    assert len(results) == 1


def test_select_users_without_address(session):
    result = session.scalars(
        select(User).where(~User.address.any())
    ).first()
    assert result.name == 'noaddress user'


def test_select_user_by_id(session):
    user = session.get(User, 1)
    print(user)
    assert user.name == 'test user'
