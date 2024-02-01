# -*- coding: UTF-8 -*-
#  
# @FILE        : Snake/Snake.py
# @Author      : Nestor
# @Date        : 2023/1/12 23:36      
# @Email       : admin@nestor.me
# 
# @Description : 
#
import os
import platform
import random
import threading
import time
from collections import namedtuple
from enum import Enum

from pynput import keyboard

Point = namedtuple('Point', ('x', 'y'))


class MoveDirection(Enum):
    undefined = -1
    left = keyboard.Key.left
    right = keyboard.Key.right
    up = keyboard.Key.up
    down = keyboard.Key.down


class CellType(Enum):
    empty = 1
    snake = 1 << 1
    food = 1 << 2
    block = 1 << 3


g_gameCount = 0
g_isGameOver = False
g_highestScore = 0

g_gameMap = []
g_snake = []
g_snakeHead = Point(0, 0)
g_snakeTail = Point(0, 0)

g_mapWidth = 30
g_mapHeight = 20

g_currentSpeed = 0.6

g_moveDirection = MoveDirection.right


def is_escape_pressed(key):
    return key == keyboard.Key.esc


def is_direction_key_pressed(key):
    return key == keyboard.Key.left or key == keyboard.Key.right or key == keyboard.Key.up or key == keyboard.Key.down


def on_key_release(key):
    if is_escape_pressed(key):
        return False

    if is_direction_key_pressed(key):
        global g_moveDirection
        g_moveDirection = MoveDirection(key)


def start_keyboard_listener():
    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()


def init_map():
    for i in range(g_mapHeight):
        g_gameMap.append([CellType.empty] * g_mapWidth)


def is_game_over(point):
    global g_isGameOver

    if is_out_of_map(point) or is_snake_self_tile(point):
        g_isGameOver = True
        return True

    return False


def is_out_of_map(point):
    row = point.y
    position = point.x

    if row < 0 or row > len(g_gameMap) - 1:
        return True

    if position < 0 or position > len(g_gameMap[0]) - 1:
        return True

    return False


def is_snake_self_tile(point):
    return g_gameMap[point.y][point.x] == CellType.snake


def pick_up_food(point):
    if g_gameMap[point.y][point.x] == CellType.food:
        g_gameMap[point.y][point.x] = CellType.snake
        init_food()
        return True

    return False


def put_snake_into_empty_tile(point):
    row = point.y
    position = point.x

    if g_gameMap[row][position] == CellType.empty:
        g_gameMap[row][position] = CellType.snake


def init_snake():
    global g_snakeTail, g_snakeHead

    for i in range(4):
        p = Point(i, 0)
        g_snake.append(p)
        put_snake_into_empty_tile(p)


def init_food():
    if g_gameMap[random.randrange(1, g_mapHeight)][random.randrange(g_mapWidth)] == CellType.empty:
        g_gameMap[random.randrange(1, g_mapHeight)][random.randrange(g_mapWidth)] = CellType.food
        return

    init_food()


def init_game():
    global g_gameCount
    g_gameCount += 1
    init_map()
    init_snake()
    init_food()

    t_listener = threading.Thread(target=start_keyboard_listener)
    t_listener.start()


def will_exit_game():
    if g_gameCount == 0:
        return False

    ipt = input("Would you like to play again? (y/n): ")

    return ipt.lower() != "y"


def clear_screen():
    userSystem = platform.platform().split("-")[0]
    if userSystem == "macOS":
        os.system("clear")
    else:
        os.system("cls")


def draw_border():
    print("-" * (g_mapWidth + 4))


def get_cell_characters(cell):
    if cell == CellType.empty:
        return " "
    elif cell == CellType.snake:
        return "*"
    elif cell == CellType.food:
        return "o"
    else:
        return "x"


def draw_game_data():
    for line in g_gameMap:
        lineString = " |"
        for cell in line:
            lineString += get_cell_characters(cell)
        lineString += "|"

        print(lineString)


def draw_frame():
    clear_screen()
    draw_border()
    draw_game_data()
    draw_border()


def print_game_score():
    pass


def end_game():
    print_game_score()


def remove_snake_tile_from_map(point):
    row = point.y
    position = point.x
    g_gameMap[row][position] = CellType.empty


def get_new_snake_head():
    head = g_snake[-1:][0]

    if g_moveDirection == MoveDirection.right:
        return Point(head.x + 1, head.y)

    if g_moveDirection == MoveDirection.left:
        return Point(head.x - 1, head.y)

    if g_moveDirection == MoveDirection.up:
        return Point(head.x, head.y - 1)

    if g_moveDirection == MoveDirection.down:
        return Point(head.x, head.y + 1)


def move_snake_tail_to_head():
    newHead = get_new_snake_head()

    if is_game_over(newHead):
        return

    g_snake.append(newHead)

    if not pick_up_food(newHead):
        tail = g_snake.pop(0)
        remove_snake_tile_from_map(tail)
        put_snake_into_empty_tile(newHead)


def move_snake():
    global g_currentSpeed

    move_snake_tail_to_head()
    time.sleep(g_currentSpeed)

    if g_currentSpeed > 0.3:
        g_currentSpeed -= 0.05


def main():
    while not will_exit_game():
        init_game()
        while not g_isGameOver:
            draw_frame()
            move_snake()

        end_game()


if __name__ == '__main__':
    main()
