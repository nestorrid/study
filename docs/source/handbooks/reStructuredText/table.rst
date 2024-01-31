================================================
表格
================================================

基础表格
------------------------------------------------

与markdown的表格格式类似, 属于直接用文本编辑想骂街的格式

==== ==== ====
A    B    C
==== ==== ====
1    2    3
1    2    3
1    2    3
1    2    3
==== ==== ====

::

    ==== ==== ====
    A    B    C
    ==== ==== ====
    1    2    3
    1    2    3
    1    2    3
    1    2    3
    ==== ==== ====

csv表格
------------------------------------------------

但是rst文件可以直接使用csv格式的数据制作表格, 使得表格的制作变得方便了许多

.. csv-table:: Some table
    :header: "Item", "Price", "Quantity", "Description"
    :widths: 20, 20, 20, 40
    :width: 100%

    "some item", 9.99, 10, "Sample description..."
    "some item", 9.99, 10, "Sample description..."
    "some item", 9.99, 10, "Sample description..."
    "some item", 9.99, 10, "Sample description..."

::

    .. csv-table:: Some table
        :header: "Item", "Price", "Quantity", "Description"
        :widths: 20, 20, 20, 40
        :width: 100%

        "some item", 9.99, 10, "Sample description..."
        "some item", 9.99, 10, "Sample description..."
        "some item", 9.99, 10, "Sample description..."
        "some item", 9.99, 10, "Sample description..."

list 表格
------------------------------------------------

也可以直接按照列表的形式来编辑表格

.. list-table:: Some table
    :widths: 20, 15, 15, 50
    :width: 100%
    :header-rows: 1

    *   - Item
        - Price
        - Quantity
        - Description
    *   - Some item
        - 9.99
        - 10
        - Sample description
    *   - Some item
        - 9.99
        - 10
        - Sample description
    *   - Some item
        - 9.99
        - 10
        - Sample description 

::

    .. list-table:: Some table
        :widths: 20, 15, 15, 50
        :width: 100%
        :header-rows: 1

        *   - Item
            - Price
            - Quantity
            - Description
        *   - Some item
            - 9.99
            - 10
            - Sample description
        *   - Some item
            - 9.99
            - 10
            - Sample description
        *   - Some item
            - 9.99
            - 10
            - Sample description

