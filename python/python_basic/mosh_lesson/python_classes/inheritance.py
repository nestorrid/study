# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : inheritance.py
# @Date         : 2023/11/5 16:34
#
# @Description  :
#

class BaseClass:

    class_id = 1

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} eat")


class SubClass(BaseClass):

    def __init__(self, name):
        super().__init__(name)
        self.age = 1

    def walk(self):
        print(f"{self.name} walk")


class SubClass2(BaseClass):
    def swim(self):
        print(f"{self.name} swim")


s1 = SubClass("a")
print(s1.class_id)
s1.eat()
s1.walk()

s2 = SubClass2("b")
print(s2.class_id)
s2.eat()
s2.swim()

print(isinstance(s1, SubClass))
print(isinstance(s1, BaseClass))
print(isinstance(s1, SubClass2))

print(issubclass(SubClass, BaseClass))
print(issubclass(SubClass, SubClass2))
