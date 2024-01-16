-- Script to create a table called first_table in the specified database
-- Checking if the argument (database name) is provided */
USE hbtn_0c_0;

-- Query to create the table first_table */
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
