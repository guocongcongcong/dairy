#表名
$tableName = "zxdc_eco_house"
#处理sql
$sql ="delete from {tableName} t
 where t.worker_social_insurance = '4'
   and t.personal_id in (select personal_id
                           from {tableName}
                          where worker_social_insurance = '4'
                          group by personal_id
                         having count(personal_id) > 1)
   and uuid not in (select min(uuid)
                      from {tableName}
                     where worker_social_insurance = '4'
                     group by personal_id
                    having count(personal_id) > 1)" -replace "{tableName}",$tableName
# #当前地址
# $path = Split-Path -Parent $MyInvocation.MyCommand.Definition
# #引入模板地址
# $template = $path +'\dealwithTable.txt'
# #读取模板
# $content = Get-Content -Path $template -Raw -encoding utf8
# #替换
# $content.Replace("{tableName}",$tableName)
##错误
# $sql.Replace("{tableName}","zxdc_eco_house")
$sql > .\dealwithTable.txt