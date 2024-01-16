-- Script to compute the score average of all records in the table second_table
-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Query to compute the average score
SELECT AVG(score) AS average FROM second_table;
