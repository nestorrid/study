import pytest


@pytest.mark.parametrize(
    argnames=["x", "y"],
    argvalues=[(1, 2), (3, 4)],
    ids=['TC-1', 'TC-2']
)
def test_params(x, y):
    """
    argnames: 用例接受的形参名字, 元组或列表
    argvalues: 实参的值, 元组或列表组成的元组或列表
    ids: 用例编号
    """
    print(f"{x} + {y} = { x + y}")


@pytest.mark.parametrize(["a"], [(1,), (2,), (3,)])
@pytest.mark.parametrize(["b", "c"], [(1, 2), (2, 3), (3, 4)])
def test_combinations(a, b, c):
    """
    a有3种组合
    b,c 共有3种组合
    总共执行9次测试
    """
    print(f'a,b,c is {a!r}, {b!r}, {c!r}')


@pytest.mark.parametrize(["a"], [(1,), (2,), (3,)])
@pytest.mark.parametrize(["b"], [(1,), (2,), (3,)])
@pytest.mark.parametrize(["c"], [(1,), (2,), (3,)])
def test_combinations_2(a, b, c):
    """
    a,b,c各有3种组合, 总共执行27次
    """
    print(f'a,b,c is {a!r}, {b!r}, {c!r}')
