#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   module_t.py
@Time    :   2019/12/25 21:45:31
@Author  :   guo congcong 
@Version :   1.0
@Contact :   guoliwei1992@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
__author__ = 'guo congcong'

# here put the import lib
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        print('Hello,%s' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
    print(3/2)