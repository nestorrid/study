import pytest


@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print('module_fixture start')
    yield
    print('module_fixture end')


def test_func1():
    print('test_func1')


def test_func2():
    print('test_func2')
