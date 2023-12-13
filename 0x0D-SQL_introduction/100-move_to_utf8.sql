-- Script to convert a database to UTF8 in MySQL Server
-- Converting database, table, field
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
