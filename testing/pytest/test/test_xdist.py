import pytest
import time

pytestmark = pytest.mark.skip


def test_xdist_func1():
    time.sleep(1)
    assert 1 == 1


def test_xdist_func2():
    time.sleep(1)
    assert 1 == 1


def test_xdist_func3():
    time.sleep(1)
    assert 1 == 1


def test_xdist_func4():
    time.sleep(1)
    assert 1 == 1


def test_xdist_func5():
    time.sleep(1)
    assert 1 == 1


def test_xdist_func6():
    time.sleep(1)
    assert 1 == 1


"""
pytest -k xdist     
==== 6 passed, 17 deselected in 6.05s ====

pytest -n 4 -k xdist
==== 6 passed in 2.54s ====
"""
