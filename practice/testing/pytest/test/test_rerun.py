import pytest


def test_rerun_func():
    """
    pytest --reruns 10 -k rerun
    == 1 failed, 24 deselected, 10 rerun in 0.06s ==

    pytest --reruns 10 -k rerun --reruns-delay 1
    == 1 failed, 24 deselected, 10 rerun in 10.11s ==
    """
    pytest.fail()
