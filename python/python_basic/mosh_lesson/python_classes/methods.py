# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : methods.py
# @Date         : 2023/11/5 15:16
#
# @Description  :
#
from typing import Type


class MyColor:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def print(self):
        """
        成员方法, 通过对象调用
        """
        print(f"({self.r, self.g, self.b})")

    @classmethod
    def white(cls):
        """
        类方法, 通过@classmethod定义, 在调用时默认传入类型,此处即MyColor
        """
        return cls(0, 0, 0)

    @staticmethod
    def to_hex(r=0, g=0, b=0):
        """
        静态方法, 通过类名调用
        """
        c = r << 16 | g << 8 | b
        print(f"({hex(c)})")

    def __str__(self) -> str:
        """
        magic method, 魔术方法, 继承自object类的一些特殊内置方法
        如`__str__`返回对象的字符串描述等等
        通过print方法打印对象时便是通过该方法获取对象的字符串描述
        """
        return f"({self.r},{self.g},{self.b})"

    def __eq__(self, o) -> bool:
        """
        判断两个对象是否相等的魔术方法
        """
        return self.r == o.r and self.g == o.g and self.b == o.b

    def __add__(self, other):
        """
        使对象支持加法数学运算的魔术方法
        """
        return MyColor(self.r + other.r, self.g + other.g, self.b + other.b)


MyColor.to_hex(255, 255, 255)
c = MyColor(15, 25, 33)
print(c)
