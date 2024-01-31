核心功能
================================================

测试夹具
------------------------------------------------

在执行测试之前和之后要执行的内容, 通过 `setup` 和 `teardown` 前缀的方法来定义夹具. 

.. code-block:: python

    import pytest

    def setup():
        print("setup")

    def teardown():
        print('teardown')

    def test_sample_test():
        print('this is a sample test')

    """
    输出结果:

    test/test_fixture.py setup
    this is a sample test
    .teardown
    """

详细案例:

.. code-block:: python

    import pytest

    # 在指定了setup_module方法之后并没有被执行
    # 但在取消掉`setup_module`方法之后与之有相同的作用
    def setup():
        print("setup >>")


    def teardown():
        print('teardown >>')

    # 模块运行和结束时执行一次
    def setup_module():
        print('setup_module >>>>')


    def teardown_module():
        print('teardown_module >>>>')

    # 每个方法运行前后执行一次
    def setup_function():
        print('setup_function >>>>>>')


    def teardown_function():
        print('teardown_function >>>>>>>')


    def test_sample_test1():
        print('this is a sample test 1')


    def test_sample_test2():
        print('this is a sample test 2')


    class TestClass:
        
        # 类在创建和销毁时执行一次
        @classmethod
        def setup_class(cls):
            print('setup class')

        @classmethod
        def teardown_class(cls):
            print('teardown class')
            
        # 类中的每个方法执行前后执行一次
        def setup_method(self):
            print('setup method')

        def teardown_method(self):
            print('teardown method')

        def test_func_1(self):
            print('test func 1')

        def test_func_2(self):
            print('test func 2')

输出结果:

.. code-block:: bash

    > pytest test/test_setup*.py -s

    test/test_setup_teardown.py session_fixture started
    setup_module >>>>
    setup_function >>>>>>
    this is a sample test 1
    .teardown_function >>>>>>>
    setup_function >>>>>>
    this is a sample test 2
    .teardown_function >>>>>>>
    setup class
    setup method
    test func 1
    .teardown method
    setup method
    test func 2
    .teardown method
    teardown class
    teardown_module >>>>
    session_fixture ended

fixture
------------------------------------------------

fixture装饰器可以定义一个固件, 该固件即可以作为夹具, 也可以作为参数等多种作用.

.. code-block:: python

    @pytest.fixture(
        scope='function', # 默认为函数级
        autouse=False, # 默认为False, 如果设置为True, 则会根据指定的作用域自动执行
        params=[], # 参数化列表
        ids=[], # 参数化id
        name='' # 固件别名
    )

作用域
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixture固件主要分为四类:

* 函数夹具(默认), function: 在所有的测试函数执行时生效
* 类夹具, class: 对于单独的测试函数, 与function作用域相同, 但对于测试类中的方法, 仅在类创建和销毁时执行
* 模块夹具, module: 在py文件内执行一次
* 包夹具, package: 在包中执行一次
* 会话夹具, session: 在测试会话中执行一次

.. code-block:: python

    @pytest.fixture(scope='class', autouse=True)
    def scope_class_fixture():
        print()
        print("class scope fixture start")
        # yield 之前的内容相当于setup, 其后的内容相当于teardown
        yield
        print("class scope fixture end")

    # 两个方法都会输出固件内容
    def test_function1():
        print('test function1 in module.')


    def test_function2():
        print('test function2 in module.')

    # 类中的方法仅输出一次固件内容    
    class TestClass:

        def test_func1(self):
            print('test function1 in class.')

        def test_func2(self):
            print('test function2 in class.')

使用别名
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

固件可以制定别名, 别名可以在随后使用, 或者用作参数将固件的返回值传递给某个测试用例

.. code-block:: python

    @pytest.fixture(name='code')
    def random_string(len=5):
        return "".join([choice(string.ascii_letters+string.digits) for _ in range(len)])

    # 将fixture的返回值作为参数
    def test_fixture_arg(code):
        print(code)
        assert len(code) == 5

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
    
    # function 'test_performance' time cost: 0.105647s  

fixture嵌套
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fixture可以调用其他的fixture, 以此来将复杂的功能进行拆分.

.. code-block:: python

    @pytest.fixture
    def agent():
        return "fake_agent"

    @pytest.fixture
    def token():
        return "fake_token"
    
    @pytest.fixture
    def header(token, agent):
        return {
            'token': token,
            'user-agent': agent
        }

    def test_fake_headers(header):
        print(header)
        assert 1 == 1

fixture实现参数化
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

通过fixture同样可以实现测试用例的参数化.

.. code-block:: python

    @pytest.fixture(params=['aa', 'bb', 'cc'], name='user')
    def users(request):
        # request是pytest的内置参数, 本质也是一个fixture, 所以名称固定
        return request.param


    def test_users(user):
        print(user)

常用的内置fixture
------------------------------------------------

capfd
    用于拦截命令行的输出

    .. code-block:: python
    
        def test_system_echo(capfd):
            os.system('echo "hello"')
            captured = capfd.readouterr()
            assert captured.out == "hello\n"



caplog
    拦截日志信息, 返回一个LogCaptureFixture对象, 通过内置的属性获取具体信息

        caplog.messages        list of format-interpolated log messages
        caplog.text            string containing formatted log output
        caplog.records         list of logging.LogRecord instances
        caplog.record_tuples   list of (logger_name, level, message) tuples
        caplog.clear()         clear captured records and formatted log output string


capsys
    与 `capfd` 功能类似, 同样用于拦截命令行输出

    .. code-block:: python
    
        def test_output(capsys):
            print("hello")
            captured = capsys.readouterr()
            assert captured.out == "hello\n"

request
    特殊的内置方法, 保存了调用测试用例的请求信息.



内置方法
------------------------------------------------

pytest.importorskip
    导入指定的模块, 如果导入失败则跳过当前测试模块

    .. code-block:: python
    
        docutils = pytest.importorskip("docutils")

pytest.raises
    期望抛出指定的异常, 如果抛出则运行通过, 否则失败

    .. code-block:: python
    
        def test_raises_exception():
            with pytest.raises(ValueError) as exc_info:
                raise ValueError("message")

            assert exc_info.type is ValueError
            assert exc_info.value.args[0] == 'message'

