-- Script to list all records with 'score >= 10' in a table from database in MySQL server
-- To display both score and name respectively ordered by score in descend
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
