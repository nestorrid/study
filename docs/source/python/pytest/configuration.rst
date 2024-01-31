编辑配置文件
================================================

pytest.ini
------------------------------------------------

可以在项目中创建`pytest.ini`文件用来进行配置管理.

addopts
    添加命令行参数

    addopts= -s -v

testpaths
    添加搜索文件夹
    
    path1 path2

python_files
    修改文件匹配方式

    python_files = \*test.py

python_classes
    修改类匹配方式
    
    python_classes = Test_*

python_functions
    修改类中方法的匹配方式
    
    python_functions = xxx_*

markers
    注册用例标记
    
    markers = mark1 mark2

log\_*
    日志管命令

    * log_cli = True
    * log_cli_date_format = ...
    * log_cli_format = fmt...
    * log_cli_level = ...
    * log_file = ...
    * log_file_date_format = ...
    * log_file_format = ...
    * log_file_level = ...
    * log_format = ...
    * log_level = ...

usefixtures
    指定全局fixture
    
    usefixtures =  myfix: 等同于为所有的测试用例添加myfix固件.

------------------------------------------------

conftest.py
------------------------------------------------

通用的fixture和全局变量设置内容会放到 `conftest.py` 文件中.

一个项目可以包含多个`conftest`文件, 每个文件对当前包和子包有效, 即父包不可访问子包的conftest, 但是子包可以访问父包的conftest, 且优先使用当前包的内容.

该文件的名称是固定的, 否则无法生效.

其中定义的fixture不需要导包即可在测试模块中直接使用.

.. note:: conftest.py文件中的常用变量

    **collect_ignore**
        定义跳过的模块, 字符串数组

    **collect_ignore_glob**
        作用相同, 区别在于可以使用通配符

    **pytest_plugins**
        注册插件

