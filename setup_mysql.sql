DROP DATABASE IF EXISTS `mysqldb`;
CREATE DATABASE `mysqldb`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;
drop user admin@localhost;

GRANT ALL PRIVILEGES ON *.* TO 'mysql-user'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
