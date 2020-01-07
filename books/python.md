<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

#python复习

<!-- TOC depthFrom:2 depthTo:3 -->

- [快速查询](#快速查询)
    - [错误列表](#错误列表)
    - [函数列表](#函数列表)
- [基础类型和变量](#基础类型和变量)
    - [小结](#小结)
- [字符串和编码](#字符串和编码)
    - [Python的字符串](#python的字符串)
    - [格式化](#格式化)
- [list 和 tuple](#list-和-tuple)
    - [list](#list)
    - [tuple](#tuple)
- [条件判断](#条件判断)
- [循环](#循环)
    - [循环](#循环-1)
    - [小结](#小结-1)
- [dict 和 set](#dict-和-set)
    - [dict](#dict)
    - [set](#set)
- [函数](#函数)
    - [调用函数](#调用函数)
    - [定义函数-def my_abs(x):](#定义函数-def-my_absx)
    - [空函数-pass](#空函数-pass)
    - [返回多个值-return nx, ny](#返回多个值-return-nx-ny)
    - [函数的参数](#函数的参数)
    - [可变参数-def calc(*numbers):](#可变参数-def-calcnumbers)
    - [关键字参数-def person(name, age, **kw):](#关键字参数-def-personname-age-kw)
    - [命名关键字参数-def person(name, age, *, city, job):](#命名关键字参数-def-personname-age--city-job)
    - [参数组合](#参数组合)
    - [小结](#小结-2)
- [递归函数](#递归函数)
- [高级特性](#高级特性)
    - [切片](#切片)
    - [迭代](#迭代)
    - [列表生成式](#列表生成式)
    - [生成器](#生成器)

<!-- /TOC -->

## 快速查询

```py
# -*- coding: utf-8 -*-
name = input('please enter your name: ')
print('hello,', name)
```

### 错误列表

- IndexError:当索引超出了范围时，Python会报一个IndexError错误;
- TypeError:调用函数的时候，如果传入的参数数量不对，会报TypeError的错误;
- 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError;

### 函数列表

[函数列表:](https://docs.python.org/3/library/functions.html#max)

|               |             | Built-in Functions |              |                |
| ------------- | ----------- | ------------------ | ------------ | -------------- |
| abs()         | delattr()   | hash()             | memoryview() | set()          |
| all()         | dict()      | help()             | min()        | setattr()      |
| any()         | dir()       | hex()              | next()       | slice()        |
| ascii()       | divmod()    | id()               | object()     | sorted()       |
| bin()         | enumerate() | input()            | oct()        | staticmethod() |
| bool()        | eval()      | int()              | open()       | str()          |
| breakpoint()  | exec()      | isinstance()       | ord()        | sum()          |
| bytearray()   | filter()    | issubclass()       | pow()        | super()        |
| bytes()       | float()     | iter()             | print()      | tuple()        |
| callable()    | format()    | len()              | property()   | type()         |
| chr()         | frozenset() | list()             | range()      | vars()         |
| classmethod() | getattr()   | locals()           | repr()       | zip()          |
| compile()     | globals()   | map()              | reversed()   | \__import__()   |
| complex()     | hasattr()   | max()              | round()      |

## 基础类型和变量

>  * Python程序是大小写敏感的，如果写错了大小写，程序会报错。
>  * 以#开头的语句是注释，注释是给人看的,解释器会忽略掉注释。
>  * 每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块。
>  * 按照约定俗成的管理，应该始终坚持使用4个空格的缩进。

1. 整数

* 在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0
* 有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2

2. 浮点数

* 浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。
* 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差
* 浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5

3. 字符串


* 字符串是以单引号'或双引号"括起来的任意文本
* 如果'本身也是一个字符，那就可以用""括起来
* 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识:```'I\'m \"OK\"!'```
* 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
* Python还允许用r''表示''内部的字符串默认不转义:```print(r'\\\t\\')->\\\t\\```
* Python允许用'''...'''的格式表示多行内容

| 字符 | 备注 |
| ---- | ---- |
| \n   | 换行 |
| \t   | 制表 |
| \\   | \    |

4. 布尔值

* 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False。
* 在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来。
* 布尔值可以用and、or和not运算。
  * not运算是非运算，它是一个单目运算符，把True变成False，False变成True。

5. 空值

* 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。


6. 变量

* 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
* 在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量

```py
# -*- coding: utf-8 -*-
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
```
>这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言

```py
# -*- coding: utf-8 -*-
a = 'ABC'
```
>Python解释器干了两件事情：在内存中创建了一个'ABC'的字符串；在内存中创建了一个名为a的变量，并把它指向'ABC'。
>也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据
```py
# -*- coding: utf-8 -*-
a = 'ABC'
b = a
a = 'XYZ'
print(b)
```
>执行a = 'ABC'，解释器创建了字符串'ABC'和变量a，并把a指向'ABC';
>执行b = a，解释器创建了变量b，并把b指向a指向的字符串'ABC';
>执行a = 'XYZ'，解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改;
>所以，最后打印变量b的结果自然是'ABC'了。


7. 常量

* 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量:```PI = 3.14159265359```
* 

8. python的除法为什么精确

* 在Python中，有两种除法，一种除法是/：```>>> 10 / 3 -> 3.3333333333333335```
* /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：```>>> 9 / 3 -> 3.0```
* 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：```>>> 10 // 3 -> 3```
* Python还提供一个余数运算，可以得到两个整数相除的余数:```>>> 10 % 3 -> 1```
* 无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的。


### 小结

* Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
* 对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。
* Python的整数没有大小限制。
* Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

## 字符串和编码

* Unicode把所有语言都统一到一套编码里
* ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节 
* 很多网页的源码上会有类似```<meta charset="UTF-8" />```的信息，表示该网页正是用的UTF-8编码。
* input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情;

### Python的字符串

* Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符;
* Python对bytes类型的数据用带b前缀的单引号或双引号表示: ```x = b'ABC```
* Unicode表示的str通过encode()方法可以编码为指定的bytes:```'ABC'.encode('ascii')  ```(utf-8)
* 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes:```b'ABC'.decode('ascii')```
* 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节:``` b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')```
* len():```len('ABC')```-> 3
* a.replace('a', 'A')

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
#替换
a = 'abc'
a.replace('a', 'A')#'Abc'
a#'abc'
```

### 格式化

* 在Python中，采用的格式化方式和C语言是一致的，用%实现:

```py
'Hello, %s' % 'world'
'Hi, %s, you have $%d.' % ('Michael', 1000000)
```

常见的占位符有:
| 占位符 | 替换内容     |
| ------ | ------------ |
| %d     | 整数         |
| %f     | 浮点数       |
| %s     | 字符串       |
| %x     | 十六进制整数 |
| %%     | %            |

* 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多:

```py
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
```

## list 和 tuple

- Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
- 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

### list

* list里面的元素的数据类型也可以不同;
* list元素也可以是另一个list;
* 用索引来访问list中每一个位置的元素，记得索引是从0开始;
* 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1;
* 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素;
* list是一个可变的有序表，所以，可以往list中追加元素到末尾:```append()```;
* 也可以把元素插入到指定的位置,比如索引号为1的位置:```insert(1, 'xxx')```;
* 删除list末尾的元素，用pop()方法;返回最后一位的数据;
* 要删除指定位置的元素，用pop(i)方法，其中i是索引位置;
* 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置;
* 如果一个list中一个元素也没有，就是一个空的list，它的长度为0
* 给list排序:a.sort()

```py
# list的初始化
classmates = ['Michael', 'Bob', 'Tracy']#['Michael', 'Bob', 'Tracy']
# 长度
len(classmates)#3
# 添加到最后一位
classmates.append('Adam')#['Michael', 'Bob', 'Tracy', 'Adam']
# 插入到索引号为1的位置
classmates.insert(1, 'Jack')#['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
# 删除最后一位
classmates.pop()# 'Adam'
#把某个元素替换
classmates[1] = 'Sarah'# ['Michael', 'Sarah', 'Tracy']
# 二维表的存取
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']# 得到 'php',可以写p[1]或者s[2][1]
# 空
L = []
len(L)# 0
# 排序
a = ['c', 'b', 'a']
a.sort()#['a', 'b', 'c']
```

### tuple

* 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple;
* classmates这个tuple不能变了，它也没有append()，insert()这样的方法;
* 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素;
* 如果要定义一个空的tuple，可以写成();

```py
# 初始化
classmates = ('Michael', 'Bob', 'Tracy')
# 单元素 tuple 的定义
t = (1,)# t = (1)->定义的不是tuple，是1这个数！
# “可变的”tuple：
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
t # ('a', 'b', ['X', 'Y'])
# tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
```

## 条件判断

* 在Python程序中，用if语句实现条件判断;
* 如果if语句判断是True，就把缩进的两行print语句执行了,否则，什么也不做;
* 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了;
* 当然上面的判断是很粗略的，完全可以用elif做更细致的判断;
* if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else;
> 注意不要少写了冒号:

```py
# if
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
# else
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
#esif
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
```

## 循环

* Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来;
* 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环;
* 在循环中，break语句可以提前退出循环。
* 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。

### 循环

* 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：

```py
# 基础
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
# range()
list(range(5)) # [0, 1, 2, 3, 4]
# for in
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
    #在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。
print(sum)
#break
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
#continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
```

### 小结

* 循环是让计算机做重复任务的有效的方法。
* break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
* 要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

## dict 和 set

* Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
* set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

### dict

>因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
>第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
>dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
>对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。


* 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉;
* 如果key不存在，dict就会报错;
* 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在;
* 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value;
* 要删除一个key，用pop(key)方法，对应的value也会从dict中删除;

- 和list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
- 而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。

```py
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']# 95
#赋值
d['Adam'] = 67
d['Adam'] # 67
# in
'Thomas' in d # False
# get
d.get('Thomas') # 注意：返回None的时候Python的交互环境不显示结果。
d.get('Thomas', -1) # -1
d.pop('Bob')# 75
d #{'Michael': 95, 'Tracy': 85}
```

>所以，dict是用空间来换取时间的一种方法。
>dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
>这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
>要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

### set

* 要创建一个set，需要提供一个list作为输入集合
* 显示的顺序也不表示set是有序的
* 重复元素在set中自动被过滤
* 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
* 通过remove(key)方法可以删除元素
* set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
```py
# index
s = set([1, 2, 3])
s #{1, 2, 3}
# add
s.add(4)# {1, 2, 3, 4}
s.add(4)# {1, 2, 3, 4}
# delete
s.remove(4)#{1, 2, 3}
# 并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2# {2, 3}
s1 | s2# {1, 2, 3, 4}
```

## 函数

计算数列的和，比如：1 + 2 + 3 + ... + 100，写起来十分不方便，于是数学家发明了求和符号∑，可以把1 + 2 + 3 + ... + 100记作:$$\sum_{n=1}^{100}n$$

函数就是最基本的一种代码抽象的方式

### 调用函数

* 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误
* abs():绝对值，单次单个,int
* max():最大值,不限类型
* 类型转换:
* 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

```cmd
>>> max(1, 2)
2
>>> int('123')
123
>>> int(12.34)
12
>>> float('12.34')
12.34
>>> str(1.23)
'1.23'
>>> str(100)
'100'
>>> bool(1)
True
>>> bool('')
False
>>> a = abs # 变量a指向abs函数
>>> a(-1) # 所以也可以通过a调用abs函数
1
```

### 定义函数-def my_abs(x):

```py
# -*- coding: utf-8 -*-
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```

* 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
* 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）;

### 空函数-pass

* 如果想定义一个什么事也不做的空函数，可以用pass语句;
* pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
* 缺少了pass，代码运行就会有语法错误。
* 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError;
* 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现;

```py
def nop():
    pass
# if
if age >= 18:
    pass
# isinstance
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
```

### 返回多个值-return nx, ny

* 返回值是一个tuple:在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple
* 定义函数时，需要确定函数名和参数个数；
* 如果有必要，可以先对参数的数据类型做检查；
* 函数体内部可以用return随时返回函数结果；
* 函数执行完毕也没有return语句时，自动return None。
* 函数可以同时返回多个值，但其实就是一个tuple。

```py
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
```

```cmd
>>> r = move(100, 100, 60, math.pi / 6)
>>> print(r)
(151.96152422706632, 70.0)
```

### 函数的参数

* 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。
* 默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。
* 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
* 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。
* Python函数在定义的时候，默认参数L的值就被计算出来了，即\[\]，因为默认参数L也是一个变量，它指向对象\[\]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

>定义默认参数要牢记一点：默认参数必须指向不变对象！
>为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

```py
# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
```

### 可变参数-def calc(*numbers):

* 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个;
* 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
* Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：```>>> nums = [1, 2, 3] >>>calc(*nums)```

```py
# 列表 list or tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
    # calc([1, 2, 3])
    # calc((1, 3, 5, 7))
# 可变参
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

### 关键字参数-def person(name, age, **kw):

* 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict;
* 它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
* 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：

> \**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

```py
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

```cmd
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

### 命名关键字参数-def person(name, age, *, city, job):

* 如果要限制关键字参数的名字，就可以用命名关键字参数
* 命名关键字参数可以有缺省值，从而简化调用：```def person(name, age, *, city='Beijing', job):```
* 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个\*作为特殊分隔符。如果缺少\*

### 参数组合

* 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
* 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

```py
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```

>最神奇的是通过一个tuple和dict，你也可以调用上述函数：
```cmd
>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```

### 小结

- 要注意定义可变参数和关键字参数的语法：
    *args是可变参数，args接收的是一个tuple；
    **kw是关键字参数，kw接收的是一个dict。
- 以及调用函数时如何传入可变参数和关键字参数的语法：
    可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
    关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过\**kw传入：func(**{'a': 1, 'b': 2})。
- 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
- 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
- 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

## 递归函数

* 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数;
* 所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰;
* 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的;
* 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

>在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
>上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
```py
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
```
>可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。
>尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
>遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

## 高级特性

* 在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
* Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。

### 切片

* Python提供了切片（Slice）操作符，能大大简化这种操作.

```cmd
>>> L[0:3]
['Michael', 'Sarah', 'Tracy']
>>> L = list(range(100))
>>> L[:10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L[-10:]
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> L[10:20]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 前10个数，每两个取一个：
>>> L[:10:2]
[0, 2, 4, 6, 8]
>>> 所有数，每5个取一个：
>>> L[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> 只写[:]就可以原样复制一个list:
>>> L[:]
[0, 1, 2, 3, ..., 99]
>>> tuple也可以用切片操作，只是操作的结果仍是tuple:
>>> (0, 1, 2, 3, 4, 5)[:3]
(0, 1, 2)
>>> 字符串'xxx'也可以看成是一种list,只是操作结果仍是字符串:
>>> 'ABCDEFG'[:3]
'ABC'
>>> 'ABCDEFG'[::2]
'ACEG'
```
### 迭代

```python
# dict.value的迭代
def testDictValue(d):
    for v in d.values():
        print(v)

# dict.items的迭代
def testDictItems(d):
    for k,v in d.items():
        print('dict的key:%s,dict的value:%s'%(k,v))

# enumerate的迭代
def testEnumerate():
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)

# 两个变量的迭代
def testManyItem():
    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x,y) 
```

### 列表生成式

```python
L = [x * x for x in range(1, 11)]
L = [x * x for x in range(1, 11) if x % 2 == 0]
L= [x * x for x in range(1, 11)]
L= [x * x for x in range(1, 11) if x % 2 == 0]
L= [d for d in os.listdir('.')]
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L = [k + '=' + v for k, v in d.items()]
L = ['Hello', 'World', 'IBM', 'Apple']
l = [s.lower() for s in L]
L = ['Hello', 'World', 18, 'Apple', None]
l = [s.lower() for s in L if isinstance(s,str)]
```

### 生成器

- 只要把一个列表生成式的[]改成()，就创建了一个generator
- 可以通过next()函数获得generator的下一个返回值

## 模块

安装了Anaconda，并且进行了引入。

## 面向对象编程

- Object Oriented Programming --OOP,把对象作为程序的基本单元，一个对象包含了数据和做作数据的函数。

### 对象的编写

```py
class Sutdnet(object):
    def __init__(self,name,score):
        self.name= name
        self.score = score
    
    def print_score(self):
        print("%s:%s" %(self.name,self.score))
```

面线对象的设计丝线故事从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
面向对象的设计思路是抽象出Class，根据Class创建Instance。
面向对象的抽象程度🈶️比函数高，因为一个Class既包含数据，又包含了操作数据的方法。
数据封装，继承和多态是面向对象的三大特点。

#### 类和实例

class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
```py
class Student(object):
    pass
```
由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
```py
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
```
 > 注意：特殊方法“__init__”前后分别有两个下划线！！！
注意到`__init__`方法的第一个参数永远是`self`，表示创建的实例本身，因此，在`__init__`方法内部，就可以把各种属性绑定到`self`，因为`self`就指向创建的实例本身。

有了`__init__`方法，在创建实例的时候，就不能传入空的参数了，必须传入与`__init__`方法匹配的参数，但`self`不需要传，Python解释器自己会把实例变量传进去.

和普通的函数相比，在类中定义的函数只有一点不同，就是**第一个参数永远是实例变量self**，**并且，调用时，不用传递该参数**。*除此之外，类的方法和普通函数没有什么区别*，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

##### 数据封装

既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法

我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。

封装的另一个好处是可以给Student类增加新的方法


```txt
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
```

#### 访问限制

在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，**就隐藏了内部的复杂逻辑**。

> **如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，在Python中，实例的变量名如果以`__`开头，就变成了一个私有变量（*private*），只有内部可以访问，外部不能访问**

你也许会问，原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数

> **需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。**

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

> **不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量**

最后注意下面的这种错误写法：
```py
>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
```
表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：
```py
>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
```

#### 继承和多态

在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法。

当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。

多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：

对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

对扩展开放：允许新增Animal子类；

对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。比如如下的继承树：


静态语言 vs 动态语言
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

class Timer(object):
    def run(self):
        print('Start...')
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

> **这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。**

使用isinstance()
对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

```py
isinstance([1, 2, 3], (list, tuple))
```

> ** 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。**

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：`dir(str)`

类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的。

我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法。
```py
class MyDog(object):
    def __len__(self):
        return 100

>>> dog = MyDog()
>>> len(dog)
100
```
