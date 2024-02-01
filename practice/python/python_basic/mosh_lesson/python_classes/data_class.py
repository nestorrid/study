# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : data_class.py
# @Date         : 2023/11/5 17:22
#
# @Description  :
#
from collections import namedtuple

# 对于仅有成员变量, 没有属性的类, 可以通过namedtuple方法来制作数据类
MyPoint = namedtuple("MyPoint", ["x", "y"])


class Point:
    """
    一个仅用于储存数据的类
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)

p3 = MyPoint(1, 2)
p4 = MyPoint(1, 2)
print(p3 == p4)
