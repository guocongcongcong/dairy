# array
$city = "ChongQing", "BeiJing", "XiAn"
foreach ($c in $city)
{
    "Welcome to $c"
}
# list--arrayList
$path = Split-Path -Parent  $MyInvocation.MyCommand.Definition
$template = $path +'\dairy\template.txt'
$template