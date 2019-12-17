#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:  Chenyang Wang
@license: MIT Licence 
@file: run_game.py 
@time: 2019/12
@contact: wcy1705@outlook.com
@software: PyCharm 
@description:

         ,'~~^- -~~\
        (          ,,)
         \  ''    .|_
         ` C       .-'
          ` ,    _ '
            ,--~,
           /~    \       
          /     . ~/--,  ___No BUG!___
         ,    .__~-_--__[     WCY     |
         |___/ ,/\ /~|_______________|
         \_____-\///~  ||         ||
                 ~~
"""

from Board import board_initial
from Modules import ai_move, human_move


def run(ai_start):
    """
    This is the run function.
    :param ai_start: If True AI first, If False Opponent first
    """
    board = board_initial()
    board.show_board()
    while 1:
        if ai_start:
            board = ai_move(board)
            if board == 0:
                break
            else:
                board = human_move(board)
                if board == 0:
                    break
        else:
            board = human_move(board)
            if board == 0:
                break
            else:
                board = ai_move(board)
                if board == 0:
                    break


if __name__ == '__main__':
    while 1:
        AI_start_flag = input('Do you want to go first?\n0 is first, 1 is second, 2 is exit')
        if AI_start_flag == '0':
            run(False)
            break
        elif AI_start_flag == '1':
            run(True)
            break
        elif AI_start_flag == '2':
            print("Thanks for your trying")
            break
        else:
            print('Wrong Input, please try again.')