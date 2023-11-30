# -*- coding: UTF-8 -*-
#  
# @FILE        : Tetris/print_utils.py
# @Author      : Nestor
# @Date        : 2023/1/16 22:47      
# @Email       : admin@nestor.me
# 
# @Description : 
#

import os
import platform

from core.types import CellType


def print_cell_character(cellType):
    if cellType == CellType.empty:
        return "  "

    if cellType == CellType.block:
        return " *"

    return ""


def clear_screen():
    p = platform.system()
    if p == "macOS" or p == "Darwin":
        os.system("clear")
    else:
        os.system("cls")


def get_line_prefix():
    return " " * 10


def print_separate_line(charCount, sep="-", prefix=get_line_prefix()):
    print(prefix + sep * (charCount * 2 + 2))


def print_game_title():
    print("Welcome to Nestor's Tetris.")
    print("Press `left` or `right` to move the block.")
    print("Press `up` to rotate the block.")
    print("Press `down` to drop the block instantly.")
