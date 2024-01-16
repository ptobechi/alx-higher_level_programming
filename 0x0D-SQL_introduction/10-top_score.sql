-- Script to list all records of the table second_table
-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Query to list all records of second_table ordered by score
SELECT score, name FROM second_table ORDER BY score DESC;
