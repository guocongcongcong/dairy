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

