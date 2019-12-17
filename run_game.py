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
from Modules import ai_move, Human_move, calculate_result


def run(ai_start=True):
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
                print("Finally!, AI score is: ")
                break
            else:
                board = Human_move(board)
        else:
            board = Human_move(board)
            if board == 0:
                print("Finally!")
                break
            else:
                board = ai_move(board)


if __name__ == '__main__':
    while 1:
        AI_start_flag = int(input('Do you want to go first?\n 0 is first, 1 is second, 2 is exit'))
        if AI_start_flag == 0:
            run(False)
            break
        elif AI_start_flag == 1:
            run(True)
            break
        elif AI_start_flag == 2:
            print("Thanks for your trying")
            break
        else:
            print('Wrong Input, please try again.')