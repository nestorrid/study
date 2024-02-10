import pytest
from app import app
from flask import Response
from flask.testing import FlaskClient

app.testing = True


def get(url) -> Response:
    with app.test_client() as client:
        return client.get(url)


def test_app_root():

    rs = get('/')
    print(rs.json)

    assert rs.status_code == 200
    assert rs.data == b'hello world!'
    assert rs.text == 'hello world!'


def test_max_int():
    import sys
    print(sys.maxsize)
