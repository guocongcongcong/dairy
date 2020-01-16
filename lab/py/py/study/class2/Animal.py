#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Animal.py
@Time    :   2019/12/29 15:17:25
@Author  :   guo congcong 
@Version :   1.0
@Contact :   guoliwei1992@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
__author__ = 'guo congcong'

# here put the import lib
class Animal(object):
    def run(self):
        print('Animal is running')


class Cat(Animal):
    def run(self):
        print('cat is running')
cat=Cat()
cat.run()