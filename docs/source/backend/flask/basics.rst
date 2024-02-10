Flask 基础
================================================

安装Flask
------------------------------------------------

.. code-block:: bash

    pip install flask

    # or

    pipenv install flask

在安装Flask的同时, 会自动安装以下依赖:

Werkzeug
    用于提供web服务

Jinja
    模板页面渲染框架

MarkupSafe
    与Jinja一同安装的框架, 用于防止非授信代码注入, 提高项目安全性的框架.

ItsDangerous
    用于保护会话中cookie数据的安全.

Click
    用于开发命令行程序的框架.

Blinker
    添加 `Signals` 功能支持的框架.

从依赖功能来看, flask也属于麻雀虽小, 五脏俱全.

第一个Flask程序
------------------------------------------------

直接在项目中创建一个 `app.py` 文件, 编写代码:

.. code-block:: python

    from flask import Flask

    app = Flask(__name__)


    @app.route('/')
    def index():
        return "hello world"

启动Flask服务
------------------------------------------------

    在项目路径下, 通过命令 ``flask run`` 即可启动flask服务

.. code-block:: bash

    flask run

    # * Serving Flask app 'app'
    #* Debug mode: off
    #WARNING: This is a development server. 
    #Do not use it in a production deployment. Use a production WSGI server instead.
    #* Running on http://127.0.0.1:5000
    #Press CTRL+C to quit

此时, Flask服务程序便已启动成功, 通过浏览器访问地址 ``http://127.0.0.1:5000``, 即可在页面中看到 `hello world` 字样.

.. note:: 

    flask在运行服务器时, 如果没有指定要运行的文件, 会自动加载 `app.py` 或者 `wsgi.py` 文件.

flask 命令行参数
------------------------------------------------

--debug
    默认情况下, flask不会检测源代码的修改, 即修改代码后需要重启服务才能查看变化.

    为了能够实时查看更改内容, 可以在debug模式下运行服务. 添加参数 ``--debug`` 即可.

    .. code-block:: bash

        flask run --debug

--port
    设置服务端口, 默认为5000

--host
    设置服务地址, 开发模式下flask服务器默认只允许本机访问, 局域网内同样不可访问. 为了能够通过其他设备进行测试, 通常会更改ip设置.
    
    使用 `0.0.0.0` , 即可打开所有的可用ip.

    .. code-block:: bash

        flask run --debug --host=0.0.0.0 --port=5001
    
