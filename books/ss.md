# ss 的一些问题

[toc]

<!-- TOC -->

- [ss 的一些问题](#ss-的一些问题)
    - [关于换ip地址](#关于换ip地址)
    - [关于ss的操作](#关于ss的操作)
    - [原始文件](#原始文件)
        - [使用方法：](#使用方法)
        - [卸载方法：](#卸载方法)
        - [单用户配置文件 Sample](#单用户配置文件-sample)
        - [多用户多端口配置文件 Sample](#多用户多端口配置文件-sample)
        - [使用命令](#使用命令)
        - [假设服务器端口1080, 查看连接数](#假设服务器端口1080-查看连接数)
        - [查看连接列表](#查看连接列表)

<!-- /TOC -->

## 关于换ip地址

- 登陆 GoogleCloudPlatform 
- 点开 左侧菜单栏
- 找到 网络 > VPC网络 > 外部IP地址
- 点开需要修改ip地址后面的更改 
- 挂接到  > 无 > 确定
- 勾选该ip地址 点击 释放静态地址
- 修改该 ip地址为静态 名字随便写 然后 保存

## 关于ss的操作

- 登陆后 使用命令 ```> sudo -i``` 切换到 root 用户下
- 访问 ```./home/g...``` 
 > 因为shadowsocks.sh 在该文件夹下
- 如果找不到 可以使用 ``` > find / -name shadowsocks.sh```查找文件 
  - [关于查找的文档](https://blog.csdn.net/qq_37506868/article/details/79238300)
- 运行 ``` > ./shadowsocks.sh uninstall ``` 卸载
  - 猜测： 更换完ip只需要 重启就应该可以正常使用了--下次尝试 ```> /etc/init.d/shadowsocks restart ```
- 使用 ```> ./shadowsocks.sh 2>&1 | tee shadowsocks.log ``` 命令重新安装
  

## 原始文件

本脚本适用环境：
系统支持：CentOS 6，7，Debian，Ubuntu
内存要求：≥128M
日期：2017 年 07 月 28 日

关于本脚本：
一键安装 Python 版 shadowsocks 的最新版。

默认配置：
服务器端口：自己设定（如不设定，默认为 8989）
密码：自己设定（如不设定，默认为 teddysun.com）
加密方式：自己设定（如不设定，默认为 aes-256-gcm）
备注：脚本默认创建单用户配置文件，如需配置多用户，安装完毕后参照下面的教程示例手动修改配置文件后重启即可。

客户端下载：
Windows
Android

### 使用方法：
使用root用户登录，运行以下命令：

wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh
chmod +x shadowsocks.sh
./shadowsocks.sh 2>&1 | tee shadowsocks.log
安装完成后，脚本提示如下：

```s
Congratulations, shadowsocks install completed!   
Your Server IP:your_server_ip   
Your Server Port:your_server_port   
Your Password:your_password   
Your Local IP:127.0.0.1   
Your Local Port:1080   
Your Encryption Method:aes-256-cfb   

Welcome to visit:http://teddysun.com/342.html   
Enjoy it! 
```

### 卸载方法：
使用root用户登录，运行以下命令：

./shadowsocks.sh uninstall


### 单用户配置文件 Sample
配置文件路径：

```json
vi /etc/shadowsocks.json
{  
    "server":"0.0.0.0",  
    "server_port":8989,   
    "local_address":"127.0.0.1",  
    "local_port":1080,  
    "password":"yourpassword",  
    "timeout":300,  
    "method":"aes-256-cfb",  
    "fast_open": false  
}
```
### 多用户多端口配置文件 Sample
配置文件路径：

```json
vi /etc/shadowsocks.json
{  
    "server":"0.0.0.0",
    "local_address":"127.0.0.1",
    "local_port":1080,
    "port_password":{
         "8989":"password0",
         "9001":"password1",
         "9002":"password2",
         "9003":"password3",
         "9004":"password4"
    },
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
```

### 使用命令
（2015 年 08 月 28 日修正）：
启动：/etc/init.d/shadowsocks start
停止：/etc/init.d/shadowsocks stop
重启：/etc/init.d/shadowsocks restart
状态：/etc/init.d/shadowsocks status
写入自启echo "ssserver -c /etc/shadowsocks.json -d restart" >> /etc/rc.local
查看日志less /var/log/shadowsocks.log

说明： 从 Shadowsocks 2.6 开始，你可以直接在后台运行 Shadowsocks，无需 Supervisor 。 这样省掉了 Supervisor 进程占用的内存。

ssserver -c /etc/shadowsocks.json -d start
ssserver -c /etc/shadowsocks.json -d stop
ssserver -c /etc/shadowsocks.json -d restart
查看连接的人数

Ubuntu:apt-get install lsof -y
CentOs:yum install lsof -y

### 假设服务器端口1080, 查看连接数
sudo lsof -i -n -P | egrep -c ':1080.+ESTABLISHED'

### 查看连接列表
sudo lsof -i -n -P | egrep ':1080.+ESTABLISHED'

利用脚本查看连接列表，并添加定时任务
新建目录mkdir test里添加以下脚本

```cmd
#!/bin/bash
#
# File: port-ip-monitor.sh
#
# Created: Wednesday, August 27 2014 by Hua Liang[Stupid ET] <et@everet.org>
#

filename="port-ip-monitor.log"
regex="8888"  # monitor 你的端口

date +"[%Y-%m-%d %H:%M:%S]" >> $filename
netstat -anp | egrep $regex | grep -E "tcp.*ESTABLISHED" | awk '{print $4, $5}' | cut -d: -f2 | sort -u >> $filename
```

编辑crontab -e里增加* * * * * (cd /test/ && bash port-ip-monitor.sh)
启动服务service crond start
然后我们在/test/里就看到port-ip-monitor.log了
查看日志less /test/port-ip-monitor.log

参考链接：
https://shadowsocks.be/1.html
http://everet.org/shadowsocks.html


