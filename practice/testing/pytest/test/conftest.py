import pytest


@pytest.fixture(scope='session', autouse=True)
def session_fixture():
    print('session_fixture started')
    yield
    print('session_fixture ended')
