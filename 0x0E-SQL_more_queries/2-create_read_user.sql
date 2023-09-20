-- Will create database hbtn_0d_2 and the user user_0d_2
-- Will make a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Will create user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- gives SELECT privileges to user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
