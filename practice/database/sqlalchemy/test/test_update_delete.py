import pytest

from sqlalchemy import create_engine, update, delete
from sqlalchemy.orm import Session

from .models import Base, User, Address


engine = create_engine('sqlite:///update_delete.sqlite', echo=True)


@pytest.fixture(scope='module', autouse=True)
def init_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    users = [
        User(name=f'user-{i}')
        for i in range(10)
    ]

    for user in users:
        user.address = [
            Address(street=f'street {i}', zipcode=f'{i}' * 5)
            for i in range(10)
        ]

    with Session(engine) as session:
        session.add_all(users)
        print(session.new)
        session.commit()


@pytest.fixture
def session():
    with Session(engine) as session:
        with session.begin():
            yield session


def test_success():
    pass


def test_update_user_by_id(session):
    result = session.execute(
        update(User).where(User.id == 1).values({
            'name': 'new name'
        })
    )
    user = session.get(User, 1)
    assert user.id == 1
    assert user.name == 'new name'
    assert result.rowcount == 1


def test_update_user_with_id_lt_10(session):
    result = session.execute(
        update(User).where(User.id < 10).values({
            'name': User.name + ' test update'
        })
    )
    print(result.rowcount)
    assert result.rowcount > 0


def test_get_updated_user_id(session):
    result = session.scalars(
        update(User).where(User.name.contains('user')).values(
            {'name': 'new user name' + User.id}
        ).returning(User.id)
    ).all()
    print(result)
    assert len(result) > 0


def test_model_default_relation_field(session):
    user = User(name='new user')
    print(user.address)
    assert user.address == []
    addr = Address(street='street', zipcode='123')
    user.address.append(addr)
    print(addr.user)


def test_model_should_have_pk_after_session_flush(session):
    u = User(name='new user')
    session.add(u)
    assert u.id is None
    session.flush()
    assert u.id > 0
