$Env:CommonProgramFils
#Script End
"start working"
"    "
# (ls).Count
# $pshome
# $home
# $profile
# # 在变量前加"$"
# # 定义变量的规则
# # 变量可以是数字 
# $123
# # -变量可以是字符串 
# $abc
# # -变量可以是特殊字符 
# ${@1b}
# # - 给变量赋值
$date = Get-Date -format 'yyyy-MM-dd'
$fileName = $date +'.md'
<#
文件：xxx.ps1
用途：用于测试的xxx功能脚本
创建：2013-03-27，jb51.net
修改：2013-09-04，jb51.net
#>
# $path = $MyInvocation.MyCommand.Definition
# $path
<#此时$x的值是当前运行中的脚本的绝对路径，再用Split-Path取它的父路径就可以了：复制代码 代码如下:#>   
$path = Split-Path -Parent $MyInvocation.MyCommand.Definition
$files = $path +'\dairy\' + $fileName
#  这样$x的值就是脚本所在的文件夹了……
## 开始试着穿件文件
"# "+$date > $files

"    "
"end working"
#Script Really End

# ```ps1
# # Test-Path，检查路径是否存在。
# # 语法：Test-Path <路径>
# # 说明：这里的路径可以是：文件、文件夹、HKLM路径、环境变量env:路径
# # 下面来举一些例子，让大家更方便懂：
# Test-Path D:\q.txt
# Test-Path C:\Scripts\Archive -pathType container
# Test-Path "HKCU:\Software\Microsoft\Driver Signing"
# Test-Path Alias:\gci
# Test-Path Env:\username
# Test-Path C:\Scripts\Archive -pathType leaf
# Test-Path C:\Scripts\Archive\*.ps1
# Test-Path C:\Scripts\Archive\* -include *.ps1, *.vbs
# Test-Path C:\Scripts\Archive\* -include Test*.ps1, Test*.vbs
# Test-Path C:\Scripts\Archive\* -exclude *.ps1
# Test-Path C:\Scripts\Archive\* -exclude *.gif, *.jpg
# ```

# ```ps1
# Powershell常用命令
# 1.Get-Command 得到Powshell所有命令
# 2.Get-Process 获取所有迚程
# 3.Set-Alias 给指定命令重命名 如:Set-Alias aaa Get-Command
# 4.Set-ExecutionPolicy remotesigned 设置powershell可直接执行脚本文件 一般脚本文件以.ps1结尾    执行脚本文件直接输入文件地址即可执行 脚本文件中叧写命令即可
# 5.Get-Help get-* 查询以get开头的命令 Get-Help *service* Get-Help Get-Command 获取Get-Command命令的基本用法
# 6.Get-Member 获取对象属性 如: $var | Get-Memeber 访问$var属性 直接$var.ToString()PS中的变量定义
# 不需要定义或声明数据类型
# 在变量前加"$"
# 定义变量的规则
# -变量可以是数字 $123
# -变量可以是字符串 $abc
# -变量可以是特殊字符 ${@1b}
# 内置的变量
# -$pshome
# -$home
# -$profile
# 变量赋值: $var=123 $var="aaaaaa"
# 取变量值: $var
# 变量赋值方法:Set-Variable var 100
# 取值方法: Get-Variable var
# 清空值: Clear-Variable var
# 删除变量 Remove-Variable var
# 取多个变量如var1 var2 var3地值: Get-Variable var*
# 另一种赋值方法 $var1="bbb" $var2="$var $var1" 结果$var2="aaaaaa bbb"
# $var2='$var $var1' 结果$var2="$var $var1"
# $date=Get-Date 获取当前时间
# $date.AddDays(3) 当前时间加3天
# 排序用法
# Get-Process | Sort-Object ws 根据WS值由小到大排序
# Get-Process | Sort-Object | fl Get-Process | Sort-Object | Format-List 以列表形式显示数据
# 注释使用
# Get-Proccess | #这里写注释信息
# sort ws
# 比较运算符
# $var="abc"
# $var -like "&b&" 返回true
# $var -clike "&b&" 返回true
# 函数使用
# 案例:在一个脚本文件中有如下代码:
# $var1=10
# function one{"The Variable is $var1"}
# function two{$var1=20;one}
# one
# two
# one
# 执行结果: The Variable is 10
# The Variable is 20
# The Variable is 10
# 此示例表明,在函数中改变变量值并不影响实际值
# 若需改变其值请看如下代码:
# $var1=10
# function one{"The Variable is $var1"}
# function two{$Script:var1=20;one}
# one
# two
# one
# 执行结果: The Variable is 10
# The Variable is 20
# The Variable is 20
# freach使用
# $var=1..6 #定义数组
# foreach($i in $var)
# {
#    $n++
#    Write-Host "$i"
# }
# Write-Host "there were $n record"
# if使用
# Get-Service | foreach{
# if($_.status -eq "running"){
#      Write-Host $_.displayname "("$_status")" -foregroundcolor "green"
# }
# else
# {
#      Write-Host $_.displayname "("$_status")" -foregroundcolor "red"
# }
# }
# error使用
# function one
# {
#    Get-Process -ea stop
#    Get-ChildItem ada -ErrorAction stop #此句有误
#    Get-Process -ErrorAction stop
# }
# one
#   -ea 定义当错误发生以后该如何继续执行
#   $?可以测试命令执行成功还是失败,成功则结果为true 反之为false
# 单步调试
# 先设置Set-PSDebug -step
# for($i=1;$i -le 10;$i++)
# {
#     Write-Host "loop number $i"
# }
# ```

# 遍历city集合并打印字符串
$city = "ChongQing", "BeiJing", "XiAn"
foreach ($c in $city)
{
    "Welcome to $c"
}