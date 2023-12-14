-- Script to list all cities in a database 'hbtn_0d_usa'

SELECT cities.id, cities.name, states.name,
FROM cities
LEFT JOIN states ON state_id = cities.state_id
ORDER BY cities.id ASC;
