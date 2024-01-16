-- Script to list all records of the table second_table without rows without a name value
-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Query to list all records with names and display score and name
-- in descending order by score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
