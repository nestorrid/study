# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : custom_container.py
# @Date         : 2023/11/5 15:45
#
# @Description  :
#

class TagCloud:

    def __init__(self):
        # 通过在变量名前加上两个`__`, 标明其为私有变量, 但是并不类似于java的private关键字所声明的变量
        # python的私有变量仍然可以在外部访问, 只是比成员变量的访问方式稍微复杂
        # 更多的是一种约定, 告诉其他人, 不要动, 这是私有变量
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, item):
        return self.__tags.get(item.lower(), 0)

    def __setitem__(self, item, value):
        self.__tags[item.lower()] = value

    def __iter__(self):
        return iter(self.__tags)

    def __len__(self):
        return len(self.__tags)

    def __str__(self):
        return self.__tags.__str__()


cloud = TagCloud()
print(cloud["python"])
cloud.add("python")
cloud.add("Python")
print(cloud["python"])
cloud["python"] = 10
print(cloud["python"])
print(len(cloud))
print(cloud)

# 访问私有变量
print(cloud.__dict__)  # 保存了对象的所有成员
# print(cloud._TagCloud__tags)  # 私有变量本质上是在python内部对变量进行了重命名, 换个名字就可以访问了
print(cloud.__dict__["_TagCloud__tags"])
