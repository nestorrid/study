路由
================================================

flask中的基础路由定义极为简单. 通过在python函数上添加 `@app.route()` 装饰器, 即可以完成路由配置.

函数体既是该请求要完成的功能.

返回值便是服务器的响应数据.

.. code-block:: python

    @app.route('/')
    def index():
        return "hello world"

接收请求参数
------------------------------------------------

在路由中通过 `<type:arg_name>` 来声明url参数

.. code-block:: python

    @app.route('/<int:user_id>')
    def get_user(user_id):
        return f'User: {user_id}'

也可以通过 `flask.request` 对象获取请求的参数

.. code-block:: python

    @app.route('/arg')
    def print_arg():
        id = request.args.get('id', 1)
        return f'request id is {id!r}'

设置路由函数接受的请求
------------------------------------------------

直接在函数的装饰器中通过 `methods` 参数即可指定接受的请求方式, 该参数接受一个字符串数组, 默认为 `GET`.

.. code-block:: python

    @app.route('/list')
    def get_list():
        pass

    @app.route('/list', methods=['POST'])
    def create_list_item():
        pass