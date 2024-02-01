# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : abstract_class.py
# @Date         : 2023/11/5 17:10
#
# @Description  :
#

from abc import ABC, abstractmethod


class Stream(ABC):

    @abstractmethod
    def read(self):
        pass


class MemoryStream(Stream):

    def read(self):
        print("read from memory.")


# TypeError: Can't instantiate abstract class Stream with abstract method read
# s = Stream()

ms = MemoryStream()
ms.read()
