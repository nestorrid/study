# -*- coding: UTF-8 -*-
#  
# @FILE        : Minesweeper/Minesweepr.py
# @Author      : Nestor
# @Date        : 2023/1/11 23:55      
# @Email       : admin@nestor.me
# 
# @Description : 
#
import os
from random import randrange

configs = {
    "1": (9, 9, 10),
    "2": (16, 16, 40),
    "3": (16, 30, 99)
}

game_config = ()
mine_remaining = 0
game_count = 0

game_map = []
player_map = []
is_game_over = False
is_player_wins = False


def set_game_level():
    global game_config
    print("Please chose a game level(1~3), or 4 for help:")
    print("> 1. Beginner | 2. Advanced | 3. Experts")
    print("> 4. Help")

    while len(game_config) == 0:
        ipt = input(">> ")
        if len(ipt) == 1 and ipt in "1234":
            game_config = configs[ipt]
        else:
            print("> Input a number between 1 to 4, please try again.")


def init_game():
    global mine_remaining, game_count, is_game_over

    rowCount = game_config[0] + 2
    rowLength = game_config[1] + 2
    mines = game_config[2]

    mine_remaining = game_config[2]
    game_count += 1
    is_game_over = False

    game_map.clear()
    player_map.clear()

    for i in range(0, rowCount):
        game_map.append([0] * rowLength)
        player_map.append([-1] * rowLength)

    while mines > 0:
        idx, row = randrange(1, rowLength - 1), randrange(1, rowCount - 1)
        if game_map[row][idx] == 0:
            game_map[row][idx] = 1
            mines -= 1


def clear_screen():
    os.system("cls")
    os.system("clear")


def print_game_title():
    title = get_column_title()
    print(title)
    print("-" * (len(title) + 3))


def print_game_footer():
    title = get_column_title()
    print("-" * (len(title) + 3))
    print(title)


def get_column_title():
    title = "    |"
    for i in range(1, len(game_map[0]) - 1):
        title += f"%3d" % i

    title += " |"

    return title


def draw_game_rows(drawMap):
    for i in range(1, len(drawMap) - 1):
        row = drawMap[i]
        rowString = f"%3d |" % i
        for j in range(1, len(row) - 1):
            rowString += format_to_three_char(row[j])

        rowString += f" |%2d" % i
        print(rowString)


def draw_map():
    clear_screen()
    print_game_title()
    draw_game_rows(player_map)
    print_game_footer()
    print_game_progress()


def show_mine_map():
    clear_screen()
    print_game_title()
    draw_game_rows(game_map)
    print_game_footer()


def format_to_three_char(num):
    if num == -1:
        return "  *"

    if num == -2:
        return "  -"

    if num == 0:
        return "   "

    if num == 1 and is_game_over and not is_player_wins:
        return "  x"

    return f"%3d" % num


def is_tile_opened(index, row):
    return player_map[row][index] > -1


def is_tile_original(index, row):
    return player_map[row][index] == -1


def is_tile_marked(index, row):
    return player_map[row][index] == -2


def is_no_mine_nearby(index, row):
    return player_map[row][index] == 0


def is_tile_has_mine(index, row):
    if is_map_boundary(index, row):
        return 0

    return game_map[row][index]


def is_map_boundary(index, row):
    if index == 0 or index == len(game_map[0]) - 1:
        return True

    if row == 0 or row == len(game_map) - 1:
        return True

    return False


def get_mine_count(index, row):
    count = 0

    count += is_tile_has_mine(index - 1, row - 1)
    count += is_tile_has_mine(index - 1, row + 1)
    count += is_tile_has_mine(index + 1, row + 1)
    count += is_tile_has_mine(index + 1, row - 1)
    count += is_tile_has_mine(index, row - 1)
    count += is_tile_has_mine(index, row + 1)
    count += is_tile_has_mine(index + 1, row)
    count += is_tile_has_mine(index - 1, row)

    return count


def open_tiles_nearby(index, row):
    open_tile(index - 1, row - 1)
    open_tile(index - 1, row + 1)
    open_tile(index + 1, row + 1)
    open_tile(index + 1, row - 1)
    open_tile(index, row - 1)
    open_tile(index, row + 1)
    open_tile(index + 1, row)
    open_tile(index - 1, row)


def open_tile(index, row):
    if is_map_boundary(index, row):
        return

    if is_tile_opened(index, row) or is_tile_marked(index, row):
        return

    if is_tile_original(index, row):
        player_map[row][index] = get_mine_count(index, row)

        if is_no_mine_nearby(index, row):
            open_tiles_nearby(index, row)


def update_player_map(index, row, cmd):
    global mine_remaining

    if cmd == 1:
        player_map[row][index] = -2
        mine_remaining -= 1

    if cmd == 2:
        player_map[row][index] = -1
        mine_remaining += 1

    if cmd == 0:
        open_tile(index, row)


def is_mine_tile_opened(index, row, cmd):
    return game_map[row][index] == 1 and cmd == 0 and player_map[row][index] == -1


def get_correct_mark():
    count = 0

    for row in range(len(game_map)):
        for idx in range(len(game_map[row])):
            if game_map[row][idx] == 1 and player_map[row][idx] == -2:
                count += 1

    return count


def is_player_win():
    correctMark = get_correct_mark()
    if correctMark == game_config[2]:
        return True

    return False


def exec_game_command(index=0, row=0, cmd=0):
    global is_game_over, is_player_wins

    if index == 0 and row == 0:
        return

    if is_mine_tile_opened(index, row, cmd):
        is_game_over = True
        is_player_wins = False

    update_player_map(index, row, cmd)

    if is_player_win():
        is_game_over = True
        is_player_wins = True


def check_game_command(location):
    t = location.split(" ")
    if len(t) < 2 or len(t) > 3:
        return False

    for i in t:
        if not i.isdigit():
            return False

    x = int(t[0])
    y = int(t[1])
    cmd = 0

    if len(t) == 3:
        cmd = int(t[2])

    if x > len(game_map[0]) - 1 or x < 1:
        return False

    if y > len(game_map) - 1 or y < 1:
        return False

    if cmd < 0 or cmd > 2:
        return False

    return True


def get_game_command(locationString):
    t = locationString.split(" ")
    c = [int(x) for x in t]

    if len(c) == 2:
        c.append(0)

    return tuple(c)


def input_game_command():
    # print("Input a location like `3 5` to sweep the tile, plus `1` to mark as mine, like `4 8 1`:")
    idx, row, mark = 0, 0, 0

    while idx == 0 and row == 0:
        locationString = input(">> ")
        if check_game_command(locationString):
            idx, row, mark = get_game_command(locationString)
        else:
            print("Please input a right location.")

    return idx, row, mark


def exit_game():
    if game_count == 0:
        return False

    restart = input(f"Would you like to play again?(y/n): ")
    if restart == "y":
        return False

    return True


def print_game_progress():
    print(f"> Marked mine: %d, remaining: %d." % (game_config[2] - mine_remaining, mine_remaining))


def print_winning_message():
    print("Congratulations! You won!")


def print_lost_message():
    print("Game over, you lost.")


def main():
    while not exit_game():
        set_game_level()
        init_game()

        x, y, cmd = 0, 0, 0

        while not is_game_over:
            draw_map()
            x, y, cmd = input_game_command()
            exec_game_command(x, y, cmd)

        if is_player_wins:
            draw_map()
            print_winning_message()
        else:
            show_mine_map()
            print_lost_message()


if __name__ == '__main__':
    main()
