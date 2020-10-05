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
  `aadharCard` bigint NOT NULL,
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
INSERT INTO `actor` VALUES (288720001485,3,165,82),(289576609004,2,172,110),(290722165251,1,150,60),(315439533406,2,120,45),(402264546504,3,152,80),(475546528070,1,160,75),(601609790887,0,145,55),(611761119375,1,157,105),(633703909581,3,90,40),(696370762846,5,155,88),(743088703942,2,165,65),(806784985109,1,155,80),(987177520201,3,162,95);
/*!40000 ALTER TABLE `actor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ad`
--

DROP TABLE IF EXISTS `ad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ad` (
  `serialNo` int NOT NULL,
  `duration` int DEFAULT NULL,
  PRIMARY KEY (`serialNo`),
  CONSTRAINT `ad_ibfk_1` FOREIGN KEY (`serialNo`) REFERENCES `production` (`adSerialNo`) ON DELETE CASCADE,
  CONSTRAINT `ad_chk_1` CHECK ((`duration` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ad`
--

LOCK TABLES `ad` WRITE;
/*!40000 ALTER TABLE `ad` DISABLE KEYS */;
INSERT INTO `ad` VALUES (1,80),(2,108),(3,101),(4,73),(5,37),(6,29),(7,107),(8,48),(9,71),(10,78);
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
INSERT INTO `adGenre` VALUES ('Comedy',1),('Thriller',2),('Thriller',3),('Romance',3),('Comedy',4),('Thriller',4),('Action',4),('Romance',5),('Comedy',6),('Fantasy',6),('Comedy',7),('Suspense',7),('Suspense',8),('Comedy',9),('Comedy',10),('Romance',10),('Action',10);
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
  `pocPhone` bigint DEFAULT NULL,
  PRIMARY KEY (`brandName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES ('Adidas','ultricies@placeratorcilacus.org',6620836486),('Hamleys','vitae.semper.egestas@arcuSedeu.net',3919282002),('McDonalds','sem.consequat@quamvelsapien.com',9623112183),('Nestle','netus@velesttempor.net',2903177783),('tichnas','iaculis@penatibus.net',7069898351);
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `channel` (
  `channelName` varchar(255) NOT NULL,
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
INSERT INTO `channel` VALUES ('Aaj Tak',9691),('Animal Planet',5127),('Disney',93317),('Nickledeon',35527),('Sony',71950);
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `director`
--

DROP TABLE IF EXISTS `director`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `director` (
  `aadharCard` bigint NOT NULL,
  `joinDate` date NOT NULL,
  `salary` int NOT NULL,
  `supervisorAadharCard` bigint DEFAULT NULL,
  PRIMARY KEY (`aadharCard`),
  KEY `supervisorAadharCard` (`supervisorAadharCard`),
  CONSTRAINT `director_ibfk_1` FOREIGN KEY (`aadharCard`) REFERENCES `person` (`aadharCard`) ON DELETE CASCADE,
  CONSTRAINT `director_ibfk_2` FOREIGN KEY (`supervisorAadharCard`) REFERENCES `director` (`aadharCard`) ON DELETE SET NULL,
  CONSTRAINT `director_chk_1` CHECK ((`salary` >= 10000))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `director`
--

LOCK TABLES `director` WRITE;
/*!40000 ALTER TABLE `director` DISABLE KEYS */;
INSERT INTO `director` VALUES (230687914469,'2001-01-10',55000,NULL),(257691800359,'2002-03-12',25000,897114443820),(261132474728,'2015-10-12',25000,230687914469),(331440631972,'2015-10-12',25000,230687914469),(475671876615,'2000-09-14',25000,897114443820),(543278675609,'2000-08-15',25000,897114443820),(897114443820,'2001-01-10',55000,NULL);
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
INSERT INTO `displayedBetween` VALUES ('2020-10-02','18:00:00','Disney',2,6),('2020-10-02','18:00:00','Disney',4,4),('2020-10-02','18:00:00','Disney',6,2),('2020-10-02','18:00:00','Disney',8,2),('2020-10-05','23:00:00','Animal Planet',1,6),('2020-10-05','23:00:00','Animal Planet',3,2),('2020-10-05','23:00:00','Animal Planet',5,1),('2020-10-05','23:00:00','Animal Planet',7,3),('2020-10-05','23:00:00','Animal Planet',8,2),('2020-10-05','23:00:00','Sony',2,2),('2020-10-05','23:00:00','Sony',4,1),('2020-10-05','23:00:00','Sony',6,1),('2020-10-05','23:00:00','Sony',8,1),('2020-10-06','05:00:00','Animal Planet',1,2),('2020-10-06','05:00:00','Animal Planet',3,2),('2020-10-06','05:00:00','Animal Planet',5,3),('2020-10-06','05:00:00','Animal Planet',7,3),('2020-10-06','05:00:00','Animal Planet',8,2),('2020-10-06','09:00:00','Animal Planet',1,2),('2020-10-06','09:00:00','Animal Planet',3,1),('2020-10-06','09:00:00','Animal Planet',5,1),('2020-10-06','09:00:00','Animal Planet',7,2),('2020-10-06','09:00:00','Animal Planet',8,2),('2020-10-07','09:00:00','Animal Planet',1,2),('2020-10-07','09:00:00','Animal Planet',3,3),('2020-10-07','09:00:00','Animal Planet',5,4),('2020-10-07','09:00:00','Animal Planet',7,1),('2020-10-07','09:00:00','Animal Planet',8,1),('2020-10-12','11:00:00','Nickledeon',2,3),('2020-10-12','11:00:00','Nickledeon',4,2),('2020-10-12','11:00:00','Nickledeon',6,1),('2020-10-12','11:00:00','Nickledeon',8,1),('2020-10-13','15:00:00','Nickledeon',2,2),('2020-10-13','15:00:00','Nickledeon',4,5),('2020-10-13','15:00:00','Nickledeon',6,3),('2020-10-13','15:00:00','Nickledeon',8,1),('2020-10-14','23:00:00','Sony',2,2),('2020-10-14','23:00:00','Sony',4,3),('2020-10-14','23:00:00','Sony',6,1),('2020-10-14','23:00:00','Sony',8,1),('2020-10-17','18:00:00','Animal Planet',1,4),('2020-10-17','18:00:00','Animal Planet',2,2),('2020-10-17','18:00:00','Animal Planet',8,2),('2020-10-19','18:00:00','Disney',2,1),('2020-10-19','18:00:00','Disney',4,2),('2020-10-19','18:00:00','Disney',6,3),('2020-10-19','18:00:00','Disney',8,1),('2020-10-20','18:00:00','Disney',2,4),('2020-10-20','18:00:00','Disney',4,5),('2020-10-20','18:00:00','Disney',6,2),('2020-10-20','18:00:00','Disney',8,2),('2020-10-22','11:00:00','Nickledeon',2,4),('2020-10-22','11:00:00','Nickledeon',4,3),('2020-10-22','11:00:00','Nickledeon',6,1),('2020-10-22','11:00:00','Nickledeon',8,2),('2020-10-25','09:00:00','Animal Planet',1,3),('2020-10-25','09:00:00','Animal Planet',3,5),('2020-10-25','09:00:00','Animal Planet',5,1),('2020-10-25','09:00:00','Animal Planet',7,1),('2020-10-25','09:00:00','Animal Planet',8,1),('2020-10-31','07:00:00','Sony',2,1),('2020-10-31','07:00:00','Sony',4,2),('2020-10-31','07:00:00','Sony',8,2);
/*!40000 ALTER TABLE `displayedBetween` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `before_displaying` BEFORE INSERT ON `displayedBetween` FOR EACH ROW BEGIN
	declare showDuration INT;
    declare adDurationTillNow INT;
    declare adDuration int;
    
    SELECT (duration*60) into showDuration from `show` where 
    (`date`= new.showDate and 
    `startTime` = new.showStartTime and 
    `channelName` = new.channelName);
    
    select sum(A.duration * D.timesShown) into adDurationTillNow from
	displayedBetween as D, ad as A where A.serialNo = D.adSerialNo and (
	D.channelName = new.channelName and
    D.showStartTime = new.showStartTime and
    D.showDate = new.showDate
    );
    
    select (duration * new.timesShown) into adDuration from `ad` where serialNo = new.adSerialNo;
    
    if (adDurationTillNow + adDuration) > showDuration
    then
		signal sqlstate '45000' set message_text = 'Ad Duration exceeding show duration';
	end if;

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `guardian`
--

DROP TABLE IF EXISTS `guardian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guardian` (
  `jActorAadharCard` bigint NOT NULL,
  `aadharCard` bigint NOT NULL,
  PRIMARY KEY (`aadharCard`,`jActorAadharCard`),
  KEY `jActorAadharCard` (`jActorAadharCard`),
  CONSTRAINT `guardian_ibfk_1` FOREIGN KEY (`jActorAadharCard`) REFERENCES `juniorActor` (`aadharCard`) ON DELETE CASCADE,
  CONSTRAINT `guardian_ibfk_2` FOREIGN KEY (`aadharCard`) REFERENCES `guardianData` (`aadharCard`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guardian`
--

LOCK TABLES `guardian` WRITE;
/*!40000 ALTER TABLE `guardian` DISABLE KEYS */;
INSERT INTO `guardian` VALUES (290722165251,245369852145),(315439533406,523478235896),(601609790887,986321456325);
/*!40000 ALTER TABLE `guardian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guardianData`
--

DROP TABLE IF EXISTS `guardianData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guardianData` (
  `aadharCard` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` bigint NOT NULL,
  PRIMARY KEY (`aadharCard`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guardianData`
--

LOCK TABLES `guardianData` WRITE;
/*!40000 ALTER TABLE `guardianData` DISABLE KEYS */;
INSERT INTO `guardianData` VALUES (245369852145,'Rajesh',9868652145),(523478235896,'Rahul',6845721398),(986321456325,'Mehak',9832145687);
/*!40000 ALTER TABLE `guardianData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juniorActor`
--

DROP TABLE IF EXISTS `juniorActor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `juniorActor` (
  `aadharCard` bigint NOT NULL,
  PRIMARY KEY (`aadharCard`),
  CONSTRAINT `juniorActor_ibfk_1` FOREIGN KEY (`aadharCard`) REFERENCES `actor` (`aadharCard`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juniorActor`
--

LOCK TABLES `juniorActor` WRITE;
/*!40000 ALTER TABLE `juniorActor` DISABLE KEYS */;
INSERT INTO `juniorActor` VALUES (290722165251),(315439533406),(601609790887);
/*!40000 ALTER TABLE `juniorActor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `aadharCard` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `accountNo` bigint NOT NULL,
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
INSERT INTO `person` VALUES (230687914469,'Lesley',852404298923,'Male','1983-05-31'),(257691800359,'Forrest',293895034818,'Male','1993-09-12'),(261132474728,'Illana',630591625104,'Male','1990-06-15'),(288720001485,'Cynthia',522875225448,'Male','1996-04-08'),(289576609004,'Kamal',737758211018,'Male','1988-11-23'),(290722165251,'Imelda',195117667857,'Other','2004-02-12'),(315439533406,'Riley',879660132703,'Other','2006-11-24'),(331440631972,'Indira',993432086651,'Female','1993-08-06'),(402264546504,'Kimberly',680176799652,'Male','1982-03-24'),(475546528070,'Baker',421251500464,'Male','1991-12-14'),(475671876615,'Nigel',144083857152,'Male','2001-01-02'),(543278675609,'Dean',668334235465,'Male','2001-12-24'),(601609790887,'Zoe',33378897725,'Female','2004-07-06'),(611761119375,'Allegra',268182069628,'Female','1988-06-30'),(633703909581,'Boris',244114081678,'Male','1992-11-07'),(696370762846,'Bruno',890939914812,'Male','1990-08-21'),(743088703942,'Ralph',606985805090,'Female','1982-04-19'),(806784985109,'Dillon',356654289589,'Female','1993-10-25'),(897114443820,'Adam',99716021918,'Female','1981-07-11'),(987177520201,'Colby',521956628669,'Male','2001-11-05');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phone`
--

DROP TABLE IF EXISTS `phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phone` (
  `aadharCard` bigint NOT NULL,
  `phoneNo` bigint NOT NULL,
  PRIMARY KEY (`aadharCard`,`phoneNo`),
  CONSTRAINT `phone_ibfk_1` FOREIGN KEY (`aadharCard`) REFERENCES `person` (`aadharCard`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone`
--

LOCK TABLES `phone` WRITE;
/*!40000 ALTER TABLE `phone` DISABLE KEYS */;
INSERT INTO `phone` VALUES (230687914469,1257469825),(257691800359,5472368415),(261132474728,5874523698),(288720001485,1225589876),(289576609004,2143698527),(290722165251,5478369821),(315439533406,8800565685),(331440631972,3214536982),(402264546504,4789685869),(475546528070,2547369285),(475671876615,2547893214),(543278675609,2415789658),(601609790887,2255479942),(611761119375,7587126985),(633703909581,9988268745),(696370762846,8800565686),(743088703942,2478569821),(806784985109,2143698521),(897114443820,2458963257),(987177520201,9876583216);
/*!40000 ALTER TABLE `phone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prefers`
--

DROP TABLE IF EXISTS `prefers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prefers` (
  `actorAadharCard` bigint NOT NULL,
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
INSERT INTO `prefers` VALUES (315439533406,'Adidas'),(601609790887,'Adidas'),(402264546504,'McDonalds'),(601609790887,'McDonalds'),(290722165251,'Nestle'),(315439533406,'Nestle'),(402264546504,'Nestle'),(290722165251,'tichnas'),(315439533406,'tichnas'),(402264546504,'tichnas'),(601609790887,'tichnas');
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
INSERT INTO `product` VALUES ('Battery','tichnas',NULL,69647),('Book','Hamleys',NULL,872),('Coffee','Nestle',NULL,600),('Laptop T17x','tichnas',NULL,268010),('Maggi','Nestle',NULL,30),('Nuggets','McDonalds',NULL,444),('Shoes','Adidas',NULL,5084),('Shoes','Hamleys',NULL,3298),('Shoes','tichnas',NULL,43843),('T-Shirt','Adidas',NULL,4737),('T-Shirt','tichnas',NULL,1661);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `production`
--

DROP TABLE IF EXISTS `production`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `production` (
  `adSerialNo` int NOT NULL AUTO_INCREMENT,
  `actorAadharCard` bigint NOT NULL,
  `directorAadharCard` bigint NOT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `production`
--

LOCK TABLES `production` WRITE;
/*!40000 ALTER TABLE `production` DISABLE KEYS */;
INSERT INTO `production` VALUES (1,290722165251,543278675609,'Shoes','Hamleys','2020-02-02',15000),(2,601609790887,261132474728,'Book','Hamleys','2020-01-14',5000),(3,315439533406,257691800359,'Nuggets','McDonalds','2020-03-20',7000),(4,806784985109,543278675609,'Laptop T17x','tichnas','2020-04-07',18000),(5,611761119375,261132474728,'Shoes','Hamleys','2020-02-18',2000),(6,475546528070,331440631972,'T-Shirt','tichnas','2020-03-23',20000),(7,987177520201,475671876615,'Shoes','Hamleys','2020-02-28',8000),(8,987177520201,257691800359,'Coffee','Nestle','2020-02-04',4000),(9,987177520201,257691800359,'Maggi','Nestle','2020-02-08',9000),(10,475546528070,475671876615,'T-Shirt','Adidas','2020-10-02',12000);
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
  KEY `channelName` (`channelName`),
  CONSTRAINT `show_ibfk_1` FOREIGN KEY (`channelName`) REFERENCES `channel` (`channelName`) ON DELETE CASCADE,
  CONSTRAINT `show_chk_1` CHECK (((`surcharge` >= 0) and (`duration` > 0)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `show`
--

LOCK TABLES `show` WRITE;
/*!40000 ALTER TABLE `show` DISABLE KEYS */;
INSERT INTO `show` VALUES ('2020-10-02','18:00:00','Disney',90,435,'Jake and Pirate'),('2020-10-05','23:00:00','Animal Planet',105,631,'King of Jungle'),('2020-10-05','23:00:00','Sony',75,280,'Pati Patni aur Wo'),('2020-10-06','05:00:00','Animal Planet',75,843,'Deadliest in the Wild'),('2020-10-06','09:00:00','Animal Planet',90,182,'1000 years before'),('2020-10-07','09:00:00','Animal Planet',75,380,'Most Dangerous 10'),('2020-10-07','18:00:00','Sony',90,712,'mollis'),('2020-10-08','09:00:00','Aaj Tak',120,838,'Aaj ki News'),('2020-10-12','11:00:00','Nickledeon',105,729,'Art Attack'),('2020-10-13','15:00:00','Nickledeon',105,16,'Ninja Hattori'),('2020-10-14','05:00:00','Aaj Tak',60,183,'Jungle News'),('2020-10-14','23:00:00','Sony',30,374,'Nach le India'),('2020-10-17','18:00:00','Animal Planet',60,492,'Jungle Jungle'),('2020-10-19','07:00:00','Aaj Tak',105,68,'10 Breaking News'),('2020-10-19','18:00:00','Disney',120,489,'Doraemon'),('2020-10-20','18:00:00','Disney',120,143,'Shinchan'),('2020-10-21','07:00:00','Aaj Tak',30,42,'Top 10'),('2020-10-22','11:00:00','Nickledeon',105,344,'Perman'),('2020-10-25','09:00:00','Animal Planet',90,362,'Snakes'),('2020-10-31','07:00:00','Sony',90,149,'Crime Patrol');
/*!40000 ALTER TABLE `show` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `before_show_insert` BEFORE INSERT ON `show` FOR EACH ROW BEGIN
	declare possible int;
    select count(*) into possible from `show` where 
    (
    `date` = new.`date` and
    ((new.startTime < startTime and startTime < ADDTIME(new.startTime, SEC_TO_TIME(new.duration*60)))
    or
    (startTime < new.startTime and new.startTime < ADDTIME(startTime, SEC_TO_TIME(duration*60)))
    ));
	if possible > 0
	then
		signal sqlstate '45000' set message_text = 'Not a valid show time and duration';
	end if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

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
INSERT INTO `showGenre` VALUES ('Comedy','2020-10-02','18:00:00','Disney'),('Thriller','2020-10-05','23:00:00','Animal Planet'),('Comedy','2020-10-05','23:00:00','Sony'),('Romance','2020-10-05','23:00:00','Sony'),('Thriller','2020-10-06','05:00:00','Animal Planet'),('Thriller','2020-10-07','09:00:00','Animal Planet'),('Action','2020-10-07','18:00:00','Sony'),('Comedy','2020-10-12','11:00:00','Nickledeon'),('Comedy','2020-10-13','15:00:00','Nickledeon'),('Comedy','2020-10-14','23:00:00','Sony'),('Comedy','2020-10-19','18:00:00','Disney'),('Comedy','2020-10-20','18:00:00','Disney'),('Comedy','2020-10-22','11:00:00','Nickledeon'),('Comedy','2020-10-25','09:00:00','Animal Planet'),('Suspense','2020-10-31','07:00:00','Sony');
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

-- Dump completed on 2020-10-05 20:17:48
