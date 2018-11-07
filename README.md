# 日记

用md写一些简单的笔记，同时这个是一个简单的实验室，用来实验一些我觉得有意思的东西。

## 备忘录

- [javascript](###javascript)
- [vue](###vue)
- [md using](###md_using)
- [翻墙](###翻墙)

### javascript-廖雪峰

>这部分以后会陆续整理出来一个目录

<!-- TOC -->

- [日记](#日记)
    - [备忘录](#备忘录)
        - [javascript-廖雪峰](#javascript-廖雪峰)
        - [vue-vue官网](#vue-vue官网)
            - [问题](#问题)
            - [总结](#总结)
            - [目录](#目录)
        - [md_using](#md_using)
        - [翻墙](#翻墙)
        - [[tumblr](https://www.tumblr.com/getting_to_know_tumblr/)](#tumblrhttpswwwtumblrcomgetting_to_know_tumblr)
    - [自建小工具业务](#自建小工具业务)
    - [node.js bug and deal](#nodejs-bug-and-deal)
    - [powershell](#powershell)
        - [别名配置](#别名配置)

<!-- /TOC -->

### vue-vue官网 

这部分以后会陆续整理出来一个目录

#### 问题

每个vue在html页面中的模块，都需要一个vue的实例来对应吗？

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

[开始](./2018·8·23.md)

[结束](./)

### md_using

- [表格和列表](./2018·8·3.md/##[md]使用规则)
- [空格和链接](./2018·8·7.md/##md的使用)
- [图片标题](./2018·8·10.md/##md用法)
- [Email链接和代码块](./2018·8·30.md/##md_using)

### 翻墙

翻墙服务地址:<https://agentneo.rocks/>

配合使用：[ShadowsocksR-4.7.0-win](./files/ShadowsocksR-4.7.0-win.7z)

### [tumblr](https://www.tumblr.com/getting_to_know_tumblr/)

163邮箱：<0308>:G**80*******

harry potter

---

## 自建小工具业务

- 字母的大小写转变
- 截取身份证号，添加英文逗号和引号（去掉空格，添加英文逗号和引号）
- 任务列表，添加每日更新列表
- 笔记功能（日记）
- md文件转换为html文件并展示

## node.js bug and deal

- Couldn't find preset "es2015" relative to directory

> npm install --save-dev babel-preset-es2015

## powershell

- [学习笔记](files\createDariy.ps1)

### 别名配置

首次使用请运行
> Set-Alias cDariy .\createDariy.ps1
其余运行
> cDariy