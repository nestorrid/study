# -*- coding: UTF-8 -*-
#  
# @FILE        : Tetris/Tetris.py
# @Author      : Nestor
# @Date        : 2023/1/14 23:17      
# @Email       : admin@nestor.me
# 
# @Description : 
#
from core.config import Config
from core.engine import Engine
from core.game_controller import GameController
from utils import print_utils


def main():
    print_utils.print_game_title()
    if not controller.is_player_want_to_start():
        exit()

    engine.run_game_loop()

    engine.print_score()


if __name__ == '__main__':

    config = Config()
    engine = Engine(config.width, config.height)
    controller = GameController()

    main()

    if controller.is_player_want_to_play_again():
        main()
