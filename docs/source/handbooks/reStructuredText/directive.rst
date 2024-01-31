================================================
指令
================================================

指令时reST的重要功能, 除了大量的内置只另外, 也可以进行指令的自定义.

通常来说, 指定的格式为::

    .. directive: arg
        :option: value

        content

常用基础指令
------------------------------------------------

rubric, 生成一个不在文章目录中显示的标题, 经常用来制作引用, 脚注的标题.

.. rubric:: This is a rubric title

.. note:: *.. note::*

.. warning:: *.. warning::*

.. versionadded:: *.. versionadded::*

.. versionchanged:: *.. versionchanged::*

.. deprecated:: *.. deprecated::*

.. seealso:: *.. seealso::*

.. centered:: *.. centered:: centerd text*

添加目录树.

::

    .. toctree::
        :maxdepth:: 3

        ...

------------------------------------------------

文本替换
    通过 ``|shortcut|`` 来声明文本标记, 并通过 `replace` 指令来将其替换成为目标文本.

简单案例::

    |RST|_ is a little annoying to type over and over, especially
    when writing about |RST| itself, and spelling out the
    bicapitalized word |RST| every time isn't really necessary for
    |RST| source readability.

    .. |RST| replace:: reStructuredText
    .. _RST: https://docutils.sourceforge.io/rst.html

|RST|_ is a little annoying to type over and over, especially
when writing about |RST| itself, and spelling out the
bicapitalized word |RST| every time isn't really necessary for
|RST| source readability.

.. |RST| replace:: reStructuredText
.. _RST: https://docutils.sourceforge.io/rst.html