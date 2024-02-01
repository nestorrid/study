# -*- coding: UTF-8 -*-
#  
# @FILE        : Tetris/gameMap.py
# @Author      : Nestor
# @Date        : 2023/1/16 22:27      
# @Email       : admin@nestor.me
# 
# @Description : 
#
import time

from core.block import *
from core.keyboard_listener import *
from utils.print_utils import get_line_prefix, print_cell_character, print_separate_line, clear_screen


def print_game_info_title(index):
    if index != 3:
        return ""

    return "NESTOR'S TETRIS"


def print_game_info_next_title(index):
    if index != 5:
        return ""

    return "Next block:"


def print_game_info_next_block(index, nextBlock: BaseBlock):
    if index < 7 or index > 7 + nextBlock.blockSize - 1:
        return ""

    return nextBlock.get_line_string(index - 7)


def print_game_info_score_title(index):
    if index != 15:
        return ""

    return "Score:"


def print_game_info_score(index, score):
    if index != 16:
        return ""

    return f"%d" % score


def print_game_info_record_title(index):
    if index != 18:
        return ""

    return "Record:"


def print_game_info_record(index, record):
    if index != 19:
        return ""

    return f"%d" % record


class Engine(object):
    _map = []
    _next_block = None
    _score = 0
    _record = 0
    _current_block = None
    _game_speed = 1
    _is_game_over = False
    _keyboard_listener = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
        for i in range(self.height):
            self._map.append([CellType.empty] * self.width)

    @property
    def next_block(self):
        if self._next_block is None:
            self._next_block = create_block()
        return self._next_block

    @property
    def keyboard_listener(self):
        if self._keyboard_listener is None:
            callbacks = [
                LeftKeyCallback(self._move_current_block_left_by_one_step),
                RightKeyCallback(self._move_current_block_right_by_one_step),
                UpKeyCallback(self._rotate_current_block),
                DownKeyCallback(self._move_current_block_to_bottom)
            ]

            self._keyboard_listener = KeyboardListener(callbacks)

        return self._keyboard_listener

    def _draw_frame(self):
        clear_screen()
        print_separate_line(self.width)
        self._draw_game_lines()
        print_separate_line(self.width)

    def _draw_game_lines(self):
        for line_index, line in enumerate(self._map):
            lineString = get_line_prefix() + "|"
            for cell in line:
                lineString += print_cell_character(cell)

            lineString += "|"
            lineString += self._draw_game_info(line_index)

            print(lineString)

    def _draw_game_info(self, index):
        infoString = " " * 8
        infoString += print_game_info_title(index)
        infoString += print_game_info_next_title(index)
        infoString += print_game_info_next_block(index, self.next_block)
        infoString += print_game_info_score_title(index)
        infoString += print_game_info_score(index, self._score)
        infoString += print_game_info_record_title(index)
        infoString += print_game_info_record(index, self._record)

        return infoString

    def run_game_loop(self):

        self._start_key_listener()

        while self._is_game_running():
            self._update_frame()
            self._wait_for_next_move()

    def print_score(self):
        pass

    def _fetch_next_block(self):
        next_block = self.next_block
        self._next_block = None
        return next_block

    def _add_new_block_to_game(self):
        self._current_block = self._fetch_next_block()

        block_locations = self._current_block.get_block_dots_location_list()

        if self._check_game_over(block_locations):
            self._is_game_over = True

        self._change_location_type(block_locations, CellType.block)

    def _move_current_block_down(self):

        self._clear_current_block()
        self._current_block.move_down_by_one_step()
        self._redraw_current_block()

    def _check_game_over(self, locations):
        for point in locations:
            if self._map[point.y][point.x] == CellType.block:
                return True

        return False

    def _change_location_type(self, locations, cell_type):
        for point in locations:
            self._map[point.y][point.x] = cell_type

    def _is_current_block_can_move_down(self):
        locations = self._current_block.get_block_edge_location_list()

        for point in locations:
            if point.y + 1 > self.height - 1:
                return False

            if self._map[point.y + 1][point.x] == CellType.block:
                return False

        return True

    def _remove_lines_with_full_blocks(self):
        full_block_lines = []
        for i in range(self.height):
            line = self._map[i]
            if line.count(CellType.block) == self.width:
                full_block_lines.append(i)

        for i in full_block_lines:
            self._map.pop(i)
            self._map.insert(0, [CellType.empty] * self.width)

        self._calculate_score(len(full_block_lines))

    def _calculate_score(self, line_count):
        self._score += line_count ** 2 * 10
        if self._score > self._record:
            self._record = self._score

    def _is_game_running(self):
        return not self._is_game_over

    def _wait_for_next_move(self):
        time.sleep(self._game_speed)

    def _reset_current_block(self):
        self._current_block = None

    def _move_current_block_left_by_one_step(self):
        self._move_and_redraw(self._current_block.move_left_by_one_step)

    def _move_current_block_right_by_one_step(self):
        self._move_and_redraw(self._current_block.move_right_by_one_step)

    def _rotate_current_block(self):
        self._move_and_redraw(self._current_block.rotate_block)

    def _move_current_block_to_bottom(self):
        while self._is_current_block_can_move_down():
            self._move_current_block_down()

        self._remove_lines_with_full_blocks()
        self._reset_current_block()
        self._update_frame()

    def _start_key_listener(self):
        self.keyboard_listener.start()

    def _clear_current_block(self):
        current_locations = self._current_block.get_block_dots_location_list()
        self._change_location_type(current_locations, CellType.empty)

    def _redraw_current_block(self):
        new_locations = self._current_block.get_block_dots_location_list()
        self._change_location_type(new_locations, CellType.block)

    def _move_and_redraw(self, func):
        self._clear_current_block()
        func()
        self._redraw_current_block()
        self._draw_frame()

    def _update_frame(self):
        if self._current_block is None:
            self._add_new_block_to_game()

        self._draw_frame()

        if self._is_current_block_can_move_down():
            # print("can move down")
            self._move_current_block_down()
        else:
            # print("can not move down")
            self._remove_lines_with_full_blocks()
            self._reset_current_block()


def create_block():
    blocks = [BlockT, BlockZ, BlockI, BlockL, BlockDot]
    return random.choice(blocks)()
