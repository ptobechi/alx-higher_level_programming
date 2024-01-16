-- Script to update the score of Bob to 10 in the table second_table
-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Query to update the score of Bob to 10
UPDATE second_table SET score = 10 WHERE name = 'Bob';
