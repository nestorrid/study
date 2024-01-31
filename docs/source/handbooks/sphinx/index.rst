================================================
Sphinx 速查手册
================================================

sphinx简介
------------------------------------------------

Sphinx是用于制作项目文档的框架, 是目前最为流行的python项目文档构建工具.

`Sphinx`_

.. _Sphinx: https://www.sphinx-doc.org/en/master/

安装
------------------------------------------------

在Mac OS系统下, 直接使用pip完成安装即可:

.. code-block:: bash

    pip install sphinx


创建文档项目
------------------------------------------------

.. code-block:: bash

    mkdir docs && cd docs
    sphinx-quickstart

    欢迎使用 Sphinx 7.2.6 快速配置工具。

    请输入接下来各项设定的值（如果方括号中指定了默认值，直接
    按回车即可使用默认值）。

    已选择根路径：.

    有两种方式来设置用于放置 Sphinx 输出的构建目录：
    一是在根路径下创建“_build”目录，二是在根路径下创建“source”
    和“build”两个独立的目录。
    > 独立的源文件和构建目录（y/n） [n]: y
    # 将源文件和构建目录分离方便与之后的管理

    项目名称将会出现在文档的许多地方。
    # 需要输入的三项基本信息
    > 项目名称: Demo documentation
    > 作者名称: Nestor
    > 项目发行版本 []: 0.1.0

    如果用英语以外的语言编写文档，
    你可以在此按语言代码选择语种。
    Sphinx 会把内置文本翻译成相应语言的版本。

    支持的语言代码列表见：
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language。
    > 项目语种 [en]: zh_CN

    正在创建文件 /Users/nestor/Workspace/projects/playground/sphinx_doc/source/conf.py。
    正在创建文件 /Users/nestor/Workspace/projects/playground/sphinx_doc/source/index.rst。
    正在创建文件 /Users/nestor/Workspace/projects/playground/sphinx_doc/Makefile。
    正在创建文件 /Users/nestor/Workspace/projects/playground/sphinx_doc/make.bat。

    完成：已创建初始目录结构。

    你现在可以填写主文档文件 path/to/docs/source/index.rst 然后创建其他文档源文件了。 像这样用 Makefile 构建文档：
      make builder
    此处的“builder”代指支持的构建器名称，比如 html、latex 或 linkcheck。


    > ### Tips
    >
    > sphinx框架本身已经添加了中文支持, 在使用命令时提示文字会根据系统语言进行切换.

构建完成之后, 文档文件夹下将包含以下内容:

* build: 文档输出内容.
* source: 文档源文件, 基于reStructuredText格式或者Markdown文件(需要配置).
* conf.py: 项目配置文件, 基本信息, 扩展, 主题等配置.
* make.bat: windows下的构建批处理文件, mac下没用.
* Makefile: 文档构建工具, 直接使用`make html`即可构建静态站点文档.

自动读取模块文档
------------------------------------------------

需要使用插件`sphinx-apidoc`, 并在`conf.py`文件中添加配置:

假定项目结构目录为

    | project
    | 	docs
    |			source
    |				conf.py
    |		project
    |			module
    | 		...

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../..')) # 向上两层目录, 将项目根目录, 即`project`添加到路径中

    extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    ]

在`docs`文件夹下执行指令:

.. code-block:: bash

    sphinx-apidoc -o source ../target


.. note:: 

    target为源码目录, 通常来说, 常见的项目目录为:
    
    - project
        - doc
    	- project
		- packages
			- modules

该命令会在`source`文件夹下生成两个文件:

* modules.rst: 模块主页, 包含了所读取模块的内容. 需要修改`index.rst`引入该文件.

  .. code-block:: reST
  
    .. toctree::
       :maxdepth: 2
       :caption: Contents:
    
       modules
    

* target.rst: 模块中的包, 子模块等内容的对应文件. 包含在`modules.rst`文件中, 无需更改

.. note:: 

    `target` 目录必须为python包, 即包含 `__init__.py` 文件, 否则无法通过自动读取构建文档.

构建文档
------------------------------------------------

通过命令 `make html` 构建文档, 会默认输出到 `build/html` 目录下.

选择主题
------------------------------------------------

在`conf.py`文件内控制生成文档的主题, 默认为:

.. code-block:: python

    html_theme = 'alabaster' # 默认主题


需要先安装主题才能使用, 直接通过pip命令安装即可. 可以在 https://sphinx-themes.org 查看更多主题.

几款效果不错的主题:

* `Book <https://sphinx-themes.org/sample-sites/sphinx-book-theme/#>`_: 支持明暗切换, 配色比较舒服.

.. code-block:: python
  
    # pipenv install sphinx-book-theme
    
    html_theme = 'sphinx_book_theme'
    

* `Furo <https://sphinx-themes.org/sample-sites/furo/>`_: 字体稍小, 可以自行调整. 整体感官也不错, 支持明暗切换. python官方文档选用该主题.

.. code-block:: python

    # pipenv install furo
    
    html_theme = 'furo'

添加插件
------------------------------------------------

sphinx可以自行配置插件, 几个简单好用的插件:

* `sphinx-copybutton <https://github.com/executablebooks/sphinx-copybutton#readme>`_: 在代码块中添加复制按钮

.. code-block:: python

    # pipenv install sphinx-copybutton

    # conf.py
    extensions.append('sphinx_copybutton')

* `sphinx-inline-tabs <https://github.com/pradyunsg/sphinx-inline-tabs#readme>`_: 在文档中添加标签页

.. code-block:: python

    # pipenv install sphinx-inline-tabs

    # conf.py
    extensions.append("sphinx_inline_tabs")

