#!/usr/bin/env python3
## -*- encoding: utf-8 -*-
'''
@File    :   readFile.py
@Time    :   2020/01/07 20:39:48
@Author  :   guo congcong 
@Version :   1.0
@Contact :   guoliwei1992@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''
__author__ = 'guo congcong'

# here put the import lib
import os
# import pymysql as mysqlDB
# path = "/Users/glw/图书/" #文件夹目录
# files= os.listdir(path) #得到文件夹下的所有文件名称
# s = []
# for file in files: #遍历文件夹
#      if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
#           f = open(path+"/"+file,'rb'); #打开文件
#           iter_f = iter(f); #创建迭代器
#           str1 = ""
#           for line in iter_f: #遍历文件，一行行遍历，读取文本
#               str1 = str1 + str(line,encoding="utf-8")
#           s.append(str1) #每个文件的文本存到list中
# print(s) #打印结果
# filePath = 'G://paperInformation//books//Detail//'
# filePath = '/Users/glw/图书/'
filePath = 'E://books'
filename = './bookIndex2.sql'
sql =''
for i,j,k in os.walk(filePath):
    # # print(i,j,k)
    # print(i)
    for o in k:
        sql += "INSERT INTO bookIndex (filePath,fileName) VALUES ('%s','%s');\n" %(i,o)
        # print(sql)
        print(i+'/'+o)
        f = open(filename,'w',encoding="utf-8")
        # sql += "INSERT INTO bookIndex VALUES ('%s','%s');\n" %(i,o)
        # print(sql)
        # print(i)
        # print(o)
# f = open(filename,'w')
f.writelines(sql)
f.close