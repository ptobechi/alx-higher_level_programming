-- Script to display the number of records with id = 89 in the table first_table
-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Query to count the number of records with id = 89 in the table first_table
SELECT COUNT(*) AS count_89 FROM first_table WHERE id = 89;
