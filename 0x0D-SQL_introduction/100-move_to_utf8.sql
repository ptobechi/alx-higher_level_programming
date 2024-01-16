-- Script to convert the hbtn_0c_0 database, first_table table,
-- and name field to UTF8

-- Checking if the argument (database name) is provided
USE hbtn_0c_0;

-- Alter the database collation to utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter the first_table table collation to utf8mb4_unicode_ci
ALTER TABLE first_table CONVERT TO CHARACTER \
SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter the name field collation in first_table to utf8mb4_unicode_ci
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) \ 
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
