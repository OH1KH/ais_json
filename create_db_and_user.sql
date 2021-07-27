-- This must br executed as root (of database) 
-- mysql -uroot -p < create_db_and_user.sql
--
CREATE DATABASE ais;

CREATE USER 'aispy'@'localhost' IDENTIFIED BY 'aispy';
GRANT ALL PRIVILEGES ON ais.* TO `aispy`@`localhost`;
FLUSH PRIVILEGES; 
