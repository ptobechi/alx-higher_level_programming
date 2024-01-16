-- Script to list records with a score >= 10 in the table second_table
-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Query to list records with a score >= 10 from second_table ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
