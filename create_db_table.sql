-- Thist should be run as ais database user
-- mysql -uaispy -paispy ais < create_db_table.sql
-- 
-- MariaDB dump 10.19  Distrib 10.4.20-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: ais
-- ------------------------------------------------------
-- Server version	10.4.20-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `nmea`
--

DROP TABLE IF EXISTS `nmea`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nmea` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `msgtype` varchar(6) NOT NULL,
  `mmsi` varchar(30) NOT NULL,
  `rxtime` varchar(20) NOT NULL,
  `lon` varchar(28) ,
  `lat` varchar(27) ,
  `speed` varchar(20) ,
  `course` varchar(12) ,
  `heading` varchar(9) ,
  `status` varchar(4) ,
  `shiptype` varchar(8) ,
  `partno` varchar(2) ,
  `callsign` varchar(42) ,
  `shipname` varchar(120) ,
  `vendorid` varchar(18) ,
  `ref_front` varchar(9) ,
  `ref_left` varchar(9) ,
  `draught` varchar(8) ,
  `length` varchar(9) ,
  `width` varchar(9) ,
  `destination` varchar(120) ,
  `persons_on_board` varchar(14) ,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nmea`
--

LOCK TABLES `nmea` WRITE;
/*!40000 ALTER TABLE `nmea` DISABLE KEYS */;
/*!40000 ALTER TABLE `nmea` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-27 16:31:39
