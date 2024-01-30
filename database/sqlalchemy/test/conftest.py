import pytest


@pytest.fixture(name='names')
def fake_names():
    return ['张三', '李四', '王五', '赵六']
