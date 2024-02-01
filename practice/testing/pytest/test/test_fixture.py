import string
from random import choice
from datetime import datetime
import time

import pytest


@pytest.fixture(scope='class', autouse=True)
def scope_class_fixture():
    print()
    print("class scope fixture start")
    yield
    print("class scope fixture end")


@pytest.fixture(scope='function', name='code')
def random_string(len=5):
    return "".join([choice(string.ascii_letters+string.digits) for _ in range(len)])


@pytest.fixture(name='timeit')
def performance(request):
    start = datetime.now()
    yield
    cost = datetime.now() - start
    print(
        f'\nfunction {request.function.__name__!r} time cost: %s.%ss'
        % (cost.seconds, cost.microseconds)
    )


@pytest.mark.usefixtures('timeit')
def test_performance():
    time.sleep(0.1)


def test_fixture_arg(code):
    print(code)
    assert len(code) == 5


def test_function1():
    print('test function1 in module.')


def test_function2():
    print('test function2 in module.')


class TestClass:

    def test_func1(self):
        print('test function1 in class.')

    def test_func2(self):
        print('test function2 in class.')


@pytest.fixture
def token():
    return "fake_token"


@pytest.fixture
def agent():
    return "fake_agent"


@pytest.fixture
def header(token, agent):
    return {
        'token': token,
        'user-agent': agent
    }


def test_fake_headers(header):
    print(header)


@pytest.fixture(params=['aa', 'bb', 'cc'], name='user')
def users(request):
    # request是pytest的内置参数, 本质也是一个fixture, 所以名称固定
    return request.param


def test_users(user):
    print(user)
