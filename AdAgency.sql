-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: AdAgency
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actor`
--

DROP TABLE IF EXISTS `actor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actor` (
  `aadharCard` int NOT NULL,
  `experience` int NOT NULL,
  `height` int NOT NULL,
  `weight` int NOT NULL,
  PRIMARY KEY (`aadharCard`),
  CONSTRAINT `actor_ibfk_1` FOREIGN KEY (`aadharCard`) REFERENCES `person` (`aadharCard`) ON DELETE CASCADE,
  CONSTRAINT `actor_chk_1` CHECK (((`experience` >= 0) and (`height` > 0) and (`weight` > 0)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actor`
--

LOCK TABLES `actor` WRITE;
/*!40000 ALTER TABLE `actor` DISABLE KEYS */;
/*!40000 ALTER TABLE `actor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ad`
--

DROP TABLE IF EXISTS `ad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ad` (
  `serialNo` int NOT NULL AUTO_INCREMENT,
  `duration` int DEFAULT NULL,
  PRIMARY KEY (`serialNo`),
  CONSTRAINT `ad_chk_1` CHECK ((`duration` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ad`
--

LOCK TABLES `ad` WRITE;
/*!40000 ALTER TABLE `ad` DISABLE KEYS */;
/*!40000 ALTER TABLE `ad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adGenre`
--

DROP TABLE IF EXISTS `adGenre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adGenre` (
  `name` enum('Comedy','Thriller','Romance','Suspense','Sci-fi','Action','Horror','Fantasy') NOT NULL,
  `adSerialNo` int NOT NULL,
  PRIMARY KEY (`name`,`adSerialNo`),
  KEY `adSerialNo` (`adSerialNo`),
  CONSTRAINT `adGenre_ibfk_1` FOREIGN KEY (`adSerialNo`) REFERENCES `ad` (`serialNo`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adGenre`
--

LOCK TABLES `adGenre` WRITE;
/*!40000 ALTER TABLE `adGenre` DISABLE KEYS */;
/*!40000 ALTER TABLE `adGenre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brand` (
  `brandName` varchar(255) NOT NULL,
  `pocEmail` varchar(255) DEFAULT NULL,
  `pocPhone` int DEFAULT NULL,
  PRIMARY KEY (`brandName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `channel` (
  `channelName` varchar(50) NOT NULL,
  `basePrice` int NOT NULL,
  PRIMARY KEY (`channelName`),
  CONSTRAINT `channel_chk_1` CHECK ((`basePrice` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel`
--

LOCK TABLES `channel` WRITE;
/*!40000 ALTER TABLE `channel` DISABLE KEYS */;
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `director`
--

