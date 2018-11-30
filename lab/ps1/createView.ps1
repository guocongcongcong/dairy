#表名
$tableName = "social_compensation"
$rowName = "SOCIAL_COMPENSATION"
#处理sql
$sql ="CREATE OR REPLACE VIEW view_{tableName}
AS
SELECT personal_id, WM_CONCAT({rowName}) AS {rowName}
FROM zxdc_{tableName}
GROUP BY personal_id;" -replace "{tableName}",$tableName   -replace "{rowName}",$rowName
$fileName = ".\create_{tableName}_view.sql" -replace "{tableName}",$tableName
$sql > $fileName
Notepad $fileName
