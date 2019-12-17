#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:  Chenyang Wang
@license: MIT Licence 
@file: Modules.py 
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
import sys


def calculate_result(board):
    ai_score = board.points(False)
    human_score = board.points(True)
    print("AI score: {}".format(ai_score))
    print("Human score: {}".format(human_score))
    if ai_score > human_score:
        print("AI Win!")
    elif ai_score < human_score:
        print('Human Win!')
    else:
        print('Tie!')


def ai_move(board):
    move_flag = True
    while move_flag:
        if board.is_finish():
            calculate_result(board)
            print('Game ended')
            return 0
        try:
            for best in board.find_best():
                pos = best[0]
                print("AI get the best position", pos)
            p = int(pos[0])
            print('AI move in position %2d' %p)
            move_flag = board.move(p-1)
            board.show_board()
        except:
            break
    return board


def human_move(board):
    board = board.Human_board()
    move_flag = True
    while move_flag:
        if board.is_finish():
            calculate_result(board)
            print('Game ended')
            return 0
        pos = input("Human Move(q means exit the game): ").split()
        if not pos:
            continue
        if pos[0] == 'q':
            sys.exit(0)
        try:
            p = int(pos[0])
            move_flag = board.move(p-1)
            board.Human_board().show_board()
        except:
            print('Wrong Move {}, Please Try Again (1-6)'.format(pos[0]))
            continue
    return board.Human_board()
