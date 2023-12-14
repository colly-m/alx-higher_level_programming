-- Script to list all cities in a database 'hbtn_0d_usa'

SELECT cities.id, cities.name, states.name,
FROM cities
LEFT JOIN states ON state_id = cities.states_id
ORDER BY cities.id ASC;
