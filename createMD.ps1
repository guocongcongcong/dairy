#Script End
#日期
$date = Get-Date -format 'yyyy·MM·dd'
$year = Get-Date -format 'yyyy'
$month =  Get-Date -format 'MM'

#文件名
$fileName = $date +'.md'
#当前地址
$path = Split-Path -Parent $MyInvocation.MyCommand.Definition
#文件夹
$filer = $path +'\diary\'+$year+'\' 
#文件
$file = $path +'\diary\'+$year+'\'+$month+'\' + $fileName
#$files = $path +'\diary\' + $fileName

if(Test-Path $filer){
}else{
    mkdir $filer
}
$filer = $filer+'\'+$month+'\' 
if(Test-Path $filer){
}else{
    mkdir $filer
}

if(Test-Path $file){
    "文件已存在，不重新创建"
}else{
    #引入模板地址
    $template = $path +'\diary\template.txt'
    if(Test-Path $template){
    }else{
        $temp1 = '

## 目录

<!-- TOC -->

<!-- /TOC -->

## 账目

|名称|价格|备注|
|---|---|---|

## TODO LIST

## 内容

### 

## 总结
'
        $temp1 > $template
    }
    #读取模板
    $content = Get-Content -Path $template -Raw -encoding utf8
    $content = "# "+ $date + $content 
    ## 创建文件
    $content > $file
}
$file
#Script Really End