REST API 规范
================================================

REST(REpresentational State Transfer)是一种服务器接口的规范, 简单来说, 就是通过HTTP的请求方式来区别接口.

在早期的web项目中, 一些接口的定义缺乏规范, 对于一些具备命名规范的项目而言, 可能会遇到一些这样的接口

- /getProducts
- /listOrders
- /retrieveClientByOrder?orderId=1

用何种方式请求接口, 需要哪些参数, 等等借口细节在了没有文档支持的情况下几乎完全无法使用.

而RESTful API的方式, 则是对API的一种规范, 以 `/product` 为例

.. csv-table:: RESTful API for product
    :header: "METHOD", "API", "DESCRIPTION"
    :widths: 15, 30, 55
    :width: 100%

    "GET", "/products", "获取product列表, 可以通过参数获取额外信息, 比如?page=2&limit=20"
    "GET", "/products/1", "获取id为1的product详情信息"
    "POST", "/products", "添加一条新的 product记录"
    "PUT/PATCH", "/products/2", "更新id为2的 product 信息"
    "DELETE", "/products/5", "删除id为5的 product 信息"

几个基本的接口名称定义规则:

- URI使用名词, 而非动词, 并且推荐使用复数形式;
    以上述接口为例, products本身即为要操作的目标, 而通过`GET`, 'POST'等请求方式的不同便可以明确希望通过该接口要执行的操作.

    而类似于 `add`, `insert`, `get`, `update` 等一类的动词是不推荐出现在接口定义之中.

- 保证 `HEAD` 和 `GET` 方法是安全的;
    即仅仅只是获得数据, 而不会对内容做出修改.

    .. warning:: 该类接口不应该在REST API中出现

        GET /deleteProducts?id=1
    
- 返回正确的状态码;
    根据通用的状态码规范定义返回状态, 通常来说, 2xx代表请求成功, 3xx代表重定向, 4xx代表客户端错误, 5xx代表服务端错误.

    .. note::

        扩展资料: `状态码速查 <https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status>`_
    