-- Script to display the top 3 cities with the highest
-- temperatures during July and August

-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Display the top 3 cities with the highest temperatures
-- during July and August
SELECT city, MAX(temperature) AS max_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY max_temp DESC
LIMIT 3;
