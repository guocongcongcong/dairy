#2018.11.30 导出河南数据
# array
$tableName = "z_hb_r0_r41_trans"
$areacode = "4112"
$sql = ""

foreach ($a in $areacode)
{
    $sql += "--$a
    select * from {table_name} t where substr(t.area_code,0,4) = '$a'"  -replace "{tableName}",$tableName 

}
$fileName = ".\2018.11.30.sql"
$sql > $fileName
Notepad $fileName