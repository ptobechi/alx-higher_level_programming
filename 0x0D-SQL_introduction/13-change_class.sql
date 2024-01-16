-- Script to remove all records with a score <= 5 in the table second_table
-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Query to delete records with a score <= 5
DELETE FROM second_table WHERE score <= 5;
