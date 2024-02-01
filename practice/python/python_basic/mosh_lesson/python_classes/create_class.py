# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : create_class.py
# @Date         : 2023/11/5 14:37
#
# @Description  :
#

class Point:

    color = "red"  # 类变量, 可以通过类或者对象访问

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def draw(self):
        print(f"draw at: ({self.x},{self.y})")


p1 = Point()
print(type(p1))
p1.draw()
print(isinstance(p1, Point))
print(isinstance(p1, int))
print(isinstance(p1, object))

# python中对象的成员是动态的,可以在任意时间为对象新增成员变量
p1.z = 100
print(p1.z)

p2 = Point(1, 1)

print(Point.color)
print(p1.color)
print(p2.color)

p3 = Point(2, 2)
p3.color = "green"  # 直接通过对象修改成员变量的值
Point.color = "blue"  # 通过类更改类变量的值,将直接影响所有保持默认值的对象

print(Point.color)
print(p1.color)
print(p2.color)
print(p3.color)
