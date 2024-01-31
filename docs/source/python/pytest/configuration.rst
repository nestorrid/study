编辑配置文件
================================================

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


