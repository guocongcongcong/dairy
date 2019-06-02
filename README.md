# 日记

用md写一些简单的笔记，同时这个是一个简单的实验室，用来实验一些我觉得有意思的东西。

## 本页目录

<!-- TOC -->

- [日记](#日记)
    - [本页目录](#本页目录)
    - [备忘录](#备忘录)
        - [成人每日所需营养物质标准](#成人每日所需营养物质标准)
        - [idea破解](#idea破解)
        - [javascript-廖雪峰](#javascript-廖雪峰)
        - [vue-vue官网](#vue-vue官网)
            - [总结](#总结)
            - [目录](#目录)
        - [md_using](#md_using)
        - [翻墙](#翻墙)
        - [tumblr](#tumblr)
        - [bolg](#bolg)
        - [读书笔记](#读书笔记)
    - [自建小工具业务](#自建小工具业务)
    - [node.js bug and deal](#nodejs-bug-and-deal)
    - [powershell](#powershell)
        - [别名配置](#别名配置)
    - [总结](#总结-1)

<!-- /TOC -->

## 备忘录

### 成人每日所需营养物质标准

[readme](./books/成人每日所需营养物质标准.md)

### idea破解

[readme](./books/idea2018.2.4破解/readme.md/#idea破解)


### javascript-廖雪峰

>这部分以后会陆续整理出来一个目录

### vue-vue官网

这部分以后会陆续整理出来一个目录
- [手摸手](https://juejin.im/post/59097cd7a22b9d0065fb61d2)


#### 总结

- vue的几种基本指令： `v-bind`、`v-on`、`v-model`、`v-if`、`v-show`和`v-for`
- vue对象的有5基本属性：`el`,`date`,`methods`,`computed`,`watch`
- vue对象中的`this`指针都是指向自己的
- vue的组件

类型|名称|说明|
-|-|-|
指令|
——|v-bind|渲染|
——|v-on|监听|
——|v-model|数据双向绑定|
——|v-if|条件显示，为false时，不创建DOM|
——|v-show|条件显示，创建DOM，但是为false时css属性为display|
——|v-for|循环|
属性|
——|el|'#id'|
——|date|数据|
——|methods|方法：处理函数|
——|computed|计算属性，与methods相比，数据不变时会读取缓存|
——|watch|侦听:键是需要观察的表达式，值是对应回调函数|

#### 目录

[开始](./dairy/2018/2018·8·23.md)

[结束](./)

### md_using

- [表格和列表](./dairy/2018/2018·8·3.md/##[md]使用规则)
- [空格和链接](./dairy/2018/2018·8·7.md/##md的使用)
- [图片标题](./dairy/2018/2018·8·10.md/##md用法)
- [Email链接和代码块](./dairy/2018/2018·8·30.md/##md_using)
- [数学公式](https://juejin.im/post/5a6721bd518825733201c4a2)

### 翻墙

翻墙服务地址:<https://agentneo.rocks/>

配合使用：[ShadowsocksR-4.7.0-win](./files/ShadowsocksR-4.7.0-win.7z)

### tumblr

[tumblr](https://www.tumblr.com/getting_to_know_tumblr/)

163邮箱：<0308>:G**80*******

harry potter

---

### bolg

- [datetimepicker--bootstrap](./books/bolg/datetimepicker--bootstrap.md)
- [deserialize+serialize](./books/bolg/deserialize+serialize.md)
- ~~[fileinput--bootstrap+自主调用](./books/bolg/fileinput--bootstrap+自主调用.md)~~
- [pug+bootstrapWizard](./books/bolg/pug+bootstrapWizard.md)
- [selectpicker+dict的自主编写](./books/bolg/selectpicker+dict的自主编写.md)

### 读书笔记

- [如何高效的学习](./books/readingNotes/如何高效的学习.md)
- [算法图解](./books/readingNotes/算法图解.md)
- [逻辑思维简单入门](./books/readingNotes/逻辑思维简单入门.md)

## 自建小工具业务

- ~~字母的大小写转变~~
- ~~截取身份证号，添加英文逗号和引号（去掉空格，添加英文逗号和引号~~
- 账本
  - 当月：（额度-剩余额度）+（额度-剩余额度）*汇率
  - 多月：当月-当月还款+必要支出（生活费+三月一次）-公积金进账（三月一次）
  - 输入
    - 开始日期
    - 信用卡 名称
    - 信用卡 额度
    - 信用卡 剩余额度
    - 套现汇率
    - 预算时间长度（六个月）/不填
    - 结束日期
    - 月还款金额（可能与上条互斥）
    - 必要支出 （间隔 金额）
    - 公积金进账 （开始日期 三月一次 一次4500）
  - 输出
    - 总金额
    - 剩余金额
    - 新增指出
    - 月份
- 任务列表，添加每日更新列表
- 笔记功能（日记）
- md文件转换为html文件并展示
- sql 修改
- js基础功能展示
- python后台处理

## node.js bug and deal

- Couldn't find preset "es2015" relative to directory

> npm install --save-dev babel-preset-es2015

## powershell

- [学习笔记](files\createDariy.ps1)

### 别名配置

[备份文件](files\createDariy.ps1)

首次使用请运行
> Set-Alias cDariy .\createDariy.ps1
>运行
> cDariy
--挂机重启后失效
---
建议使用:
> .\cDariy

- Powershell中禁止运行脚本（about_Execution_Policies）的解决方法

>powershell，右键以管理员运行
>
>set-ExecutionPolicy RemoteSigned
>
>y

- [模板地址](dairy\template.txt)

模板规则：

- 使用md文件规则
- 文件开头空两行

## 总结

[2018](books\letter\2018.md)