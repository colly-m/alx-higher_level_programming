-- Script to create a database 'hbtn_0d_2' and user 'user_0d_2' with read priviledge

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates user
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants priviledge
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
