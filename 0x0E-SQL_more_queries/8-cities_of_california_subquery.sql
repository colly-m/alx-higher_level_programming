-- Script to list all cities of California found in database 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Select all cities in California sorted by cities.id
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
