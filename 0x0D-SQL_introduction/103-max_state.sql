-- Script to display the max temperature of each state ordered by State name

-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Display the max temperature of each state ordered by State name
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
