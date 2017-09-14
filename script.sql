/*DROP DATABASE IF EXISTS `guillaumeElec`;
CREATE DATABASE `guillaumeElec`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

USE 'mysql';
GRANT ALL PRIVILEGES ON mydb.* TO 'thomas'@'localhost' IDENTIFIED BY 'Cr@y0n!Vert'

WITH GRANT OPTION;
FLUSH PRIVILEGES;*/



CREATE DATABASE guillaumeElec CHARACTER SET UTF8;

CREATE USER 'thomas'@'localhost' IDENTIFIED BY 'Cr@y0n!Vert';

GRANT ALL PRIVILEGES ON guillaumeElec.* TO 'thomas'@'localhost';

FLUSH PRIVILEGES;
