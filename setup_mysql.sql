DROP DATABASE IF EXISTS `mysqldb`;
CREATE DATABASE `mysqldb`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;
CREATE USER 'mysql-user'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'mysql-user'@'$' WITH GRANT OPTION;
FLUSH PRIVILEGES;
