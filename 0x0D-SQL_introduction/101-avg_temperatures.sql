-- Script to show average temperature in fahrenheit by city in descending
SELECT city, avg(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
