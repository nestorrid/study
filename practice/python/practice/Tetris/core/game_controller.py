# -*- coding: UTF-8 -*-
#  
# @FILE        : Tetris/game_controller.py
# @Author      : Nestor
# @Date        : 2023/1/16 22:57      
# @Email       : admin@nestor.me
# 
# @Description : 
#


class GameController(object):
    _is_game_over = False

    @staticmethod
    def is_player_want_to_start():
        ipt = input("Would you like to play know? (y/n): ")

        if ipt.lower() == "y":
            return True

        return False

    @staticmethod
    def is_player_want_to_play_again():
        ipt = input("Would you like to play again? (y/n): ")

        if ipt.lower() == "y":
            return True

        return False

    def is_game_over(self):
        return self._is_game_over

