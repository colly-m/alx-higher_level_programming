-- Script to list number of records with samw score in a table  of database in MySQL server
-- Should display the 'score' and 'number' of records
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
