import pytest


def setup():
    print("setup >>")


def teardown():
    print('teardown >>')


def setup_module():
    print('setup_module >>>>')


def teardown_module():
    print('teardown_module >>>>')


def setup_function():
    print('setup_function >>>>>>')


def teardown_function():
    print('teardown_function >>>>>>>')


def test_sample_test1():
    print('this is a sample test 1')


def test_sample_test2():
    print('this is a sample test 2')


class TestClass:

    @classmethod
    def setup_class(cls):
        print('setup class')

    @classmethod
    def teardown_class(cls):
        print('teardown class')

    def setup_method(self):
        print('setup method')

    def teardown_method(self):
        print('teardown method')

    def test_func_1(self):
        print('test func 1')

    def test_func_2(self):
        print('test func 2')
