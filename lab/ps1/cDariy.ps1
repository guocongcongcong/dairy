#Script End
#日期
$date = Get-Date -format 'yyyy·MM·dd'
$year = Get-Date -format 'yyyy'
#文件名
$fileName = $date +'.md'
#当前地址
$path = Split-Path -Parent $MyInvocation.MyCommand.Definition
#文件夹
$filer = $path +'\dairy\'+$year+'\' 
#文件
$file = $path +'\dairy\'+$year+'\' + $fileName
#$files = $path +'\dairy\' + $fileName

if(Test-Path $filer){
}else{
    mkdir $filer
}

if(Test-Path $file){
    "文件已存在，不重新创建"
}else{
    #引入模板地址
    $template = $path +'\dairy\template.txt'
    #读取模板
    $content = Get-Content -Path $template -Raw -encoding utf8
    $content = "# "+ $date + $content 
    ## 创建文件
    $content > $file
}
$file
#Script Really End


