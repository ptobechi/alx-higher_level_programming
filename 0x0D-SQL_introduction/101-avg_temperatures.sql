-- Script to calculate and display the average temperature
-- (Fahrenheit) by city ordered by temperature (descending)

-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Create a temporary table to store the converted temperature in Fahrenheit
CREATE TEMPORARY TABLE temp_table AS
    SELECT city, (temperature * 9/5 + 32) AS temp_fahrenheit
    FROM temperatures;

-- Display the average temperature by city, ordered by
-- temperature in descending order
SELECT city, AVG(temp_fahrenheit) AS avg_temp
FROM temp_table
GROUP BY city
ORDER BY avg_temp DESC;

-- Drop the temporary table
DROP TEMPORARY TABLE IF EXISTS temp_table;
