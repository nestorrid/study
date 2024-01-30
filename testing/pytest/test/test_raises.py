import pytest


def test_raises_exception():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("message")

    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == 'message'
