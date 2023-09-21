-- Will list all records of table second_table having a name value in my MySQL server.
-- Records will be ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
