#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:  Chenyang Wang
@license: MIT Licence 
@file: Board.py 
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


class board_initial:
    """
    This class is using to initiate board.
    board[0] is opponent's store
    board[7] is AI's store
    """
    def __init__(self, exist_board=None):
        if exist_board is None:     # initial the board
            self.board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
            self.reversed = False
        else:       # load the exist board
            self.board = exist_board.board[:]
            self.reversed = exist_board.reversed
        self.hold_score = 7  # judge if pass the opponent's store
        self.end_in_blank_hole = False  # judge if the last stone is stop in blank hole

    def show_board(self):
        """
        Game Board show: P means position
        example for initial board
        ************AI*************
        Pos 6   5   4   3   2   1
        AI: 4 - 4 - 4 - 4 - 4 - 4
         0 ——————— STORE ——————— 0
        H:  4 - 4 - 4 - 4 - 4 - 4
        Pos 1   2   3   4   5   6
        **********Human***********
        """
        print('\n')
        print("************AI*************")
        print("Pos", end="")
        print(*["%2d" % x for x in reversed([1, 2, 3, 4, 5, 6])], sep="  ")      # position from human perspective
        print("AI:", end="")
        print(*["%2d" % x for x in reversed(self.board[1:7])], sep=" -")
        print("%2d ——————— STORE ———————%2d" % (self.points(False), self.points(True)))     # Store
        print("H: ", end="")
        print(*["%2d" % x for x in self.board[8:]], sep=" -")
        print("Pos", end="")
        print(*["%2d" % x for x in [1, 2, 3, 4, 5, 6]], sep="  ")    # position from AI's perspective
        print("**********Human***********")

    def Human_board(self):
        """
        Get human's board, reverse of ai's board
        :return: human's board
        """
        board = board_initial()
        board.board = self.board[7:] + self.board[:7]       # reverse current board for opponent
        board.reversed = not self.reversed      # set the self.reversed as True
        return board

    def is_finish(self):
        """
        Judge if there are no position to move
        :return: True: no position to move;
                 False: there are position can be move
        """
        if any(self.board[1:7]) == 0 or any(self.board[8:]) == 0:
            return True
        else:
            return False

    def points(self, is_human=False):
        """
        Get the total points for every player
        :param is_human: judge get whose points
        :return: points
        """
        if is_human is False:
            if self.is_finish():
                return sum(self.board[1:8])
            else:
                return self.board[7]
        else:
            if self.is_finish():
                return self.board[0] + sum(self.board[8:])
            else:
                return self.board[0]

    def score(self):
        if not self.reversed:
            return self.points(False) - self.points(True)       # Calculate AI score
        else:
            return self.points(True) - self.points(False)       # calculate Human score

    def yield_all_positions(self):
        """
        Get all the position AI can choose
        :return: the yield generator for positions
        """
        for pos, stones in enumerate(self.board[1:7]):
            if stones > 0:
                yield pos

    def move(self, position):
        """
        Get movement for the position you input based on the rule
        :param position: start position
        :return: True or False to judge if finish moving and updating the board
        """
        assert position < 6, "Wrong Position you choose"
        position += 1
        stones = self.board[position]
        assert stones > 0, "Wrong number of stone"
        self.board[position] = 0
        while stones:
            position += 1
            stones -= 1
            if position >= len(self.board):
                position = 1
            self.board[position] += 1
        if position == self.hold_score:
            return True
        if self.board[position] == 1 and 0 < position < 7:
            human_position = len(self.board) - position
            if self.end_in_blank_hole is False or (self.end_in_blank_hole is True and self.board[human_position] != 0):
                self.board[position] = 0
                self.board[self.hold_score] += 1 + self.board[human_position]
                self.board[human_position] = 0
        return False

    def get_moves(self, pos, moves_list, moves):
        """
        get all the positions can be chosen.
        :return: list to show all the moves
        """
        updated_board = board_initial(self)
        move_con = updated_board.move(pos)
        if move_con and list(updated_board.yield_all_positions()):
            for i in updated_board.yield_all_positions():
                updated_board.get_moves(i, moves_list + [pos], moves)
        else:
            moves.append((moves_list + [pos], updated_board))
            return

    def find_all_moves(self):
        """
        Find all the positions that can move in
        :return: list consists of positions
        """
        move = []
        for i in self.yield_all_positions():
            self.get_moves(i, [], move)
        return move

    def minmax(self, depth=5, ai_max=True):
        """
        MiniMax function to calculate move value for every move.
        :param depth: search depth
        :param ai_max: setting for if the regard AI as the max value
        :return: best value for one move
        """
        if depth == 0 or self.is_finish():
            return self.score()
        if ai_max:
            best = -999
            for _, board in self.Human_board().find_all_moves():
                v = board.minmax(depth-1, not ai_max)       # Get value for every move
                b = max(best, v)            # compare with the best value
            return b
        else:
            best = 999
            for _, board in self.Human_board().find_all_moves():
                v = board.minmax(depth-1, not ai_max)       # Get value for every move
                b = min(best, v)        # compare with the best value
            return b

    def compute(self, x):
        """
        calculate the value for every move.
        :param x: all the position can ai move to
        :return: tuple, combination of position with move value.
        example: ([positions], value)
        """
        move_sequence, board = x
        return list(set([x + 1 for x in move_sequence])), board.minmax()

    def find_best(self):
        """
        To find the best move according to the calculate and minmax function
        :return: best move result.
        """
        print("Be patient, AI is thinking")

        def all_moves():
            yield from map(self.compute, list(self.find_all_moves()))

        result = sorted(all_moves(), key=lambda x: x[1], reverse=True)[:1]
        return result