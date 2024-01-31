pytest标记
================================================

装饰器标记
------------------------------------------------

通过 ``@pytest.mark.*`` 使用标记, 可以是内置标记, 也可以是自定义标记.

run
    默认情况下, pytest会按照模块名, 用例名, 从上而下顺序执行.

    可以通过`run`装饰器修改特定用例的执行顺序:

    .. code-block:: python
    
        @python.mark.run(order=n)


xfail
    预期失败, 有些用例会在特定情况下失败, 属于可预计且允许的失败, 此时可以添加`xfail`标记.

    .. code-block:: python

        @pytest.mark.xfail(reason="除数为0")
        def test_divide_by_zero():
            print(1 / 0)

skip
    无条件跳过测试用例.

    .. code-block:: python
    
        @pytest.mark.skip(reason='...')

skipif
    根据条件跳过测试用例.

    .. code-block:: python
    
        @pytest.mark.skipif(condition, reason='...')

模块标记
------------------------------------------------

通过 `pytestmark` 变量进行模块级的跳过, 该变量是pytest内置变量, 名称固定.

.. code-block:: python

    pytestmark = pytest.mark.skip


参数化
------------------------------------------------

当需要对不同的参数进行同样的测试时便可以使用参数化用例.

.. code-block:: python

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

`ids` 和 `argvalues` 两个参数的长度必须相同

叠加参数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

测试用例可以包含多个 `parametrize` 装饰器, 多个装饰器的参数会进行交叉匹配, 对所有可能的组合形式进行测试.

.. code-block:: python

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

