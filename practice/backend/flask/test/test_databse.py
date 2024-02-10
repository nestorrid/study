import pytest

from sqlalchemy import text

from app import app, db


@pytest.fixture(scope='module', autouse=True)
def flask_context():
    with app.app_context() as ctx:
        yield ctx


@pytest.fixture
def conn():
    with db.engine.connect() as conn:
        yield conn


def test_session():
    rs = db.session.execute(text('select 1')).fetchall()
    assert rs == [(1,)]


def test_conn(conn):
    rs = conn.execute(text('select 1')).fetchall()
    assert rs == [(1,)]


def test_print_current_module_name():
    print(__name__)
    print(__file__)
    print(__package__)