DROP TABLE IF EXISTS `director`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `director` (
  `aadharCard` int NOT NULL,
  `joinDate` date NOT NULL,
  `salary` int NOT NULL,
  `supervisorAadharCard` int DEFAULT NULL,
  PRIMARY KEY (`aadharCard`),
  KEY `supervisorAadharCard` (`supervisorAadharCard`),
  CONSTRAINT `director_ibfk_1` FOREIGN KEY (`supervisorAadharCard`) REFERENCES `director` (`aadharCard`) ON DELETE CASCADE,
  CONSTRAINT `director_chk_1` CHECK ((`salary` >= 10000))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `director`
--

LOCK TABLES `director` WRITE;
/*!40000 ALTER TABLE `director` DISABLE KEYS */;
/*!40000 ALTER TABLE `director` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `displayedBetween`
--

DROP TABLE IF EXISTS `displayedBetween`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `displayedBetween` (
  `showDate` date NOT NULL,
  `showStartTime` time NOT NULL,
  `channelName` varchar(255) NOT NULL,
  `adSerialNo` int NOT NULL,
  `timesShown` int DEFAULT '1',
  PRIMARY KEY (`showDate`,`showStartTime`,`channelName`,`adSerialNo`),
  KEY `adSerialNo` (`adSerialNo`),
  CONSTRAINT `displayedBetween_ibfk_1` FOREIGN KEY (`showDate`, `showStartTime`, `channelName`) REFERENCES `show` (`date`, `startTime`, `channelName`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `displayedBetween_ibfk_2` FOREIGN KEY (`adSerialNo`) REFERENCES `ad` (`serialNo`) ON DELETE CASCADE,
  CONSTRAINT `displayedBetween_chk_1` CHECK ((`timesShown` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `displayedBetween`
--

LOCK TABLES `displayedBetween` WRITE;
/*!40000 ALTER TABLE `displayedBetween` DISABLE KEYS */;
/*!40000 ALTER TABLE `displayedBetween` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gaurdian`
--

DROP TABLE IF EXISTS `gaurdian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gaurdian` (
  `jActorAadharCard` int NOT NULL,
  `aadharCard` int NOT NULL,
  PRIMARY KEY (`aadharCard`,`jActorAadharCard`),
  KEY `jActorAadharCard` (`jActorAadharCard`),
  CONSTRAINT `gaurdian_ibfk_1` FOREIGN KEY (`jActorAadharCard`) REFERENCES `juniorActor` (`aadharCard`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gaurdian`
--

LOCK TABLES `gaurdian` WRITE;
/*!40000 ALTER TABLE `gaurdian` DISABLE KEYS */;
/*!40000 ALTER TABLE `gaurdian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gaurdianData`
--

DROP TABLE IF EXISTS `gaurdianData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gaurdianData` (
  `aadharCard` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` int NOT NULL,
  PRIMARY KEY (`aadharCard`),
  CONSTRAINT `gaurdianData_ibfk_1` FOREIGN KEY (`aadharCard`) REFERENCES `gaurdian` (`aadharCard`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gaurdianData`
--

LOCK TABLES `gaurdianData` WRITE;
/*!40000 ALTER TABLE `gaurdianData` DISABLE KEYS */;
/*!40000 ALTER TABLE `gaurdianData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juniorActor`
--

DROP TABLE IF EXISTS `juniorActor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `juniorActor` (
  `aadharCard` int NOT NULL,
  PRIMARY KEY (`aadharCard`),
  CONSTRAINT `juniorActor_ibfk_1` FOREIGN KEY (`aadharCard`) REFERENCES `actor` (`aadharCard`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juniorActor`
--

LOCK TABLES `juniorActor` WRITE;
/*!40000 ALTER TABLE `juniorActor` DISABLE KEYS */;
/*!40000 ALTER TABLE `juniorActor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `aadharCard` int NOT NULL,
  `name` varchar(12) NOT NULL,
  `accountNo` int NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `DOB` date NOT NULL,
  PRIMARY KEY (`aadharCard`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phone`
--

DROP TABLE IF EXISTS `phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phone` (
  `aadharCard` int NOT NULL,
  `phoneNo` int NOT NULL,
  PRIMARY KEY (`aadharCard`,`phoneNo`),
  CONSTRAINT `phone_ibfk_1` FOREIGN KEY (`aadharCard`) REFERENCES `person` (`aadharCard`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone`
--

LOCK TABLES `phone` WRITE;
/*!40000 ALTER TABLE `phone` DISABLE KEYS */;
/*!40000 ALTER TABLE `phone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prefers`
--

DROP TABLE IF EXISTS `prefers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prefers` (
  `actorAadharCard` int NOT NULL,
  `brandName` varchar(255) NOT NULL,
  PRIMARY KEY (`actorAadharCard`,`brandName`),
  KEY `brandName` (`brandName`),
  CONSTRAINT `prefers_ibfk_1` FOREIGN KEY (`actorAadharCard`) REFERENCES `actor` (`aadharCard`) ON DELETE CASCADE,
  CONSTRAINT `prefers_ibfk_2` FOREIGN KEY (`brandName`) REFERENCES `brand` (`brandName`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prefers`
--

LOCK TABLES `prefers` WRITE;
/*!40000 ALTER TABLE `prefers` DISABLE KEYS */;
/*!40000 ALTER TABLE `prefers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `name` varchar(255) NOT NULL,
  `brandName` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`name`,`brandName`),
  KEY `brandName` (`brandName`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`brandName`) REFERENCES `brand` (`brandName`) ON DELETE CASCADE,
  CONSTRAINT `product_chk_1` CHECK ((`price` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `production`
--

DROP TABLE IF EXISTS `production`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `production` (
  `adSerialNo` int NOT NULL,
  `actorAadharCard` int NOT NULL,
  `directorAadharCard` int NOT NULL,
  `productName` varchar(255) NOT NULL,
  `brandName` varchar(255) NOT NULL,
  `signingDate` date NOT NULL,
  `productionCost` int NOT NULL,
  PRIMARY KEY (`adSerialNo`),
  KEY `actorAadharCard` (`actorAadharCard`),
  KEY `directorAadharCard` (`directorAadharCard`),
  KEY `productName` (`productName`,`brandName`),
  CONSTRAINT `production_ibfk_1` FOREIGN KEY (`actorAadharCard`) REFERENCES `actor` (`aadharCard`) ON DELETE CASCADE,
  CONSTRAINT `production_ibfk_2` FOREIGN KEY (`directorAadharCard`) REFERENCES `director` (`aadharCard`) ON DELETE CASCADE,
  CONSTRAINT `production_ibfk_3` FOREIGN KEY (`productName`, `brandName`) REFERENCES `product` (`name`, `brandName`) ON DELETE CASCADE,
  CONSTRAINT `production_chk_1` CHECK ((`productionCost` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `production`
--

LOCK TABLES `production` WRITE;
/*!40000 ALTER TABLE `production` DISABLE KEYS */;
/*!40000 ALTER TABLE `production` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `show`
--

DROP TABLE IF EXISTS `show`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `show` (
  `date` date NOT NULL,
  `startTime` time NOT NULL,
  `channelName` varchar(255) NOT NULL,
  `duration` int NOT NULL,
  `surcharge` int NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`date`,`startTime`,`channelName`),
  CONSTRAINT `show_chk_1` CHECK (((`surcharge` >= 0) and (`duration` > 0)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `show`
--

LOCK TABLES `show` WRITE;
/*!40000 ALTER TABLE `show` DISABLE KEYS */;
/*!40000 ALTER TABLE `show` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `showGenre`
--

DROP TABLE IF EXISTS `showGenre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `showGenre` (
  `name` enum('Comedy','Thriller','Romance','Suspense','Sci-fi','Action','Horror','Fantasy') NOT NULL,
  `showDate` date NOT NULL,
  `showStartTime` time NOT NULL,
  `channelName` varchar(255) NOT NULL,
  PRIMARY KEY (`showDate`,`showStartTime`,`channelName`,`name`),
  CONSTRAINT `showGenre_ibfk_1` FOREIGN KEY (`showDate`, `showStartTime`, `channelName`) REFERENCES `show` (`date`, `startTime`, `channelName`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `showGenre`
--

LOCK TABLES `showGenre` WRITE;
/*!40000 ALTER TABLE `showGenre` DISABLE KEYS */;
/*!40000 ALTER TABLE `showGenre` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-02 23:21:53
