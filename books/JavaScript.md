# js笔记

## 目录

- [js笔记](#js笔记)
  - [快速入门](#快速入门)
  - [函数](#函数)
    - [箭头函数--Arrow Function](#箭头函数--arrow-function)
    - [标准对象](#标准对象)
    - [Date](#date)
    - [RegExp](#regexp)
    - [JSON](#json)
    - [面向对象编程](#面向对象编程)
    - [class继承](#class继承)
  - [浏览器](#浏览器)
    - [浏览器对象](#浏览器对象)
      - [windows](#windows)
      - [navigator](#navigator)
      - [screen](#screen)
      - [document](#document)
      - [history](#history)
    - [操作DOM](#操作dom)
    - [更新DOM](#更新dom)
    - [插入DOM](#插入dom)
      - [insertBefore](#insertbefore)
      - [练习](#练习)
    - [删除DOM](#删除dom)
    - [表单操作](#表单操作)
    - [操作文件](#操作文件)
    - [AJAX](#ajax)
      - [安全限制](#安全限制)
      - [CORS](#cors)
    - [Promise](#promise)
    - [Canvas](#canvas)
  - [jQuery](#jquery)
    - [选择器](#选择器)
      - [层级选择器](#层级选择器)
      - [查找和过滤](#查找和过滤)

## 快速入门

[快速入门]

- 动态语言：变量本身不固定，静态语言：变量定义是必须制定变量类型
- strict模式：再不用var申明变量的情况下，直接使用变量，该变量则为全局变量，在js开头使用'usr strict';则使用strict模式，强制通过var定义变量，未使用的则报错ReferneceError 。
- 转义字符 \  可以转义很多字符，比如 \n 换行，\t 制表符，本身也可以转义 \\ ,ASCII字符可以以 \x## 表示十六进制：'\x41';//等同于'A',Unicode可以用 '\u####'表示，'\u4e2d\u6587'='中文'
- 多行字符（ES6）：`....`【`:反引号】。
- 模板字符串（ES6）：${XXX}

```js
var name ='小明';
var message = `你好，${name}`;//注意：用的是反引号
alert(message);
```

- 字符串的操作：toUpperCase();--变成大写，toLowerCase();--变成小写，indexOf();--会搜索制指定字符串的位置，字符串是不可变的，如果对字符串的某个索引赋值，不会有错，但是也不会变，substring():返回制定区间的子串

```js
var s = 'Hello,World';
s.toUpperCase();//HELLO,WORLD
s.toLowerCase();//hello,world
s.indexOf('world');//没有找到子串,返回-1
s.indexOf('World');//返回 7
s.substring(0,5);//返回'Hello'
s.substring(7);//从索引7开始到结束，返回'World'
```

- JavaScript的array可以包含任意的数据类型，并通过索引访问每个元素，要取Array的长度，可以直接访问length属性,给length赋值可以改变Array的大小，indexOf()可以搜索某个指定元素的位置，slice()是Array的截取函数，push()想Array结尾添加若干元素，pop()是删除最后一个元素，unshift()头部添加，shift()删除第一个元素，sort()是排序，reverse()是反转，splice()修改的方法（它可以从指定的索引开始删除若干元素，然后再从该位置添加若干元素），concat()连接并返回另一个新的array，join是把当前Array的每个元素都用指定的字符串连接起来，然后返回连接后的字符串

```js
var arr = [1, 2, 3.14, 'Hello', null, true];
arr.length;//6
arr.length = 8;
arr; // arr变为 [1, 2, 3.14, 'Hello', null, true, undefined, undefined]
arr.length = 2;
arr; // arr变为[1, 2]
arr[1] = 99;
arr; // arr现在变为['1', 99]
arr[5] = 'x';
arr; // arr变为['1', 99 , undefined, undefined, 'x']
arr.indexOf(99); // 元素10的索引为1
arr.indexOf('x'); // 元素'x'的索引为4
arr.indexOf(1); // 元素1没有找到，返回-1
arr.indexOf('1'); // 元素'1'的索引为0
arr.slice(0, 3); // 从索引0开始，到索引3结束，但不包括索引3: ['1', 99 , undefined]
arr.slice(3); // 从索引3开始到结束: [undefined, 'x']

arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
var aCopy = arr.slice();
aCopy; // ['A', 'B', 'C', 'D', 'E', 'F', 'G']
aCopy === arr; // false

arr = [1, 2];
arr.push('A', 'B'); // 返回Array新的长度: 4
arr; // [1, 2, 'A', 'B']
arr.pop(); // pop()返回'B'
arr; // [1, 2, 'A']
arr.pop(); arr.pop(); arr.pop(); // 连续pop 3次
arr; // []
arr.pop(); // 空数组继续pop不会报错，而是返回undefined
arr; // []

arr = [1, 2];
arr.unshift('A', 'B'); // 返回Array新的长度: 4
arr; // ['A', 'B', 1, 2]
arr.shift(); // 'A'
arr; // ['B', 1, 2]
arr.shift(); arr.shift(); arr.shift(); // 连续shift 3次
arr; // []
arr.shift(); // 空数组继续shift不会报错，而是返回undefined
arr; // []

arr = ['B', 'C', 'A'];
arr.sort();
arr; // ['A', 'B', 'C']

arr = ['one', 'two', 'three'];
arr.reverse();
arr; // ['three', 'two', 'one']

arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
// 从索引2开始删除3个元素,然后再添加两个元素:
arr.splice(2, 3, 'Google', 'Facebook'); // 返回删除的元素 ['Yahoo', 'AOL', 'Excite']
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
// 只删除,不添加:
arr.splice(2, 2); // ['Google', 'Facebook']
arr; // ['Microsoft', 'Apple', 'Oracle']
// 只添加,不删除:
arr.splice(2, 0, 'Google', 'Facebook'); // 返回[],因为没有删除任何元素
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']

arr = ['A', 'B', 'C'];
var added = arr.concat([1, 2, 3]);
added; // ['A', 'B', 'C', 1, 2, 3]
arr; // ['A', 'B', 'C']

arr = ['A', 'B', 'C'];
arr.concat(1, 2, [3, 4]); // ['A', 'B', 'C', 1, 2, 3, 4]
arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-'); // 'A-B-C-1-2-3'
arr = [[1, 2, 3], [400, 500, 600], '-'];
```

```js
//Array提供了一种顺序存储一组元素的功能，并可以按索引来读写。
//练习：在新生欢迎会上，你已经拿到了新同学的名单，请排序后显示：欢迎XXX，XXX，XXX和XXX同学！：
'use strict';
var arr = ['小明', '小红', '大军', '阿黄'];
//arr.sort();
//console.log(`欢迎${arr[0]},${arr[1]},${arr[2]}和${arr[3]}同学！`);
arr.push(`${arr.sort().pop()}同学！`);
arr.push(arr.splice(2,2).join('和'));
arr.unshift(`欢迎${arr.shift()}`);
console.log(arr.join(","));
```

- 对象：{...} 键值对以xxxx：xxxx形式申明，用'，'隔开，包含特殊字符则需要用''括起来，这种变量需要用['xxx']来访问，属性名尽量使用标准的变量名，这样就可以直接通过object.prop的形式访问一个属性了，实际上JavaScript对象的所有属性都是字符串，不过属性对应的值可以是任意数据类型。如果访问一个不存在的属性会返回什么呢？JavaScript规定，访问不存在的属性不报错，而是返回undefined，如果我们要检测xiaoming是否拥有某一属性，可以用in操作符：'name' in xiaoming; // true，'grade' in xiaoming; // false，不过要小心，如果in判断一个属性存在，这个属性不一定是xiaoming的，它可能是xiaoming继承得到的：'toString' in xiaoming; // true，因为toString定义在object对象中，而所有对象最终都会在原型链上指向object，所以xiaoming也拥有toString属性。要判断一个属性是否是xiaoming自身拥有的，而不是继承得到的，可以用hasOwnProperty()方法xiaoming.hasOwnProperty('name'); // true，xiaoming.hasOwnProperty('toString'); // false
- if判断建议永远都要写上{}，在多个if...else...语句中，如果某个条件成立，则后续就不再继续判断了
- JavaScript把null、undefined、0、NaN和空字符串''视为false，其他值一概视为true，因此上述代码条件判断的结果是true。
- var height = parseFloat(prompt('请输入身高(m):'));
- for循环的一个变体是for ... in循环，它可以把一个对象的所有属性依次循环出来：
- while:for循环在已知循环的初始和结束条件时非常有用。而上述忽略了条件的for循环容易让人看不清循环的逻辑，此时用while循环更佳。while循环只有一个判断条件，条件满足，就不断循环，条件不满足时则退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
- do ... while:最后一种循环是do { ... } while()循环，它和while循环的唯一区别在于，不是在每次循环开始的时候判断条件，而是在每次循环完成的时候判断条件：

```js
var o = {
  name: 'Jack',
  age: 20,
  city: 'Beijing'
};
for (var key in o) {
  console.log(key); // 'name', 'age', 'city'
}
//要过滤掉对象继承的属性，用hasOwnProperty()来实现：
var o = {
  name: 'Jack',
  age: 20,
  city: 'Beijing'
};
for (var key in o) {
  if (o.hasOwnProperty(key)) {
    console.log(key); // 'name', 'age', 'city'
  }
}
//由于Array也是对象，而它的每个元素的索引被视为对象的属性，因此，for ... in循环可以直接循环出Array的索引：
var a = ['A', 'B', 'C'];
for (var i in a) {
  console.log(i); // '0', '1', '2'
  console.log(a[i]); // 'A', 'B', 'C'
}//请注意，for ... in对Array的循环得到的是String而不是Number。
var x = 0;
var n = 99;
while (n > 0) {
  x = x + n;
  n = n - 2;
}
x; // 2500
var n = 0;
do {
  n = n + 1;
} while (n < 100);
n; // 100//用do { ... } while()循环要小心，循环体会至少执行1次，而for和while循环则可能一次都不执行。
```

- JavaScript的默认对象表示方式{}可以视为其他语言中的Map或Dictionary的数据结构，即一组键值对。但是JavaScript的对象有个小问题，就是键必须是字符串。但实际上Number或者其他数据类型作为键也是非常合理的。为了解决这个问题，最新的ES6规范引入了新的数据类型Map。
- Set和Map类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在Set中，没有重复的key。要创建一个Set，需要提供一个Array作为输入，或者直接创建一个空Set：重复元素在Set中自动被过滤：注意数字3和字符串'3'是不同的元素。通过add(key)方法可以添加元素到Set中，可以重复添加，但不会有效果：通过delete(key)方法可以删除元素：

```js
'use strict';
var m = new Map();
var s = new Set();
console.log('你的浏览器支持Map和Set！');
///
var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
m.get('Michael'); // 95
//
var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key 'Adam': true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key 'Adam'
m.get('Adam'); // undefined
//
var s1 = new Set(); // 空Set
var s2 = new Set([1, 2, 3]); // 含1, 2, 3
var s = new Set([1, 2, 3, 3, '3']);
s; // Set {1, 2, 3, "3"}
s.add(4);
s; // Set {1, 2, 3, 4}
s.add(4);
s; // 仍然是 Set {1, 2, 3, 4}
var s = new Set([1, 2, 3]);
s; // Set {1, 2, 3}
s.delete(3);
s; // Set {1, 2}
```

- 遍历Array可以采用下标循环，遍历Map和Set就无法使用下标。为了统一集合类型，ES6标准引入了新的iterable类型，Array、Map和Set都属于iterable类型。具有iterable类型的集合可以通过新的for ... of循环来遍历。for ... of循环是ES6引入的新的语法，用for ... of循环遍历集合，用法如下：

```js
var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
for (var x of a) { // 遍历Array
  console.log(x);
}
for (var x of s) { // 遍历Set
  console.log(x);
}
for (var x of m) { // 遍历Map
  console.log(x[0] + '=' + x[1]);
}
//forEach的使用
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
  // element: 指向当前元素的值
  // index: 指向当前索引
  // array: 指向Array对象本身
  console.log(element + ', index = ' + index);
});
var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
  console.log(element);
});
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
  console.log(value);
});
```

## 函数

[函数]

- js函数默认参数：arguments,只在函数内部起作用，并永远指向函数调用者传入的所有参数，arguments类似于Array但并不是。arguments最常用于判断传入参数的个数

```js
// foo(a[, b], c)
// 接收2~3个参数，b是可选参数，如果只传2个参数，b默认为null：
function foo(a, b, c) {
  if (arguments.length === 2) {
    // 实际拿到的参数是a和b，c为undefined
    c = b; // 把b赋给c
    b = null; // b变为默认值
  }
  // ...
}
```

- ES6引入rest,是一个Array数据，具有iterable属性,可以使用forEach(function(element,index,array){})进行遍历，

```js
function foo(a, b, ...rest) {
  console.log('a = ' + a);
  console.log('b = ' + b);
  console.log(rest);
}

foo(1, 2, 3, 4, 5);
// 结果:
// a = 1
// b = 2
// Array [ 3, 4, 5 ]

foo(1);
// 结果:
// a = 1
// b = undefined
// Array []
function sum(...rest){
   var a = 0 ;
  rest.forEach(function(e){a+=e})
   return a;
}
```

- 全局变量：不在任何函数内定义的变量就具有全局作用域。实际上，JavaScript默认有一个全局对象window，全局作用域的变量实际上被绑定到window的一个属性,JavaScript实际上只有一个全局作用域。任何变量（函数也视为变量），如果没有在当前函数作用域中找到，就会继续往上查找，最后如果在全局作用域中也没有找到，则报ReferenceError错误,全局变量会绑定到window上，不同的JavaScript文件如果使用了相同的全局变量，或者定义了相同名字的顶层函数，都会造成命名冲突，并且很难被发现。减少冲突的一个方法是把自己的所有变量和函数全部绑定到一个全局变量中。例如：

```js
// 唯一的全局变量MYAPP:
var MYAPP = {};

// 其他变量:
MYAPP.name = 'myapp';
MYAPP.version = 1.0;

// 其他函数:
MYAPP.foo = function () {
  return 'foo';
};
```

- 局部作用域：为了解决块级作用域，ES6引入了新的关键字let，用let替代var可以申明一个块级作用域的变量
- 常量:由于var和let申明的是变量，如果要申明一个常量，在ES6之前是不行的，我们通常用全部大写的变量来表示“这是一个常量，不要修改它的值”.ES6标准引入了新的关键字const来定义常量，const与let都具有块级作用域.

```js
'use strict';

const PI = 3.14;
PI = 3; // 某些浏览器不报错，但是无效果！
PI; // 3.14

function foo() {
  var sum = 0;
  for (let i=0; i<100; i++) {
    sum += i;
  }
  // SyntaxError:
  i += 1;
}
```

- [解构赋值]：从ES6开始，JavaScript引入了解构赋值，可以同时对一组变量进行赋值。***var [x, y, z] = ['hello', 'JavaScript', 'ES6'];***

```js
'use strict';
//也可以使用解构赋值，便于快速获取对象的指定属性
var person = {
  name: '小明',
  age: 20,
  gender: 'male',
  passport: 'G-12345678',
  school: 'No.4 middle school'
};
var {name, age, passport} = person;
//对一个对象进行解构赋值时，同样可以直接对嵌套的对象属性进行赋值，只要保证对应的层次是一致的
var person = {
  name: '小明',
  age: 20,
  gender: 'male',
  passport: 'G-12345678',
  school: 'No.4 middle school',
  address: {
    city: 'Beijing',
    street: 'No.1 Road',
    zipcode: '100001'
  }
};
var {name, address: {city, zip}} = person;
name; // '小明'
city; // 'Beijing'
zip; // undefined, 因为属性名是zipcode而不是zip
// 注意: address不是变量，而是为了让city和zip获得嵌套的address对象的属性:
address; // Uncaught ReferenceError: address is not defined
//使用解构赋值对对象属性进行赋值时，如果对应的属性不存在，变量将被赋值为undefined，这和引用一个不存在的属性获得undefined是一致的。如果要使用的变量名和属性名不一致，可以用下面的语法获取：
var person = {
  name: '小明',
  age: 20,
  gender: 'male',
  passport: 'G-12345678',
  school: 'No.4 middle school'
};

// 把passport属性赋值给变量id:
let {name, passport:id} = person;
name; // '小明'
id; // 'G-12345678'
// 注意: passport不是变量，而是为了让变量id获得passport属性:
passport; // Uncaught ReferenceError: passport is not defined

// 解构赋值还可以使用默认值，这样就避免了不存在的属性返回undefined的问题：
var person = {
  name: '小明',
  age: 20,
  gender: 'male',
  passport: 'G-12345678'
};

// 如果person对象没有single属性，默认赋值为true:
var {name, single=true} = person;
name; // '小明'
single; // true
```

- 方法：绑定到对象上的函数称为方法
> 在一个方法内部，this是一个特殊变量，它始终指向当前对象，也就是xiaoming这个变量。所以，this.birth可以拿到xiaoming的birth属性。
> new Date().getFullYear();
> 如果以对象的方法形式调用，比如xiaoming.age()，该函数的this指向被调用的对象，也就是xiaoming，这是符合我们预期的。如果单独调用函数，比如getAge()，此时，该函数的this指向全局对象，也就是window。

```js
'use strict';

var xiaoming = {
  name: '小明',
  birth: 1990,
  age: function () {
    var that = this; // 在方法内部一开始就捕获this
    function getAgeFromBirth() {
      var y = new Date().getFullYear();
      return y - that.birth; // 用that而不是this
    }
    return getAgeFromBirth();
  }
};
xiaoming.age(); // 25
```

- apply:要指定函数的this指向哪个对象，可以用函数本身的apply方法，它接收两个参数，第一个参数就是需要绑定的this变量，第二个参数是Array，表示函数本身的参数。用apply修复getAge()调用：

```js
function getAge() {
  var y = new Date().getFullYear();
  return y - this.birth;
}

var xiaoming = {
  name: '小明',
  birth: 1990,
  age: getAge
};

xiaoming.age(); // 25
getAge.apply(xiaoming, []); // 25, this指向xiaoming, 参数为空
```

> 另一个与apply()类似的方法是call()，唯一区别是：
>
>*apply()把参数打包成Array再传入；*
>
>*call()把参数按顺序传入。*
>
>比如调用Math.max(3, 5, 4)，分别用apply()和call()实现如下：
>> Math.max.apply(null, [3, 5, 4]); // 5
>>
>> Math.max.call(null, 3, 5, 4); // 5
>
>利用apply()，我们还可以动态改变函数的行为。
>
>JavaScript的所有对象都是动态的，即使内置的函数，我们也可以重新指向新的函数。
>
>现在假定我们想统计一下代码一共调用了多少次parseInt()，可以把所有的调用都找出来，然后手动加上count += 1，不过这样做太傻了。最佳方案是用我们自己的函数替换掉默认的parseInt()：

```js
'use strict';

var count = 0;
var oldParseInt = parseInt; // 保存原函数

window.parseInt = function () {
  count += 1;
  return oldParseInt.apply(null, arguments); // 调用原函数
};
// 测试:
parseInt('10');
parseInt('20');
parseInt('30');
console.log('count = ' + count); // 3
```

- 高阶函数：JavaScript的函数其实都指向某个变量。既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。编写高阶函数，就是让函数的参数能够接收别的函数。
- MapReduce：它既是一种编程模型，也是一种与之关联的、用于处理和产生大数据集的实现。请查看[文献]
- map:map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把Array的所有数字转为字符串
- reduce:reduce的用法。Array的reduce()把一个函数作用在这个Array的[x1, x2, x3...]上，这个函数必须接收两个参数，reduce()把结果继续和序列的下一个元素做累积计算，其效果就是:
> - [x1, x2, x3, x4].reduce(f) = f(f(f(x1, x2), x3), x4)

```js
'use strict';
//利用reduce()求积
function product(arr) {
  return arr.reduce(function(x,y){return x*=y;}) ;
}
```

> [测试失败] [console.log]

```js
//失败
var s = '123123';
var arr = s.split('');
var index = function (n) {
  var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
  numbers.forEach(function (e) {
    if ('' + e + '' === n) return e;
  })
}
var arr1 = arr.map(index);
return arr1.reduce(function (x, y) {
  return x * 10 + y;
});
//通过
var arr = s.split('');
var index  = function(n){
var numbers=[1,2,3,4,5,6,7,8,9,0];
var tmp = '';
numbers.forEach(function(e){
if(''+e+'' === n) tmp = e;});
return tmp;
}
arr = arr.map(index);
return arr.reduce(function (x,y){return x*10+y;});
```

- filter:[filter]也是一个常用的操作，它用于把Array的某些元素过滤掉，然后返回剩下的元素。false:去掉，true：为不去掉，同时如果不返回则全部去除。[练习]结果在这里。

### 箭头函数--Arrow Function

[箭头函数]

- 为什么叫Arrow Function？因为它的定义用的就是一个箭头：
> x => x * x
>>相当于 function (x) {return x * x;}

- 箭头函数相当于匿名函数，并且简化了函数定义。箭头函数有两种格式，一种像上面的，只包含一个表达式，连{ ... }和return都省略掉了。还有一种可以包含多条语句，这时候就不能省略{ ... }和return：

```js
x => {
  if (x > 0) {
    return x * x;
  }
  else {
    return - x * x;
  }
}
//如果参数不是一个，就需要用括号()括起来：
// 两个参数:
(x, y) => x * x + y * y
// 无参数:
() => 3.14
// 可变参数:
(x, y, ...rest) => {
  var i, sum = x + y;
  for (i=0; i<rest.length; i++) {
    sum += rest[i];
  }
  return sum;
}
//如果要返回一个对象，就要注意，如果是单表达式要改为：
// ok:
x => ({ foo: x })
```

### 标准对象

- 不要使用new Number()、new Boolean()、new String()创建包装对象；
- 用parseInt()或parseFloat()来转换任意类型到number；
- 用String()来转换任意类型到string，或者直接调用某个对象的toString()方法；
- 通常不必把任意类型转换为boolean再判断，因为可以直接写if (myVar) {...}；
- typeof操作符可以判断出number、boolean、string、function和undefined；
- 判断Array要使用Array.isArray(arr)；
- 判断null请使用myVar === null；
- 判断某个全局变量是否存在用typeof window.myVar === 'undefined'；
- 函数内部判断某个变量是否存在用typeof myVar === 'undefined'。

>更细心的同学指出，number对象调用toString()报SyntaxError：
>>123.toString(); // SyntaxError
>
>遇到这种情况，要特殊处理一下：
>>123..toString(); // '123', 注意是两个点！
>>
>>(123).toString(); // '123'

### Date

```js
var now = new Date();
now; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
now.getFullYear(); // 2015, 年份
now.getMonth(); // 5, 月份，注意月份范围是0~11，5表示六月
now.getDate(); // 24, 表示24号
now.getDay(); // 3, 表示星期三
now.getHours(); // 19, 24小时制
now.getMinutes(); // 49, 分钟
now.getSeconds(); // 22, 秒
now.getMilliseconds(); // 875, 毫秒数
now.getTime(); // 1435146562875, 以number形式表示的时间戳
//注意，当前时间是浏览器从本机操作系统获取的时间，所以不一定准确，因为用户可以把当前时间设定为任何值。
//如果要创建一个指定日期和时间的Date对象，可以用：
var d = new Date(2015, 5, 19, 20, 15, 30, 123);
d; // Fri Jun 19 2015 20:15:30 GMT+0800 (CST)
```

>JavaScript的Date对象月份值从0开始，牢记0=1月，1=2月，2=3月，……，11=12月。

第二种创建一个指定日期和时间的方法是解析一个符合ISO 8601格式的字符串：

```js
var d = Date.parse('2015-06-24T19:49:22.875+08:00');
d; // 1435146562875
```

但它返回的不是Date对象，而是一个时间戳。不过有时间戳就可以很容易地把它转换为一个Date：

```js
var d = new Date(1435146562875);
d; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
d.getMonth(); // 5
```

>使用Date.parse()时传入的字符串使用实际月份01~12，转换为Date对象后getMonth()获取的月份值为0~11。

```js
var d = new Date(1435146562875);
d.toLocaleString(); // '2015/6/24 下午7:49:22'，本地时间（北京时区+8:00），显示的字符串与操作系统设定的格式有关
d.toUTCString(); // 'Wed, 24 Jun 2015 11:49:22 GMT'，UTC时间，与本地时间相差8小时
```

- 正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

>在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字
>
>.可以匹配任意字符
>
>要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符

- 第一种方式是直接通过/正则表达式/写出来，第二种方式是通过new RegExp('正则表达式')创建一个RegExp对象。

```js
var re1 = /ABC\-001/;
var re2 = new RegExp('ABC\\-001');

re1; // /ABC\-001/
re2; // /ABC\-001/
```

- RegExp对象的test()方法用于测试给定的字符串是否符合条件。

```js
//无法识别连续的空格，用正则表达式试试：
'a b   c'.split(/\s+/); // ['a', 'b', 'c']
//无论多少个空格都可以正常分割。加入,试试：
'a,b, c  d'.split(/[\s\,]+/); // ['a', 'b', 'c', 'd']
//再加入;试试：
'a,b;; c  d'.split(/[\s\,\;]+/); // ['a', 'b', 'c', 'd']
```

### RegExp

- 分组：除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
- 贪婪匹配：正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。

```js
var re = /^(\d+)(0*)$/;
re.exec('102300'); // ['102300', '102300', '']
```

- 全局搜索：JavaScript的正则表达式还有几个特殊的标志，最常用的是g，表示全局匹配,全局匹配可以多次执行exec()方法来搜索一个匹配的字符串。当我们指定g标志后，每次运行exec()，正则表达式本身会更新lastIndex属性，表示上次匹配到的最后索引，全局匹配类似搜索，因此不能使用/^...$/，那样只会最多匹配一次。正则表达式还可以指定i标志，表示忽略大小写，m标志，表示执行多行匹配。
- 小结：正则表达式非常强大，要在短短的一节里讲完是不可能的。要讲清楚正则的所有内容，可以写一本厚厚的书了。如果你经常遇到正则表达式的问题，你可能需要一本正则表达式的参考书。

```js
var r1 = /test/g;
// 等价于:
var r2 = new RegExp('test', 'g');

var s = 'JavaScript, VBScript, JScript and ECMAScript';
var re=/[a-zA-Z]+Script/g;

// 使用全局匹配:
re.exec(s); // ['JavaScript']
re.lastIndex; // 10

re.exec(s); // ['VBScript']
re.lastIndex; // 20

re.exec(s); // ['JScript']
re.lastIndex; // 29

re.exec(s); // ['ECMAScript']
re.lastIndex; // 44

re.exec(s); // null，直到结束仍没有匹配到
```

- 练习

```js
'use strict';
//邮箱正则表达式
var re = /^[a-zA-Z\_\$][0-9a-zA-Z\_\.\$]*\@[0-9a-zA-Z\_\$]*\.[a-zA-Z\$]/;
// 测试:
var
  i,
  success = true,
  should_pass = ['someone@gmail.com', 'bill.gates@microsoft.com', 'tom@voyager.org', 'bob2015@163.com'],
  should_fail = ['test#gmail.com', 'bill@microsoft', 'bill%gates@ms.com', '@voyager.org'];
for (i = 0; i < should_pass.length; i++) {
  if (!re.test(should_pass[i])) {
    console.log('测试失败: ' + should_pass[i]);
    success = false;
    break;
  }
}
for (i = 0; i < should_fail.length; i++) {
  if (re.test(should_fail[i])) {
    console.log('测试失败: ' + should_fail[i]);
    success = false;
    break;
  }
}
if (success) {
  console.log('测试通过!');
}
```

### JSON

[JSON]

- 是JavaScript Object Notation的缩写，它是一种数据交换格式。道格拉斯·克罗克福特（Douglas Crockford:道格拉斯同学长期担任雅虎的高级架构师，自然钟情于JavaScript。）在2002年的一天发明了JSON这种超轻量级的数据交换格式。JSON实际上是JavaScript的一个子集
  - 在JSON中，一共就这么几种数据类型：
  - number：和JavaScript的number完全一致；
  - boolean：就是JavaScript的true或false；
  - string：就是JavaScript的string；
  - null：就是JavaScript的null；
  - array：就是JavaScript的Array表示方式——[]；
  - object：就是JavaScript的{ ... }表示方式。
- JSON还定死了字符集必须是UTF-8,JSON的字符串规定必须用双引号`""`，Object的键也必须用双引号`""`,json的序列化函数：stringify(),JSON.stringify(xiaoming, null, '  ');

```js
'use strict';
var xiaoming = {
  name: '小明',
  age: 14,
  gender: true,
  height: 1.65,
  grade: null,
  'middle-school': '\"W3C\" Middle School',
  skills: ['JavaScript', 'Java', 'Python', 'Lisp']
  };
var s = JSON.stringify(xiaoming);
console.log(s);
JSON.stringify(xiaoming, ['name', 'skills'], '  ');
xiaoming ={
  "name": "小明",
  "skills": [
  "JavaScript",
  "Java",
  "Python",
  "Lisp"
  ]
}
function convert(key, value) {
  if (typeof value === 'string') {
    return value.toUpperCase();
  }
  return value;
}

JSON.stringify(xiaoming, convert, '  ');
xiaoming ={
  "name": "小明",
  "age": 14,
  "gender": true,
  "height": 1.65,
  "grade": null,
  "middle-school": "\"W3C\" MIDDLE SCHOOL",
  "skills": [
  "JAVASCRIPT",
  "JAVA",
  "PYTHON",
  "LISP"
  ]
}
//如果我们还想要精确控制如何序列化小明，可以给xiaoming定义一个toJSON()的方法，直接返回JSON应该序列化的数据：
var xiaoming = {
  name: '小明',
  age: 14,
  gender: true,
  height: 1.65,
  grade: null,
  'middle-school': '\"W3C\" Middle School',
  skills: ['JavaScript', 'Java', 'Python', 'Lisp'],
  toJSON: function () {
    return { // 只输出name和age，并且改变了key：
      'Name': this.name,
      'Age': this.age
    };
  }
};

JSON.stringify(xiaoming); // '{"Name":"小明","Age":14}'
//拿到一个JSON格式的字符串，我们直接用JSON.parse()把它变成一个JavaScript对象：
JSON.parse('[1,2,3,true]'); // [1, 2, 3, true]
JSON.parse('{"name":"小明","age":14}'); // Object {name: '小明', age: 14}
JSON.parse('true'); // true
JSON.parse('123.45'); // 123.45
var obj = JSON.parse('{"name":"小明","age":14}', function (key, value) {
  if (key === 'name') {
    return value + '同学';
  }
  return value;
});
console.log(JSON.stringify(obj)); // {name: '小明同学', age: 14}
```

### 面向对象编程

- avaScript的面向对象编程和大多数其他语言如Java、C#的面向对象编程都不太一样。如果你熟悉Java或C#，很好，你一定明白面向对象的两个基本概念：
  1. 类：类是对象的类型模板，例如，定义`Student`类来表示学生，类本身是一种类型，`Student`表示学生类型，但不表示任何具体的某个学生；
  2. 实例：实例是根据类创建的对象，例如，根据`Student`类可以创建出xiaoming、xiaohong、xiaojun等多个实例，每个实例表示一个具体的学生，他们全都属于`Student`类型。
- 在JavaScript中，这个概念需要改一改。JavaScript不区分类和实例的概念，而是通过原型（prototype）来实现面向对象编程。

```js
var Student = {
  name: 'Robot',
  height: 1.2,
  run: function () {
    console.log(this.name + ' is running...');
  }
};

var xiaoming = {
  name: '小明'
};
xiaoming.__proto__ = Student;
```

>注意最后一行代码把xiaoming的原型指向了对象Student，看上去xiaoming仿佛是从Student继承下来的
>
>在JavaScrip代码运行时期，你可以把xiaoming从Student变成Bird，或者变成任何对象。

- 请注意，上述代码仅用于演示目的。在编写JavaScript代码时，不要直接用obj.\__proto\__去改变一个对象的原型，并且，低版本的IE也无法使用\__proto\__。Object.create()方法可以传入一个原型对象，并创建一个基于该原型的新对象，但是新对象什么属性都没有，因此，我们可以编写一个函数来创建xiaoming：

```js
// 原型对象:
var Student = {
  name: 'Robot',
  height: 1.2,
  run: function () {
    console.log(this.name + ' is running...');
  }
};

function createStudent(name) {
  // 基于Student原型创建一个新对象:
  var s = Object.create(Student);
  // 初始化新对象:
  s.name = name;
  return s;
}

var xiaoming = createStudent('小明');
xiaoming.run(); // 小明 is running...
xiaoming.__proto__ === Student; // true
```

- JavaScript对每个创建的对象都会设置一个原型，指向它的原型对象。
  >当我们用obj.xxx访问一个对象的属性时，JavaScript引擎先在当前对象上查找该属性，如果没有找到，就到其原型对象上找，如果还没有找到，就一直上溯到Object.prototype对象，最后，如果还没有找到，就只能返回undefined。

- 构造函数：除了直接用{ ... }创建一个对象外，JavaScript还可以用一种构造函数的方法来创建对象。它的用法是，先定义一个构造函数：

```js
  function Student(name) {
    this.name = name;
    this.hello = function () {
      alert('Hello, ' + this.name + '!');
    }
  }
  var xiaoming = new Student('小明');
  xiaoming.name;// '小明'
  xiaoming.hello();// Hello, 小明!
```

- 在JavaScript中，可以用关键字new来调用这个函数，并返回一个对象：
  > 注意，如果不写`new`，这就是一个普通函数，它返回`undefined`。但是，如果写了`new`，它就变成了一个构造函数，它绑定的`this`指向新创建的对象，并默认返回`this`，也就是说，不需要在最后写`return this`;。

```js
xiaoming ----> Student.prototype ----> Object.prototype ----> null
```

### class继承

- 新的关键字class从ES6开始正式被引入到JavaScript中。class的目的就是让定义类更简单。

```js
//class的定义包含了构造函数constructor和定义在原型对象上的函数hello()（注意没有function关键字），这样就避免了Student.prototype.hello = function () {...}这样分散的代码。
class Student {
  constructor(name) {
    this.name = name;
  }

  hello() {
    alert('Hello, ' + this.name + '!');
  }
}
```

- 用`class`定义对象的另一个巨大的好处是继承更方便了。想一想我们从Student派生一个PrimaryStudent需要编写的代码量。现在，原型继承的中间对象，原型对象的构造函数等等都不需要考虑了，直接通过`extends`来实现：

```js
class PrimaryStudent extends Student {
  constructor(name, grade) {
    super(name); // 记得用super调用父类的构造方法!
    this.grade = grade;
  }

  myGrade() {
    alert('I am at grade ' + this.grade);
  }
}
```

注意PrimaryStudent的定义也是`class`关键字实现的，而`extends`则表示原型链对象来自Student。子类的构造函数可能会与父类不太相同，例如，PrimaryStudent需要name和grade两个参数，并且需要通过`super(name)`来调用父类的构造函数，否则父类的`name`属性无法正常初始化。

PrimaryStudent已经自动获得了父类Student的hello方法，我们又在子类中定义了新的myGrade方法。

ES6引入的class和原有的JavaScript原型继承有什么区别呢？实际上它们没有任何区别，`class`的作用就是让JavaScript引擎去实现原来需要我们自己编写的原型链代码。简而言之，用`class`的好处就是极大地简化了原型链代码。

你一定会问，class这么好用，能不能现在就用上？

现在用还早了点，因为不是所有的主流浏览器都支持`ES6`的`class`。如果一定要现在就用上，就需要一个工具把`class`代码转换为传统的`prototype`代码，可以试试[`Babel`]这个工具。

```js
//练习
'use strict';
class Animal {
  constructor(name) {
    this.name = name;
  }
}
class Cat extends Animal {
  constructor(name) {
    super(name);
  }
  say() {
    return 'Hello, ' + this.name + '!';
  }
}
// 测试:
var kitty = new Cat('Kitty');
var doraemon = new Cat('哆啦A梦');
if ((new Cat('x') instanceof Animal) && kitty && kitty.name === 'Kitty' && kitty.say && typeof kitty.say === 'function' && kitty.say() === 'Hello, Kitty!' && kitty.say === doraemon.say) {
  console.log('测试通过!');
} else {
  console.log('测试失败!');
}
```

## 浏览器

[浏览器]

- IE 6~11：国内用得最多的`IE`浏览器，历来对W3C标准支持差。从`IE10`开始支持ES6标准；
- Chrome：`Google`出品的基于`Webkit`内核浏览器，内置了非常强悍的JavaScript引擎——`V8`。由于Chrome一经安装就时刻保持自升级，所以不用管它的版本，最新版早就支持`ES6`了；
- Safari：`Apple`的Mac系统自带的基于`Webkit`内核的浏览器，从`OS X 10.7 Lion`自带的6.1版本开始支持`ES6`，目前最新的`OS X 10.11 El Capitan`自带的`Safari`版本是`9.x`，早已支持`ES6`；
- Firefox：`Mozilla`自己研制的`Gecko`内核和`JavaScript`引擎`OdinMonkey`。早期的`Firefox`按版本发布，后来终于聪明地学习`Chrome`的做法进行自升级，时刻保持最新；
- 移动设备上目前`iOS`和`Android`两大阵营分别主要使用`Apple`的`Safari`和Google的`Chrome`，由于两者都是`Webkit`核心，结果`HTML5`首先在手机上全面普及（桌面绝对是`Microsoft`拖了后腿），对`JavaScript`的标准支持也很好，最新版本均支持ES6。

其他浏览器如`Opera`等由于市场份额太小就被自动忽略了。

另外还要注意识别各种国产浏览器，如某某安全浏览器，某某旋风浏览器，它们只是做了一个壳，其核心调用的是`IE`，也有号称同时支持`IE`和`Webkit`的“双核”浏览器。

不同的浏览器对`JavaScript`支持的差异主要是，有些`API`的接口不一样，比如`AJAX，File接口`。对于ES6标准，不同的浏览器对各个特性支持也不一样。

在编写JavaScript的时候，就要充分考虑到浏览器的差异，尽量让同一份JavaScript代码能运行在不同的浏览器中。

### 浏览器对象

- JavaScript可以获取浏览器提供的很多对象，并进行操作。

#### windows

`window`对象不但充当全局作用域，而且表示浏览器窗口。

`window`对象有`innerWidth`和`innerHeight`属性，可以获取浏览器窗口的内部宽度和高度。内部宽高是指除去菜单栏、工具栏、边框等占位元素后，用于显示网页的净宽高。`兼容性：IE<=8不支持。`
对应的，还有一个`outerWidth`和`outerHeight`属性，可以获取浏览器窗口的整个宽高。

#### navigator

navigator对象表示浏览器的信息，最常用的属性包括：

- navigator.appName：浏览器名称；
- navigator.appVersion：浏览器版本；
- navigator.language：浏览器设置的语言；
- navigator.platform：操作系统类型；
- navigator.userAgent：浏览器设定的User-Agent字符串。

```js
console.log('appName = ' + navigator.appName);
console.log('appVersion = ' + navigator.appVersion);
console.log('language = ' + navigator.language);
console.log('platform = ' + navigator.platform);
console.log('userAgent = ' + navigator.userAgent);
```

- 但这样既可能判断不准确，也很难维护代码。正确的方法是充分利用JavaScript对不存在属性返回`undefined`的特性，直接用短路运算符`||`计算：`var width = window.innerWidth || document.body.clientWidth;`

#### screen

screen对象表示屏幕的信息，常用的属性有：

- screen.width：屏幕宽度，以像素为单位；
- screen.height：屏幕高度，以像素为单位；
- screen.colorDepth：返回颜色位数，如8、16、24。

`location`对象表示当前页面的URL信息。例如，一个完整的URL：`http://www.example.com:8080/path/index.html?a=1&b=2#TOP`,可以用location.href获取。要获得URL各个部分的值，可以这么写：

```js
location.protocol; // 'http'
location.host; // 'www.example.com'
location.port; // '8080'
location.pathname; // '/path/index.html'
location.search; // '?a=1&b=2'
location.hash; // 'TOP'
```

要加载一个新页面，可以调用location.assign()。如果要重新加载当前页面，调用location.reload()方法非常方便。

```js
'use strict';
if (confirm('重新加载当前页' + location.href + '?')) {
  location.reload();
} else {
  location.assign('/'); // 设置一个新的URL地址
}
```

#### document

`document`对象表示当前页面。由于`HTML`在浏览器中以`DOM`形式表示为树形结构，`document`对象就是整个`DOM`树的根节点。

`document`的`title`属性是从`HTML`文档中的`<title>xxx</title>`读取的，但是可以动态改变：`'use strict';document.title = 'JavaScript';`
要查找DOM树的某个节点，需要从`document`对象开始查找。最常用的查找是根据`ID`和`Tag Name`。
用`document`对象提供的`getElementById()`和`getElementsByTagName()`可以按`ID`获得一个`DOM`节点和按`Tag`名称获得一组`DOM`节点：

```html
<dl id="drink-menu" style="border:solid 1px #ccc;padding:6px;">
  <dt>摩卡</dt>
  <dd>热摩卡咖啡</dd>
  <dt>酸奶</dt>
  <dd>北京老酸奶</dd>
  <dt>果汁</dt>
  <dd>鲜榨苹果汁</dd>
</dl>
```

```js
var menu = document.getElementById('drink-menu');
var drinks = document.getElementsByTagName('dt');
var i, s, menu, drinks;

menu = document.getElementById('drink-menu');
menu.tagName; // 'DL'

drinks = document.getElementsByTagName('dt');
s = '提供的饮料有:';
for (i=0; i<drinks.length; i++) {
  s = s + drinks[i].innerHTML + ',';
}
console.log(s);
//提供的饮料有:摩卡,酸奶,果汁,
```

document对象还有一个cookie属性，可以获取当前页面的Cookie。
> Cookie是由服务器发送的`key-value`标示符。因为`HTTP`协议是无状态的，但是服务器要区分到底是哪个用户发过来的请求，就可以用`Cookie`来区分。当一个用户成功登录后，服务器发送一个`Cookie`给浏览器，例如`user=ABC123XYZ(加密的字符串)...`，此后，浏览器访问该网站时，会在请求头附上这个`Cookie`，服务器根据`Cookie`即可区分出用户。
>
>`Cookie`还可以存储网站的一些设置，例如，页面显示的语言等等。
>
>`JavaScript`可以通过`document.cookie`读取到当前页面的`Cookie`：
>> `document.cookie; // 'v=123; remember=true; prefer=zh'`
>
>如果引入的第三方的`JavaScript`中存在恶意代码，则www.foo.com网站将直接获取到www.example.com网站的用户登录信息。
>
>为了解决这个问题，服务器在设置`Cookie`时可以使用`httpOnly`，设定了`httpOnly`的`Cookie`将不能被`JavaScript`读取。这个行为由浏览器实现，主流浏览器均支持`httpOnly`选项，`IE`从`IE6 SP1`开始支持。
>
>为了确保安全，服务器端在设置`Cookie`时，应该始终坚持使用`httpOnly`。

#### history

`history`对象保存了浏览器的历史记录，`JavaScript`可以调用`history`对象的`back()`或`forward ()`，相当于用户点击了浏览器的“后退”或“前进”按钮。

这个对象属于历史遗留对象，对于现代`Web`页面来说，由于大量使用`AJAX`和页面交互，简单粗暴地调用`history.back()`可能会让用户感到非常愤怒。

新手开始设计`Web`页面时喜欢在登录页登录成功时调用`history.back()`，试图回到登录前的页面。**这是一种错误的方法。**

- 任何情况，你都不应该使用history这个对象了。

### 操作DOM

由于HTML文档被浏览器解析后就是一棵DOM树，要改变HTML的结构，就需要通过JavaScript来操作DOM。

始终记住DOM是一个树形结构。操作一个DOM节点实际上就是这么几个操作：

- 更新：更新该DOM节点的内容，相当于更新了该DOM节点表示的HTML的内容；
- 遍历：遍历该DOM节点下的子节点，以便进行进一步操作；
- 添加：在该DOM节点下新增一个子节点，相当于动态增加了一个HTML节点；
- 删除：将该节点从HTML中删除，相当于删掉了该DOM节点的内容以及它包含的所有子节点。

在操作一个`DOM`节点前，我们需要通过各种方式先拿到这个`DOM`节点。最常用的方法是`document.getElementById()`和`document.getElementsByTagName()`，以及`CSS`选择器`document.getElementsByClassName()`。

由于`ID`在`HTML`文档中是唯一的，所以`document.getElementById()`可以直接定位唯一的一个`DOM`节点。`document.getElementsByTagName()`和`document.getElementsByClassName()`总是返回一组`DOM`节点。要精确地选择`DOM`，可以先定位父节点，再从父节点开始选择，以缩小范围。例如：

```js
// 返回ID为'test'的节点：
var test = document.getElementById('test');
// 先定位ID为'test-table'的节点，再返回其内部所有tr节点：
var trs = document.getElementById('test-table').getElementsByTagName('tr');
// 先定位ID为'test-div'的节点，再返回其内部所有class包含red的节点：
var reds = document.getElementById('test-div').getElementsByClassName('red');
// 获取节点test下的所有直属子节点:
var cs = test.children;
// 获取节点test下第一个、最后一个子节点：
var first = test.firstElementChild;
var last = test.lastElementChild;


```

第二种方法是使用`querySelector()`和`querySelectorAll()`，需要了解`selector`语法，然后使用条件来获取节点，更加方便：

```js
// 通过querySelector获取ID为q1的节点：
var q1 = document.querySelector('#q1');

// 通过querySelectorAll获取q1节点内的符合条件的所有节点：
var ps = q1.querySelectorAll('div.highlighted > p');
```

>注意：低版本的`IE<8`不支持`querySelector`和`querySelectorAll`。`IE8`仅有限支持。

严格地讲，我们这里的`DOM`节点是指`Element`，但是`DOM`节点实际上是`Node`，在`HTML`中，`Node`包括`Element`、`Comment`、`CDATA_SECTION`等很多种，以及根节点`Document`类型，但是，绝大多数时候我们只关心`Element`，也就是实际控制页面结构的`Node`，其他类型的`Node`忽略即可。根节点`Document`已经自动绑定为全局变量`document`。

```html
<!-- HTML结构 -->
<div id="test-div">
<div class="c-red">
  <p id="test-p">JavaScript</p>
  <p>Java</p>
  </div>
  <div class="c-red c-green">
  <p>Python</p>
  <p>Ruby</p>
  <p>Swift</p>
  </div>
  <div class="c-green">
  <p>Scheme</p>
  <p>Haskell</p>
  </div>
</div>
```

```js
'use strict';
// 选择<p>JavaScript</p>:
var js = document.querySelector('#test-p');
// 选择<p>Python</p>,<p>Ruby</p>,<p>Swift</p>:
var arr = document.querySelectorAll('div.c-red.c-green > p');
// 选择<p>Haskell</p>:
var haskell = document.querySelectorAll('div.c-green')[1].lastElementChild;
// 测试:
if (!js || js.innerText !== 'JavaScript') {
  alert('选择JavaScript失败!');
} else if (!arr || arr.length !== 3 || !arr[0] || !arr[1] || !arr[2] || arr[0].innerText !== 'Python' || arr[1].innerText !== 'Ruby' || arr[2].innerText !== 'Swift') {
  console.log('选择Python,Ruby,Swift失败!');
} else if (!haskell || haskell.innerText !== 'Haskell') {
  console.log('选择Haskell失败!');
} else {
  console.log('测试通过!');
}
```

### 更新DOM

可以直接修改节点的文本，方法有两种：

**一种是修改`innerHTML`属性，这个方式非常强大，不但可以修改一个`DOM`节点的文本内容，还可以直接通过`HTML`片段修改`DOM`节点内部的子树：**

```js
// 获取<p id="p-id">...</p>
var p = document.getElementById('p-id');
// 设置文本为abc:
p.innerHTML = 'ABC'; // <p id="p-id">ABC</p>
// 设置HTML:
p.innerHTML = 'ABC <span style="color:red">RED</span> XYZ';
// <p>...</p>的内部结构已修改
```

用`innerHTML`时要注意，是否需要写入`HTML`。如果写入的字符串是通过网络拿到了，要注意对字符编码来避免`XSS`攻击。

**第二种是修改innerText或textContent属性，这样可以自动对字符串进行HTML编码，保证无法设置任何HTML标签:**

```js
// 获取<p id="p-id">...</p>
var p = document.getElementById('p-id');
// 设置文本:
p.innerText = '<script>alert("Hi")</script>';
// HTML被自动编码，无法设置一个<script>节点:
// <p id="p-id">&lt;script&gt;alert("Hi")&lt;/script&gt;</p>
```

两者的区别在于读取属性时，`innerText`不返回隐藏元素的文本，而`textContent`返回所有文本。另外注意`IE<9`不支持`textContent`。

修改`CSS`也是经常需要的操作。DOM节点的`style`属性对应所有的`CSS`，可以直接获取或设置。因为`CSS`允许`font-size`这样的名称，但它并非`JavaScript`有效的属性名，所以需要在`JavaScript`中改写为驼峰式命名`fontSize`：

```js
// 获取<p id="p-id">...</p>
var p = document.getElementById('p-id');
// 设置CSS:
p.style.color = '#ff0000';
p.style.fontSize = '20px';
p.style.paddingTop = '2em';
```

### 插入DOM

如果这个`DOM`节点是空的，例如，`<div></div>`，那么，直接使用`innerHTML = '<span>child</span>'`就可以修改`DOM`节点的内容，相当于“插入”了新的DOM节点。

如果这个DOM节点不是空的，那就不能这么做，因为innerHTML会直接替换掉原来的所有子节点。

有两个办法可以插入新的节点。**一个是使用appendChild，把一个子节点添加到父节点的最后一个子节点。** 把`<p id="js">JavaScript</p>`添加到`<div id="list">`的最后一项：例如：

```html
<!--原本-->
<!-- HTML结构 -->
<p id="js">JavaScript</p>
<div id="list">
  <p id="java">Java</p>
  <p id="python">Python</p>
  <p id="scheme">Scheme</p>
</div>

<!--结果-->
<!-- HTML结构 -->
<div id="list">
  <p id="java">Java</p>
  <p id="python">Python</p>
  <p id="scheme">Scheme</p>
  <p id="js">JavaScript</p>
</div>
```

```js
var
  js = document.getElementById('js'),
  list = document.getElementById('list');
list.appendChild(js);
```

因为我们插入的`js`节点已经存在于当前的文档树，因此这个节点首先会从原先的位置删除，再插入到新的位置。

**更多的时候我们会从零创建一个新的节点，然后插入到指定位置:**

```js
var
  list = document.getElementById('list'),
  haskell = document.createElement('p');
haskell.id = 'haskell';
haskell.innerText = 'Haskell';
list.appendChild(haskell);
```

动态创建一个节点然后添加到DOM树中，可以实现很多功能。举个例子，下面的代码动态创建了一个`<style>`节点，然后把它添加到`<head>`节点的末尾，这样就动态地给文档添加了新的CSS定义：

```js
var d = document.createElement('style');
d.setAttribute('type', 'text/css');
d.innerHTML = 'p { color: red }';
document.getElementsByTagName('head')[0].appendChild(d);
```

#### insertBefore

如果我们要把子节点插入到指定的位置怎么办？可以使用`parentElement.insertBefore(newElement, referenceElement);`，子节点会插入到`referenceElement`之前。

```html
<!-- HTML结构 -->
<div id="list">
  <p id="java">Java</p>
  <p id="python">Python</p>
  <p id="scheme">Scheme</p>
</div>
```

```js
var
  list = document.getElementById('list'),
  ref = document.getElementById('python'),
  haskell = document.createElement('p');
haskell.id = 'haskell';
haskell.innerText = 'Haskell';
list.insertBefore(haskell, ref);
```

可见，使用`insertBefore`重点是要拿到一个“参考子节点”的引用。很多时候，需要循环一个父节点的所有子节点，可以通过迭代`children`属性实现：

```js
var
  i, c,
  list = document.getElementById('list');
for (i = 0; i < list.children.length; i++) {
  c = list.children[i]; // 拿到第i个子节点
}
```

#### 练习

```html
<!-- HTML结构 -->
<ol id="test-list">
  <li class="lang">Scheme</li>
  <li class="lang">JavaScript</li>
  <li class="lang">Python</li>
  <li class="lang">Ruby</li>
  <li class="lang">Haskell</li>
</ol>
```

按字符串顺序重新排序DOM节点：

```js
'use strict';
// sort list:
var arr = [],
  list = document.querySelectorAll('li.lang'),
div_list = document.querySelector('#test-list');
list.forEach(e =>{
  arr.push(e.innerHTML);
});
arr.sort();
console.log(arr);
arr.forEach(e =>{
console.log(e);
let i,c;
  for(i= 0; i< list.length;i++){
    c=list[i];
    if(c.innerHTML === e){
      div_list .appendChild(c);
    }

  }
});
// 测试:
;(function () {
  var
    arr, i,
    t = document.getElementById('test-list');
  if (t && t.children && t.children.length === 5) {
    arr = [];
    for (i=0; i<t.children.length; i++) {
      arr.push(t.children[i].innerText);
    }
    if (arr.toString() === ['Haskell', 'JavaScript', 'Python', 'Ruby', 'Scheme'].toString()) {
      console.log('测试通过!');
    }
    else {
      console.log('测试失败: ' + arr.toString());
    }
  }
  else {
    console.log('测试失败!');
  }
})();
```

#### 删除DOM

要删除一个节点，首先要获得该节点本身以及它的父节点，然后，调用父节点的removeChild把自己删掉：

```js
// 拿到待删除节点:
var self = document.getElementById('to-be-removed');
// 拿到父节点:
var parent = self.parentElement;
// 删除:
var removed = parent.removeChild(self);
removed === self; // true
```

- 注意到删除后的节点虽然不在文档树中了，但其实它还在内存中，可以随时再次被添加到别的位置。
- 当你遍历一个父节点的子节点并进行删除操作时，要注意，children属性是一个只读属性，并且它在子节点变化时会实时更新。
- 因此，删除多个节点时，要注意children属性时刻都在变化。

```js
var parent = document.getElementById('parent');
parent.removeChild(parent.children[0]);
parent.removeChild(parent.children[1]); // <-- 浏览器报错
```

### 表单操作

用JavaScript操作表单和操作DOM是类似的，因为表单本身也是DOM树。

不过表单的输入框、下拉框等可以接收用户输入，所以用JavaScript来操作表单，可以获得用户输入的内容，或者对一个输入框设置新的内容。
HTML表单的输入控件主要有以下几种：

- 文本框，对应的`<input type="text">`，用于输入文本；

- 口令框，对应的`<input type="password">`，用于输入口令；

- 单选框，对应的`<input type="radio">`，用于选择一项；

- 复选框，对应的`<input type="checkbox">`，用于选择多项；

- 下拉框，对应的`<select>`，用于选择一项；

- 隐藏文本，对应的`<input type="hidden">`，用户不可见，但表单提交时会把隐藏文本发送到服务器。

1.*获取值*

```js
//如果我们获得了一个<input>节点的引用，就可以直接调用value获得对应的用户输入值,这种方式可以应用于text、password、hidden以及select
// <input type="text" id="email">
var input = document.getElementById('email');
input.value; // '用户输入的值'
//但是，对于单选框和复选框，value属性返回的永远是HTML预设的值，而我们需要获得的实际是用户是否“勾上了”选项，所以应该用checked判断：
// <label><input type="radio" name="weekday" id="monday" value="1"> Monday</label>
// <label><input type="radio" name="weekday" id="tuesday" value="2"> Tuesday</label>
var mon = document.getElementById('monday');
var tue = document.getElementById('tuesday');
mon.value; // '1'
tue.value; // '2'
mon.checked; // true或者false
tue.checked; // true或者false
```

2.*设置值*

```js
//设置值和获取值类似，对于text、password、hidden以及select，直接设置value就可以：
// <input type="text" id="email">
var input = document.getElementById('email');
input.value = 'test@example.com'; // 文本框的内容已更新
//对于单选框和复选框，设置checked为true或false即可
```

3.[*HTML5控件*](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434499922277b890fd537901490a84fc24b2b8b8867e000)

- HTML5新增了大量标准控件，常用的包括date、datetime、datetime-local、color等，它们都使用`<input>`标签：
- 不支持HTML5的浏览器无法识别新的控件，会把它们当做type="text"来显示。支持HTML5的浏览器将获得格式化的字符串。例如，type="date"类型的input的value将保证是一个有效的YYYY-MM-DD格式的日期，或者空字符串。

```js
<input type="date" value="2015-07-01">
<input type="datetime-local" value="2015-07-01T02:03:04">
<input type="color" value="#ff0000">
```

4.*提交表单*

`JavaScript`可以以两种方式来处理表单的提交（`AJAX`方式在后面章节介绍）。

方式一是通过`<form>`元素的`submit()`方法提交一个表单，例如，响应一个`<button>`的`click`事件，在JavaScript代码中提交表单.这种方式的缺点是扰乱了浏览器对`form`的正常提交。

```js
<!-- HTML -->
<form id="test-form">
  <input type="text" name="test">
  <button type="button" onclick="doSubmitForm()">Submit</button>
</form>

<script>
function doSubmitForm() {
  var form = document.getElementById('test-form');
  // 可以在此修改form的input...
  // 提交form:
  form.submit();
}
</script>
```

浏览器默认点击`<button type="submit">`时提交表单，或者用户在最后一个输入框按回车键。因此，第二种方式是响应`<form>`本身的`onsubmit`事件，在提交`form`时作修改：**注意要return true来告诉浏览器继续提交，如果return false，浏览器将不会继续提交form，这种情况通常对应用户输入有误，提示用户错误信息后终止提交form。**

```js
<!-- HTML -->
<form id="test-form" onsubmit="return checkForm()">
  <input type="text" name="test">
  <button type="submit">Submit</button>
</form>

<script>
function checkForm() {
  var form = document.getElementById('test-form');
  // 可以在此修改form的input...
  // 继续下一步:
  return true;
}
</script>
```

表单提交利用`hidden`完成加密的方案：

**注意到id为md5-password的`<input>`标记了`name="password"`，而用户输入的`id`为`input-password`的`<input>`没有`name`属性。没有`name`属性的`<input>`的数据不会被提交。**

```js
<!-- HTML -->
<form id="login-form" method="post" onsubmit="return checkForm()">
  <input type="text" id="username" name="username">
  <input type="password" id="input-password">
  <input type="hidden" id="md5-password" name="password">
  <button type="submit">Submit</button>
</form>

<script>
function checkForm() {
  var input_pwd = document.getElementById('input-password');
  var md5_pwd = document.getElementById('md5-password');
  // 把用户输入的明文变为MD5:
  md5_pwd.value = toMD5(input_pwd.value);
  // 继续下一步:
  return true;
}
</script>
```

### 操作文件

在HTML表单中，可以上传文件的唯一控件就是`<input type="file">`。

**`注意`：当一个表单包含`<input type="file">`时，表单的`enctype`必须指定为`multipart/form-data`，`method`必须指定为`post`，浏览器才能正确编码并以`multipart/form-data`格式发送表单的数据。出于安全考虑，浏览器只允许用户点击`<input type="file">`来选择本地文件，用JavaScript对`<input type="file">`的`value`赋值是没有任何效果的。当用户选择了上传某个文件后，`JavaScript`也无法获得该文件的真实路径。**

通常，上传的文件都由后台服务器处理，JavaScript可以在提交表单时对文件扩展名做检查，以便防止用户上传无效格式的文件：

```js
var f = document.getElementById('test-file-upload');
var filename = f.value; // 'C:\fakepath\test.png'
if (!filename || !(filename.endsWith('.jpg') || filename.endsWith('.png') || filename.endsWith('.gif'))) {
  alert('Can only upload image file.');
  return false;
}
```

1.*File API*

HTML5的File API提供了File和FileReader两个主要对象，可以获得文件信息并读取文件。

```js
var
  fileInput = document.getElementById('test-image-file'),
  info = document.getElementById('test-file-info'),
  preview = document.getElementById('test-image-preview');
// 监听change事件:
fileInput.addEventListener('change', function () {
  // 清除背景图片:
  preview.style.backgroundImage = '';
  // 检查文件是否选择:
  if (!fileInput.value) {
    info.innerHTML = '没有选择文件';
    return;
  }
  // 获取File引用:
  var file = fileInput.files[0];
  // 获取File信息:
  info.innerHTML = '文件: ' + file.name + '<br>' +
           '大小: ' + file.size + '<br>' +
           '修改: ' + file.lastModifiedDate;
  if (file.type !== 'image/jpeg' && file.type !== 'image/png' && file.type !== 'image/gif') {
    alert('不是有效的图片文件!');
    return;
  }
  // 读取文件:
  var reader = new FileReader();
  reader.onload = function(e) {
    var
      data = e.target.result; // 'data:image/jpeg;base64,/9j/4AAQSk...(base64编码)...'
    preview.style.backgroundImage = 'url(' + data + ')';
  };
  // 以DataURL的形式读取文件:
  reader.readAsDataURL(file);
});
```

- 上面的代码演示了如何通过`HTML5`的`File API`读取文件内容。以`DataURL`的形式读取到的文件是一个字符串，类似于`data:image/jpeg;base64,/9j/4AAQSk...(base64编码)...`，常用于设置图像。如果需要服务器端处理，把字符串`base64`,后面的字符发送给服务器并用`Base64`解码就可以得到原始文件的二进制内容。

- 上面的代码还演示了JavaScript的一个重要的特性就是单线程执行模式.在JavaScript中，浏览器的JavaScript执行引擎在执行JavaScript代码时，总是以单线程模式执行，也就是说，任何时候，JavaScript代码都不可能同时有多于1个线程在执行。

2.*回调*

在JavaScript中，执行多任务实际上都是异步调用，比如上面的代码：`reader.readAsDataURL(file);` 就会发起一个异步操作来读取文件内容。因为是异步操作，所以我们在JavaScript代码中就不知道什么时候操作结束，因此需要先设置一个回调函数：`reader.onload = function(e) {// 当文件读取完成后，自动调用此函数:};` 当文件读取完成后，JavaScript引擎将自动调用我们设置的回调函数。执行回调函数时，文件已经读取完毕，所以我们可以在回调函数内部安全地获得文件内容。

### AJAX

> AJAX不是JavaScript的规范，它只是一个哥们“发明”的缩写：Asynchronous JavaScript and XML，意思就是用JavaScript执行异步网络请求。

如果仔细观察一个Form的提交，你就会发现，一旦用户点击“Submit”按钮，表单开始提交，浏览器就会刷新页面，然后在新页面里告诉你操作是成功了还是失败了。如果不幸由于网络太慢或者其他原因，就会得到一个404页面。

- **这就是Web的运作原理：一次HTTP请求对应一个页面。**

> 如果要让用户留在当前页面中，同时发出新的HTTP请求，就必须用JavaScript发送这个新请求，接收到数据后，再用JavaScript更新页面，这样一来，用户就感觉自己仍然停留在当前页面，但是数据却可以不断地更新。
用JavaScript写一个完整的AJAX代码并不复杂，但是需要注意：AJAX请求是异步执行的，也就是说，要通过回调函数获得响应。

在现代浏览器上写AJAX主要依靠XMLHttpRequest对象：

```js
'use strict';
function success(text) {
  var textarea = document.getElementById('test-response-text');
  textarea.value = text;
}

function fail(code) {
  var textarea = document.getElementById('test-response-text');
  textarea.value = 'Error code: ' + code;
}

var request = new XMLHttpRequest(); // 新建XMLHttpRequest对象

request.onreadystatechange = function () { // 状态发生变化时，函数被回调
  if (request.readyState === 4) { // 成功完成
    // 判断响应结果:
    if (request.status === 200) {
      // 成功，通过responseText拿到响应的文本:
      return success(request.responseText);
    } else {
      // 失败，根据响应码判断失败原因:
      return fail(request.status);
    }
  } else {
    // HTTP请求还在继续...
  }
}

// 发送请求:
request.open('GET', '/api/categories');
request.send();

alert('请求已发送，请等待响应...');
```

> Asynchronous JavaScript and XML：意思就是用JavaScript执行异步网络请求。
如果你想把标准写法和IE写法混在一起，可以这么写：

 ```js
 var request;
if (window.XMLHttpRequest) {
  request = new XMLHttpRequest();
} else {
  request = new ActiveXObject('Microsoft.XMLHTTP');
}
 ```

 通过检测`window`对象是否有`XMLHttpRequest`属性来确定浏览器是否支持标准的`XMLHttpRequest`。注意，不要根据浏览器的`navigator.userAgent`来检测浏览器是否支持某个`JavaScript`特性，一是因为这个字符串本身可以伪造，二是通过IE版本判断`JavaScript`特性将非常复杂。

 当创建了`XMLHttpRequest`对象后，要先设置`onreadystatechange`的回调函数。在回调函数中，通常我们只需通过`readyState === 4`判断请求是否完成，如果已完成，再根据`status === 200`判断是否是一个成功的响应。

`XMLHttpRequest`对象的`open()`方法有3个参数，第一个参数指定是`GET`还是`POST`，第二个参数指定`URL`地址，第三个参数指定是否使用异步，默认是`true`，所以不用写。

注意，千万不要把第三个参数指定为`false`，否则浏览器将停止响应，直到`AJAX`请求完成。如果这个请求耗时10秒，那么10秒内你会发现浏览器处于“假死”状态。

最后调用`send()`方法才真正发送请求。`GET`请求不需要参数，`POST`请求需要把`body`部分以字符串或者`FormData`对象传进去。

#### 安全限制

[安全限制](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434499861493e7c35be5e0864769a2c06afb4754acc6000)

> **默认情况下，JavaScript在发送AJAX请求时，URL的域名必须和当前页面完全一致。**
>>完全一致的意思是，域名要相同（www.example.com和example.com不同），协议要相同（http和https不同），端口号要相同（默认是:80端口，它和:8080就不同）。有的浏览器口子松一点，允许端口不同，大多数浏览器都会严格遵守这个限制。

1. 第三种方式称为JSONP，它有个限制，只能用GET请求，并且要求返回JavaScript。这种方式跨域实际上是利用了浏览器允许跨域引用JavaScript资源
2. JSONP通常以函数调用的形式返回
3. 这样一来，我们如果在页面中先准备好foo()函数，然后给页面动态加一个`<script>`节点，相当于动态读取外域的JavaScript资源，最后就等着接收回调了。
4. 因此我们需要首先在页面中准备好回调函数
5. 最后用getPrice()函数触发：

```html 1
<html>
<head>
  <script src="http://example.com/abc.js"></script>
  ...
</head>
<body>
...
</body>
</html>
```

```js
//2
foo('data');
//3
refreshPrice({"0000001":{"code": "0000001", ... });
//4
function refreshPrice(data) {
  var p = document.getElementById('test-jsonp');
  p.innerHTML = '当前价格：' +
    data['0000001'].name +': ' +
    data['0000001'].price + '；' +
    data['1399001'].name + ': ' +
    data['1399001'].price;
}
//5
function getPrice() {
  var
    js = document.createElement('script'),
    head = document.getElementsByTagName('head')[0];
  js.src = 'http://api.money.126.net/data/feed/0000001,1399001?callback=refreshPrice';
  head.appendChild(js);
}
```

#### CORS

[CORS](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434499861493e7c35be5e0864769a2c06afb4754acc6000)

如果浏览器支持HTML5，那么就可以一劳永逸地使用新的跨域策略：CORS了。

CORS全称Cross-Origin Resource Sharing，是HTML5规范定义的如何跨域访问资源。

Origin表示本域，也就是浏览器当前页面的域。当JavaScript向外域（如sina.com）发起请求后，浏览器收到响应后，首先检查`Access-Control-Allow-Origin`是否包含本域，如果是，则此次跨域请求成功，如果不是，则请求失败，JavaScript将无法获取到响应的任何数据。

![cors](../../pic/cors.png)

假设本域是my.com，外域是sina.com，只要响应头`Access-Control-Allow-Origin`为`http://my.com`，或者是`*`，本次请求就可以成功。

可见，跨域能否成功，取决于对方服务器是否愿意给你设置一个正确的`Access-Control-Allow-Origin`，决定权始终在对方手中。

上面这种跨域请求，称之为“简单请求”。简单请求包括`GET`、`HEAD`和`POST`（POST的`Content-Type`类型
仅限`application/x-www-form-urlencoded、multipart/form-data和text/plain`），并且不能出现任何自定义头（例如，X-Custom: 12345），通常能满足90%的需求。

> 无论你是否需要用JavaScript通过CORS跨域请求资源，你都要了解CORS的原理。最新的浏览器全面支持HTML5。在引用外域资源时，除了JavaScript和CSS外，都要验证CORS。
>>如果该CDN服务商未正确设置Access-Control-Allow-Origin，那么浏览器无法加载字体资源。对于PUT、DELETE以及其他类型如application/json的POST请求，在发送AJAX请求之前，浏览器会先发送一个OPTIONS请求（称为preflighted请求）到这个URL上，询问目标服务器是否接受。
>>
>>服务器必须响应并明确指出允许的Method
>>
>>浏览器确认服务器响应的Access-Control-Allow-Methods头确实包含将要发送的AJAX请求的Method，才会继续发送AJAX，否则，抛出一个错误。由于以POST、PUT方式传送JSON格式的数据在REST中很常见，所以要跨域正确处理POST和PUT请求，服务器端必须正确响应OPTIONS请求。需要深入了解CORS的童鞋请移步[W3C文档](https://www.w3.org/TR/cors/)。

### Promise

在JavaScript的世界中，所有代码都是单线程执行的。

古人云：“君子一诺千金”，这种“承诺将来会执行”的对象在JavaScript中称为Promise对象。

我们先看一个最简单的Promise例子：生成一个0-2之间的随机数，如果小于1，则等待一段时间后返回成功，否则返回失败

```js
function test(resolve, reject) {
  var timeOut = Math.random() * 2;
  log('set timeout to: ' + timeOut + ' seconds.');
  setTimeout(function () {
    if (timeOut < 1) {
      log('call resolve()...');
      resolve('200 OK');
    }
    else {
      log('call reject()...');
      reject('timeout in ' + timeOut + ' seconds.');
    }
  }, timeOut * 1000);
}
```

这个`test()`函数有两个参数，这两个参数都是函数，如果执行成功，我们将调用`resolve('200 OK')`，如果执行失败，我们将调用`reject('timeout in ' + timeOut + ' seconds.')`。可以看出，test()函数只关心自身的逻辑，并不关心具体的`resolve`和`reject`将如何处理结果。

有了执行函数，我们就可以用一个Promise对象来执行它，并在将来某个时刻获得成功或失败的结果:

```js
var p1 = new Promise(test);
var p2 = p1.then(function (result) {
  console.log('成功：' + result);
});
var p3 = p2.catch(function (reason) {
  console.log('失败：' + reason);
});
```

Promise对象可以串联起来，所以上述代码可以简化为：

```js
new Promise(test).then(function (result) {
  console.log('成功：' + result);
}).catch(function (reason) {
  console.log('失败：' + reason);
});
```

实际测试一下，看看Promise是如何异步执行的：

```js
'use strict';

// 清除log:
var logging = document.getElementById('test-promise-log');
while (logging.children.length > 1) {
  logging.removeChild(logging.children[logging.children.length - 1]);
}

// 输出log到页面:
function log(s) {
  var p = document.createElement('p');
  p.innerHTML = s;
  logging.appendChild(p);
}
new Promise(function (resolve, reject) {
  log('start new Promise...');
  var timeOut = Math.random() * 2;
  log('set timeout to: ' + timeOut + ' seconds.');
  setTimeout(function () {
    if (timeOut < 1) {
      log('call resolve()...');
      resolve('200 OK');
    }
    else {
      log('call reject()...');
      reject('timeout in ' + timeOut + ' seconds.');
    }
  }, timeOut * 1000);
}).then(function (r) {
  log('Done: ' + r);
}).catch(function (reason) {
  log('Failed: ' + reason);
});
```

```txt
Log:

start new Promise...

set timeout to: 1.8571884388119746 seconds.

call reject()...

Failed: timeout in 1.8571884388119746 seconds.
```

可见Promise最大的好处是在异步执行的流程中，把执行代码和处理结果的代码清晰地分离了：

![promise](../../pic/promise_1.png)

Promise还可以做更多的事情，比如，有若干个异步任务，需要先做任务1，如果成功后再做任务2，任何任务失败则不再继续并执行错误处理函数。

要串行执行这样的异步任务，不用Promise需要写一层一层的嵌套代码。有了Promise，我们只需要简单地写：
>`job1.then(job2).then(job3).catch(handleError);`
其中，job1、job2和job3都是Promise对象。

- 下面的例子演示了如何串行执行一系列需要异步计算获得结果的任务：

```js
'use strict';

var logging = document.getElementById('test-promise2-log');
while (logging.children.length > 1) {
  logging.removeChild(logging.children[logging.children.length - 1]);
}

function log(s) {
  var p = document.createElement('p');
  p.innerHTML = s;
  logging.appendChild(p);
}
// 0.5秒后返回input*input的计算结果:
function multiply(input) {
  return new Promise(function (resolve, reject) {
    log('calculating ' + input + ' x ' + input + '...');
    setTimeout(resolve, 500, input * input);
  });
}

// 0.5秒后返回input+input的计算结果:
function add(input) {
  return new Promise(function (resolve, reject) {
    log('calculating ' + input + ' + ' + input + '...');
    setTimeout(resolve, 500, input + input);
  });
}

var p = new Promise(function (resolve, reject) {
  log('start new Promise...');
  resolve(123);
});

p.then(multiply)
 .then(add)
 .then(multiply)
 .then(add)
 .then(function (result) {
  log('Got value: ' + result);
});
```

- `setTimeout`可以看成一个模拟网络等异步执行的函数。现在，我们把上一节的AJAX异步执行函数转换为Promise对象，看看用Promise如何简化异步处理：

```js
'use strict';

// ajax函数将返回Promise对象:
function ajax(method, url, data) {
  var request = new XMLHttpRequest();
  return new Promise(function (resolve, reject) {
    request.onreadystatechange = function () {
      if (request.readyState === 4) {
        if (request.status === 200) {
          resolve(request.responseText);
        } else {
          reject(request.status);
        }
      }
    };
    request.open(method, url);
    request.send(data);
  });
}
var log = document.getElementById('test-promise-ajax-result');
var p = ajax('GET', '/api/categories');
p.then(function (text) { // 如果AJAX成功，获得响应内容
  log.innerText = text;
}).catch(function (status) { // 如果AJAX失败，获得响应代码
  log.innerText = 'ERROR: ' + status;
});
```

有些时候，多个异步任务是为了容错。比如，同时向两个URL读取用户的个人信息，只需要获得先返回的结果即可。这种情况下，用`Promise.race()`实现：

```js
var p1 = new Promise(function (resolve, reject) {
  setTimeout(resolve, 500, 'P1');
});
var p2 = new Promise(function (resolve, reject) {
  setTimeout(resolve, 600, 'P2');
});
Promise.race([p1, p2]).then(function (result) {
  console.log(result); // 'P1'
});
```

由于p1执行较快，Promise的then()将获得结果'P1'。p2仍在继续执行，但执行结果将被丢弃。

- **如果我们组合使用Promise，就可以把很多异步任务以并行和串行的方式组合起来执行。**

### Canvas

[Canvas](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/00143449990549914b596ac1da54a228a6fa9643e88bc0c000)

Canvas是HTML5新增的组件，它就像一块幕布，可以用JavaScript在上面绘制各种图表、动画等。

没有Canvas的年代，绘图只能借助Flash插件实现，页面不得不用JavaScript和Flash进行交互。有了Canvas，我们就再也不需要Flash了，直接使用JavaScript完成绘制。

一个Canvas定义了一个指定尺寸的矩形框，在这个范围内我们可以随意绘制：`<canvas id="test-canvas" width="300" height="200"></canvas>`

由于浏览器对HTML5标准支持不一致，所以，通常在`<canvas>`内部添加一些说明性HTML代码，如果浏览器支持Canvas，它将忽略`<canvas>`内部的HTML，如果浏览器不支持Canvas，它将显示`<canvas>`内部的HTML：

```html
<canvas id="test-stock" width="300" height="200">
  <p>Current Price: 25.51</p>
</canvas>

<!-- HTML代码 -->
<canvas id="test-canvas" width="200" heigth="100">
  <p>你的浏览器不支持Canvas</p>
</canvas>
```

在使用Canvas前，用`canvas.getContext`来测试浏览器是否支持Canvas

```js
var canvas = document.getElementById('test-canvas');
if (canvas.getContext) {
  console.log('你的浏览器支持Canvas!');
} else {
  console.log('你的浏览器不支持Canvas!');
}
```

## jQuery

你可能听说过jQuery，它名字起得很土，但却是JavaScript世界中使用最广泛的一个库。

jQuery这么流行，肯定是因为它解决了一些很重要的问题。实际上，jQuery能帮我们干这些事情：

- 消除浏览器差异：你不需要自己写冗长的代码来针对不同的浏览器来绑定事件，编写AJAX等代码；

- 简洁的操作DOM的方法：写$('#test')肯定比document.getElementById('test')来得简洁；

- 轻松实现动画、修改CSS等各种操作。

1. jQuery版本

    目前[jQuery](http://jquery.com/download/)有1.x和2.x两个主要版本，区别在于2.x移除了对古老的IE 6、7、8的支持，因此2.x的代码更精简。选择哪个版本主要取决于你是否想支持IE 6~8。

    从jQuery官网可以下载最新版本。jQuery只是一个jquery-xxx.js文件，但你会看到有compressed（已压缩）和uncompressed（未压缩）两种版本，使用时完全一样，但如果你想深入研究jQuery源码，那就用uncompressed版本。

2. 使用jQuery

    `$`符号
    >`$`是著名的jQuery符号。实际上，`jQuery`把所有功能全部封装在一个全局变量`jQuery`中，而`$`也是一个合法的变量名，它是变量`jQuery`的别名：

    `$`本质上就是一个函数，但是函数也是对象，于是$除了可以直接调用外，也可以有很多其他属性。

    >*注意*，你看到的$函数名可能不是`jQuery(selector, context)`，因为很多JavaScript压缩工具可以对函数名和参数改名，所以压缩过的jQuery源码$函数可能变成a(b, c)。

    绝大多数时候，我们都直接用$（因为写起来更简单嘛）。但是，如果$这个变量不幸地被占用了，而且还不能改，那我们就只能让jQuery把$变量交出来，然后就只能使用jQuery这个变量：

    ```JS
    $; // jQuery(selector, context)
    jQuery.noConflict();
    $; // undefined
    jQuery; // jQuery(selector, context)
    ```

  这种黑魔法的原理是jQuery在占用$之前，先在内部保存了原来的$,调用jQuery.noConflict()时会把原来保存的变量还原。

### 选择器

选择器是jQuery的核心。一个选择器写出来类似$('#dom-id')。
如果id为abc的`<div>`不存在，返回的jQuery对象如下：`[]`
总之jQuery的选择器不会返回`undefined`或者`null`，这样的好处是你不必在下一行判断`if (div === undefined)`。

```js
var div = $('#abc'); // jQuery对象
var divDom = div.get(0); // 假设存在div，获取第1个DOM元素
var another = $(divDom); // 重新把DOM包装为jQuery对象
```

通常情况下你不需要获取DOM对象，直接使用`jQuery`对象更加方便。如果你拿到了一个`DOM`对象，那可以简单地调用`$(aDomObject)`把它变成`jQuery`对象，这样就可以方便地使用`jQuery`的`API`了。

按tag查找:`var ps = $('p'); // 返回所有<p>节点`

按class查找:

```js
var a = $('.red'); // 所有节点包含`class="red"`都将返回
// 例如:
// <div class="red">...</div>
// <p class="green red">...</p>
var a = $('.red.green'); // 注意没有空格！
// 符合条件的节点：
// <div class="red green">...</div>
// <div class="blue green red">...</div>
```

按属性查找:一个DOM节点除了id和class外还可以有很多属性，很多时候按属性查找会非常方便，比如在一个表单中按属性来查找

```js
var email = $('[name=email]'); // 找出<??? name="email">
var passwordInput = $('[type=password]'); // 找出<??? type="password">
var a = $('[items="A B"]'); // 找出<??? items="A B">

//当属性的值包含空格等特殊字符时，需要用双引号括起来。
//按属性查找还可以使用前缀查找或者后缀查找：
var icons = $('[name^=icon]'); // 找出所有name属性值以icon开头的DOM
// 例如: name="icon-1", name="icon-2"
var names = $('[name$=with]'); // 找出所有name属性值以with结尾的DOM
// 例如: name="startswith", name="endswith"

//这个方法尤其适合通过class属性查找，且不受class包含多个名称的影响：
var icons = $('[class^="icon-"]'); // 找出所有class包含至少一个以`icon-`开头的DOM
// 例如: class="icon-clock", class="abc icon-home"
```

组合查找:组合查找就是把上述简单选择器组合起来使用。如果我们查找`$('[name=email]')`，很可能把表单外的`<div name="email">`也找出来，但我们只希望查找`<input>`，就可以这么写：

```js
var emailInput = $('input[name=email]'); // 不会找出<div name="email">  
var tr = $('tr.red'); // 找出<tr class="red ...">...</tr>
```

多项选择器：多项选择器就是把多个选择器用`,`组合起来一块选:*要注意的是，选出来的元素是按照它们在HTML中出现的顺序排列的，而且不会有重复元素。例如，`<p class="red green">`不会被上面的`$('p.red,p.green')`选择两次。*

```js
$('p,div'); // 把<p>和<div>都选出来
$('p.red,p.green'); // 把<p class="red">和<p class="green">都选出来
```

练习：选择邮件和名字input

```html
<!-- HTML结构 -->
<div id="test-jquery">
  <p id="para-1" class="color-red">JavaScript</p>
  <p id="para-2" class="color-green">Haskell</p>
  <p class="color-red color-green">Erlang</p>
  <p name="name" class="color-black">Python</p>
  <form class="test-form" target="_blank" action="#0" onsubmit="return false;">
    <legend>注册新用户</legend>
    <fieldset>
      <p><label>名字: <input name="name"></label></p>
      <p><label>邮件: <input name="email"></label></p>
      <p><label>口令: <input name="password" type="password"></label></p>
      <p><button type="submit">注册</button></p>
    </fieldset>
  </form>
</div>
```

```js
'use strict';
selected = $('input[name=name],input[name=email]');
// 高亮结果:
if (!(selected instanceof jQuery)) {
  return console.log('不是有效的jQuery对象!');
}
$('#test-jquery').find('*').css('background-color', '');
selected.css('background-color', '#ffd351');
```

#### 层级选择器

[层级选择器](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001437023139167510b90eb2c924f72aeba0db592a9eb54000)

表单相关
针对表单元素，jQuery还有一组特殊的选择器：

- `:input`：可以选择`<input>，<textarea>，<select>和<button>`；

- `:file`：可以选择`<input type="file">`，和input[type=file]一样；

- `:checkbox`：可以选择复选框，和`input[type=checkbox]`一样；

- `:radio`：可以选择单选框，和`input[type=radio]`一样；

- `:focus`：可以选择当前输入焦点的元素，例如把光标放到一个`<input>`上，用`$('input:focus')`就可以选出；

- `:checked`：选择当前勾上的单选框和复选框，用这个选择器可以立刻获得用户选择的项目，如`$('input[type=radio]:checked')`；

- `:enabled`：可以选择可以正常输入的`<input>、<select>`等，也就是没有灰掉的输入；

- `:disabled`：和:enabled正好相反，选择那些不能输入的。

#### 查找和过滤

- `find()`:`var hsk = ul.find('[name=haskell]'); // 获得Haskell`
- `next()`:`swift.next('[name=haskell]');// 空的jQuery对象，因为Swift的下一个元素Scheme不符合条件[name=haskell]`
- `prev()`:`swift.prev('.dy'); // Python，因为Python同时符合过滤器条件.dy`
- `filter()`:

```js
var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
langs.filter(function () {
  return this.innerHTML.indexOf('S') === 0; // 返回S开头的节点
}); // 拿到Swift, Scheme
```

- `map()`:

```js
var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
var arr = langs.map(function () {
  return this.innerHTML;
}).get(); // 用get()拿到包含string的Array：['JavaScript', 'Python', 'Swift', 'Scheme', 'Haskell']
//此外，一个jQuery对象如果包含了不止一个DOM节点，first()、last()和slice()方法可以返回一个新的jQuery对象，把不需要的DOM节点去掉：
var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
var js = langs.first(); // JavaScript，相当于$('ul.lang li:first-child')
var haskell = langs.last(); // Haskell, 相当于$('ul.lang li:last-child')
var sub = langs.slice(2, 4); // Swift, Scheme, 参数和数组的slice()方法一致
```

练习

```html
<form id="test-form" action="#0" onsubmit="return false;">
  <p><label>Name: <input name="name"></label></p>
  <p><label>Email: <input name="email"></label></p>
  <p><label>Password: <input name="password" type="password"></label></p>
  <p>Gender: <label><input name="gender" type="radio" value="m" checked> Male</label> <label><input name="gender" type="radio" value="f"> Female</label></p>
  <p><label>City: <select name="city">
    <option value="BJ" selected>Beijing</option>
    <option value="SH">Shanghai</option>
    <option value="CD">Chengdu</option>
    <option value="XM">Xiamen</option>
  </select></label></p>
  <p><button type="submit">Submit</button></p>
</form>
```

输入值后，用`jQuery`获取表单的JSON字符串，`key`和`value`分别对应每个输入的`name`和相应的`value`，例如：`{"name":"Michael","email":...}`

```js
'use strict';
var json = null;
var obj = {
  name: $('[name=name]').val(),
  email: $('[name=email]').val(),
  password: $('[name=password]').val(),
  gender: $('[name = gender]').filter(function () {
    return this.checked === true;
  }).val(),
  city: $('form#test-form select').val()
}
json = JSON.stringify(obj);
// 显示结果:
if (typeof (json) === 'string') {
  console.log(json);
} else {
  console.log('json变量不是string!');
}
```

---
[`Babel`]:https://babeljs.io/
[浏览器]:https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/0014344997647015f03abc1bb5f46129a7526292a12ab26000
[JSON]:https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434499490767fe5a0e31e17e44b69dcd1196f7ec6fc6000
[RegExp]:https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434499503920bb7b42ff6627420da2ceae4babf6c4f2000
[函数]:https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/00143449926746982f181557d9b423f819e89709feabdb4000
[解构赋值]:https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/0014344993159773a464f34e1724700a6d5dd9e235ceb7c000
[文献]:https://blog.csdn.net/u010359965/article/details/49795213
[测试失败]:https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001435119854495d29b9b3d7028477a96ed74db95032675000
[console.log]:https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434499203693072018f8878842a9b0011e3ff4e38b6b000
[练习]:./js_lab/filter.js
[filter]:https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/0014351226817991a9c08f1ec0a45c99b9209bcfc71b8f6000
[箭头函数]:https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001438565969057627e5435793645b7acaee3b6869d1374000