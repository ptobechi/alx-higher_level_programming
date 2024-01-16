-- Script to list the number of records with the same score in the table second_table
-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Query to count the number of records for each score and
-- sort by count in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;
