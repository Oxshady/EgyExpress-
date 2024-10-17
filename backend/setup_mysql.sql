-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS sh;
CREATE USER IF NOT EXISTS 'shadi'@'localhost' IDENTIFIED BY '1';
GRANT ALL PRIVILEGES ON `sh`.* TO 'shadi'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'shadi'@'localhost';
FLUSH PRIVILEGES;
