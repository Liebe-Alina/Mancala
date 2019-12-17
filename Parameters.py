#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:  Chenyang WANG
@license: MIT Licence 
@file: Parameters.py 
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

import argparse


class parameters:
    parser = argparse.ArgumentParser(description='AI Calculation')
    parser.add_argument('--board', default=None, help='Initial board')
    parser.add_argument('--depth', default=5, help='Search depth')
    parser.add_argument('--second_move', default=False, help='AI move secondly')
    parser.add_argument('--score', default=False)