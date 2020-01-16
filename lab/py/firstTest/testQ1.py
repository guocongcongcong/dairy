# 测试关于函数中的break和continue等

# break

# def testBreak():
#     print('这是第一句语句，在句话之后会是break，break后存在另外一个break')
#     break
#     print('这是第二句语句，是在break后的')

# testBreak() # 该语句证明，break不能再循环外面使用，不用更担心break破坏函数的整体性
#   File ".\testQ1.py", line 6
#     break
#     ^
# SyntaxError: 'break' outside loop

# continue
# def testContinue():
#     print('这是第一句语句，在句话之后会是break，break后存在另外一个break')
#     continue
#     print('这是第二句语句，是在break后的')

# testContinue() # 该语句证明，continue不能再循环外面使用，不用更担心break破坏函数的整体性
#   File ".\testQ1.py", line 13
#     continue
#     ^
# SyntaxError: 'continue' not properly in loop

# 运算符
# print('True ^ False:',True ^ False)
# print('True + False:',True + False)
# print('True & False:',True & False)
# print('True and False:',True and False)
# print('True | False:',True | False)
# print('True or False:',True or False)

# for循环

# from collections.abc import Iterable

# # 循环dict
# def testDict():
#     d = {'a': 1, 'b': 2, 'c': 3}
#     for key in d:
#         print(key)
#         print(d[key])

# # 循环list
# def testFor(iters):
#     if(isinstance(iters,Iterable)):
#         for key in iters:
#             print(key)
#     else:
#         print('不是序列')

# # 存在可变参数的循环，可变参数，传入的是一个list，可变的是参数的个数
# def testForAndChange(*iters):
#     if(isinstance(iters,Iterable)):
#         for key in iters:
#             if(isinstance(iters,Iterable)):
#                 for i in key:
#                     print(i)
#             else:
#                 print('key 不是序列')
#     else:
#         print('不是序列')

# # dict.value的迭代
# def testDictValue(d):
#     for v in d.values():
#         print(v)

# # dict.items的迭代
# def testDictItems(d):
#     for k,v in d.items():
#         print('dict的key:%s,dict的value:%s'%(k,v))

# # enumerate的迭代
# def testEnumerate():
#     for i, value in enumerate(['A', 'B', 'C']):
#         print(i, value)

# # 两个变量的迭代
# def testManyItem():
#     for x, y in [(1, 1), (2, 4), (3, 9)]:
#         print(x,y)


# # 变量初始化
# classmates = ['Michael', 'Bob', 'Tracy']
# t = ('a', 'b', ['A', 'B'])
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# s = set([1, 2, 3])
# print(' ////////// before ////////// ')
# print(classmates)
# print(range(0,2))
# print(' ////////// testFor ////////// ')
# testFor(range(0,2))
# testFor(classmates)
# testFor(t)
# testFor(d)
# testFor(s)
# print(' ////////// testForAndChange ////////// ')
# testForAndChange(classmates,range(0,2))
# testDictValue(d)
# testDictItems(d)
# testEnumerate()
# testManyItem()

# # 列表生成式
# import os
# from collections.abc import Iterable
# L= [x * x for x in range(1, 11)]
# L= [x * x for x in range(1, 11) if x % 2 == 0]
# L= [d for d in os.listdir('.')]
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# L = [k + '=' + v for k, v in d.items()]
# L = ['Hello', 'World', 'IBM', 'Apple']
# l = [s.lower() for s in L]
# print(L)
# print(l)

# # 练习
# # 使用内建的isinstance函数可以判断一个变量是不是字符串： isinstance(x, str)
# L = ['Hello', 'World', 18, 'Apple', None]
# l = [s.lower() for s in L if isinstance(s,str)]
# print(l)

# # 生成器
# # 第一种方法:只要把一个列表生成式的[]改成()，就创建了一个generator
# g = (x * x for x in range(10))
# # 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
# # 可以通过next()函数获得generator的下一个返回值。
# # 正确的方法是使用for循环，因为generator也是可迭代对象：
# for n in g:
#     print(n)

# # 斐波拉契数列(Fibonacci):除第一个和第二个数外，任意一个数都可由前两个数相加得到
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# # 第二种方法:要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# g = fib(6)
#  while True:
#      try:
#          x = next(g)
#          print('g:', x)
#      except StopIteration as e:
#          print('Generator return value:', e.value)
#          break

# 练习：杨辉三角(1开始，1结束，对称，相加的后一个数)
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 第一次循环，i = 0，列表长度为1，序号零内的数字为1，
def triangles():
    L = [1]
    while 1:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')