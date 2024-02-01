# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : properties.py
# @Date         : 2023/11/5 16:17
#
# @Description  :
#

class Product:

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price must be positive")
        self.__price = value


p = Product(10)
p.price = -1
