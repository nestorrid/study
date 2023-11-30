# -*- coding: UTF-8 -*-
#  
# @FILE        : Tetris/types.py
# @Author      : Nestor
# @Date        : 2023/1/16 22:45      
# @Email       : admin@nestor.me
# 
# @Description : 
#

from collections import namedtuple
from enum import Enum

Point = namedtuple("Point", ["x", "y"])
KeyCallback = namedtuple("KeyCallback", ["key", "callback"])


class CellType(Enum):
    empty = 0
    block = 1
