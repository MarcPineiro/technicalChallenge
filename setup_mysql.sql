DROP DATABASE IF EXISTS `mysqldb`;
CREATE DATABASE `mysqldb`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;
CREATE USER 'mysql-user'@'localhost' IDENTIFIED BY 'password';
USE mysql;
GRANT ALL PRIVILEGES ON *.* TO 'mysql-user'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
