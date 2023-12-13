-- Script tolist all records of a table 'second_table' of database in MySQL server
-- No list without name value
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
