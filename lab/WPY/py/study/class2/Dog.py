#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Dog.py
@Time    :   2019/12/29 15:19:58
@Author  :   guo congcong 
@Version :   1.0
@Contact :   guoliwei1992@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
__author__ = 'guo congcong'

# here put the import lib
from Animal import Animal

class Dog(Animal):
    def run(self):
        print('dog is running')

dog = Dog()
dog.run()