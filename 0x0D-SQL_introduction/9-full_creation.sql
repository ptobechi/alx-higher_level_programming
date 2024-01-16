-- Script to create table second_table and add multiple rows
-- Checking if the argument (database name) is provided */
USE hbtn_0c_0;

-- Query to create table second_table if not exists */
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

--Query to insert multiple rows into second_table */
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
