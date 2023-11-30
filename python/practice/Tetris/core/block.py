# -*- coding: UTF-8 -*-
#  
# @FILE        : Tetris/block.py
# @Author      : Nestor
# @Date        : 2023/1/16 23:19      
# @Email       : admin@nestor.me
# 
# @Description : 
#
import random
from abc import ABCMeta, abstractmethod

import utils.print_utils
from core.config import Config
from core.types import CellType, Point


class BaseBlock(object, metaclass=ABCMeta):

    def __init__(self, block_size, start_x=0, config=Config()):
        self.blockSize = block_size
        self.x = start_x if start_x != 0 else random.randrange(config.width - self.blockSize)
        self.y = 0
        self.config = config
        self._block = []

        for i in range(self.blockSize):
            self._block.append([CellType.empty] * self.blockSize)

        self._init_block()

    @abstractmethod
    def _init_block(self):
        pass

    def get_line_string(self, line):
        line_string = ""
        if 0 <= line < self.blockSize:
            for i in range(self.blockSize):
                line_string += utils.print_utils.print_cell_character(self._block[line][i])

        return line_string

    # @abstractmethod
    def get_block_dots_location_list(self):
        location_list = []
        for y in range(self.blockSize):
            for x in range(self.blockSize):
                if self._block[y][x] == CellType.block:
                    location_list.append(Point(self.x + x, self.y + y))

        return location_list

    def get_block_edge_location_list(self):
        edge_list = []
        for x in range(self.blockSize):
            is_edge_for_x_found = False

            for y in range(self.blockSize - 1, -1, -1):
                if self._block[y][x] == CellType.block:
                    edge_list.append(Point(self.x + x, self.y + y))
                    is_edge_for_x_found = True
                    break

            if is_edge_for_x_found:
                continue

        return edge_list

    # @abstractmethod
    def rotate_block(self):
        new_block = []
        for i in range(self.blockSize):
            new_block.append([CellType.empty] * self.blockSize)

        for x in range(self.blockSize):
            for y in range(self.blockSize):
                new_block[self.blockSize - 1 - y][x] = self._block[x][y]

        def remove_top_empty_lines(target_list):
            if target_list[0].count(CellType.block) == 0:
                empty_line = target_list.pop(0)
                target_list.append(empty_line)
                remove_top_empty_lines(target_list)
            return

        remove_top_empty_lines(new_block)

        self._block = new_block

    # @abstractmethod
    def move_left_by_one_step(self):
        self.x = 0 if self.x == 1 else self.x - 1

    # @abstractmethod
    def move_right_by_one_step(self):
        self.x = self.config.width if self.x == self.config.width - 1 else self.x + 1

    def move_down_by_one_step(self):
        self.y += 1

    def print_block(self):
        for line in self._block:
            line_string = ""
            for cell in line:
                line_string += utils.print_utils.print_cell_character(cell)

            print(line_string)


class BlockL(BaseBlock):

    def __init__(self, block_size=3):
        super().__init__(block_size=block_size)

    def _init_block(self):
        for line in self._block:
            line[0] = CellType.block

        self._block[2][1] = CellType.block


class BlockZ(BaseBlock):
    def __init__(self, block_size=3):
        super().__init__(block_size)

    def _init_block(self):
        self._block[0][0] = CellType.block
        self._block[0][1] = CellType.block
        self._block[1][1] = CellType.block
        self._block[1][2] = CellType.block


class BlockI(BaseBlock):

    def __init__(self, block_size=4):
        super().__init__(block_size)

    def _init_block(self):
        for line in self._block:
            line[0] = CellType.block


class BlockDot(BaseBlock):
    def __init__(self, block_size=2):
        super().__init__(block_size)

    def _init_block(self):
        self._block[0][0] = CellType.block
        self._block[0][1] = CellType.block
        self._block[1][0] = CellType.block
        self._block[1][1] = CellType.block


class BlockT(BaseBlock):
    def __init__(self, block_size=3):
        super().__init__(block_size)

    def _init_block(self):
        self._block[0][0] = CellType.block
        self._block[0][1] = CellType.block
        self._block[0][2] = CellType.block
        self._block[1][1] = CellType.block


if __name__ == '__main__':
    block = BlockZ()
    block.print_block()
    print(block.get_block_dots_location_list())
