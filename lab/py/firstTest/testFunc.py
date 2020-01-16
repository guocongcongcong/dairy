def sayHello():
    print('hello world')

# sayHello()

# 默认参数 : 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 该函数用来计算x的n次方，默认是x的2次方
def defaultParameter(x,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s

# x = input("请输入一个参数x:")
# print(defaultParameter(int(x)))

# x1 = input("请输入参数x1:")
# n1 = input("请输入参数n1:")
# print(defaultParameter(int(x1),int(n1)))

# 可变参数 : 参数个数可变 -- 在函数内部，参数numbers接收到的是一个tuple
def variableParameter(*numbers):
    sum = 0
    for n in numbers:
        sum  = sum + n * n
    return sum

# # 正常调用，数组的请款，不适用可变参数的情况下：
# # print(variableParameter([1,2,3]))
# # 利用可变参数 简化为
# print(variableParameter(1,2,3))
# print(variableParameter())
# # Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
# num = [1,2,3]
# print(variableParameter(*num))

# 关键字参数:关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def keywordParameter(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# keywordParameter('gul',27)
# keywordParameter('Bob', 35, city='Beijing')
# # 关键字参数的简化输入： **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# keywordParameter('Jack', 24, **extra)

# 小昕的练习题
# townee = [
#     {'海底王国':['小美人鱼''海之王''小美人鱼的祖母''五位姐姐'],'上层世界':['王子','邻国公主']},
#     '丑小鸭','坚定的锡兵','睡美人','青蛙王子',
#     [{'主角':'小红帽','配角1':'外婆','配角2':'猎人'},{'反面角色':'狼'}]
#     ]
# print(len(townee))
# print(townee[5])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
# townee[5][1]['反面角色']='读者'
# print(townee[-1][-1].get('反面角色'))
# townee.insert(4,'第三者')
# print(townee)

# import os
# for x in [d for d in os.listdir('.')]:
#     print(x)




L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [d.lower() for d in L1 if isinstance(d,str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# num1 = 24
# while True:
#     for i in range(3):
#         x = int(input("请输入一个数字:"))
#         if x == num1:
#             print('你答对了')
#             break
#         elif x>num1 :
#             print('太大了')
#         else:
#             print('太小了')
#     else:
#         print('你失败了')
#         break

# a = input('请随便输入')
# print(type(a))


a=int(input('A你认罪call：1 或不认罪call 2 ：'))
b=int(input('B你认罪call：1 或不认罪call 2 ：'))
if (a ==1 and b==1):
    print('各判十年')
elif (a ==2 and b==2):
    print('各判三年')
elif (a ==1 and b==2):
    print('a 认罪1年，b 20年')
else :
    print('a 20年，b 一年')


# while True:
#     a=input('A你认罪或不认罪')
#     b=input('B你认罪或不认罪')
#     if a=input('认罪')and b=input('不认罪'):
#      print('各判十年')
#         break
#     #避免死循环
#     elif a and b=input('不认罪'):
#         print('各判三年')
#     if a =input('认罪')and b=input('不认罪')
#         print('认罪1年，抵赖20年')
#     elif a =input('不认罪') and b=input('认罪')
#         print('认罪1年，抵赖20年')


