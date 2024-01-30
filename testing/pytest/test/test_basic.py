import pytest


def test_first_test():
    print('第一条测试用例')
    assert True


@pytest.mark.xfail(reason="test -X parameter, it should be failed.")
def test_faile():
    pytest.fail()


@pytest.mark.skip("skip demo")
def test_skipped_test():
    print('this test will be skipped.')
    assert False


@pytest.mark.xfail(reason="除数为0")
def test_divide_by_zero():
    print(1 / 0)


def setup():
    print('setup')


def teardown():
    print('teardown')


@pytest.mark.xfail(reason="parent module cannot use fixture in subpackage")
def test_fixture_in_subpackage_conftest(subfixture):
    print(subfixture)


class TestClass:

    def test_func_in_class(self):
        print('在测试类中的测试方法')
        assert True
