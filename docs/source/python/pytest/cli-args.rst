pytest常用命令行参数
================================================

* -v: 详细命令行输出

* -s: 不拦截打印文本

* -k: 运行包含指定关键字的测试用例
    ``pytest -k func``

* -q: 简化输出信息

  .. code-block:: bash
  
    >>> pytest -q     
    .sx..x..........

* -X: 遇到失败用例时结束.

* -n: 多线程执行测试用例, 需要`pytest-xdist`插件支持

  .. code-block:: python
  
    import pytest
    import time
    
    
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
    

* -m: 执行带有自定义装饰器标记的测试用例

  .. code-block:: python
  
    # 使用自定义标记首先需要对标记进行注册.
    
    # pytest.ini
    """
    [pytest]
    markers = 
        demo: a sample demo marker.
    """
    
    # test_marker.py
    import pytest
    
    @pytest.mark.demo
    def test_marker():
        assert 1 == 1
    
    # 运行带有`demo`标记的测试用例    
    # > pytest -m demo
    
    # 运行不包含`demo`标记的测试用例
    # > pytest -m "not demo"

* --reruns n: 重跑失败的测试用例, 需要使用插件`pytest-rerunfailures`

  .. code-block:: python
  
    import pytest
    
    def test_rerun_func():
        """
        pytest --reruns 10 -k rerun
        == 1 failed, 24 deselected, 10 rerun in 0.06s ==
    
        pytest --reruns 10 -k rerun --reruns-delay 1
        == 1 failed, 24 deselected, 10 rerun in 10.11s ==
        """
        pytest.fail()

  * --reruns-delay n: 重跑间隔时间

* --durations=n: 显示最慢的n个测试用例

  * -vv: 显示最慢测试用用例的详情

* --tb=[option]: 指定回溯信息格式

  * auto: 默认
  * long
  * short
  * line
  * native
  * no

* --full-trace: 完整的回溯信息

* --strict-markers: 只有内置, 插件注册和配置注册的标记可用.

* --lf, 进运行上次失败的用例

* --ff, 优先运行之前失败的用例

* -- nf, 优先运行新增的用例.

* -c FILE: 指定配置文件

* -p: 加载或禁用插件, 如`no:doctest`
