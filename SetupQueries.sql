use AdAgency;

CREATE TABLE `person` (
    `aadharCard` BIGINT primary key,
    `name` VARCHAR (255) NOT NULL,
    `accountNo` BIGINT NOT NULL,
    `gender` enum ('Male', 'Female', 'Other') NOT NULL,
    `DOB` DATE NOT NULL
);

create table `brand` (
	`brandName` varchar(255) primary key,
	`pocEmail` varchar(255),
	`pocPhone` bigint
);

CREATE TABLE `channel` (
    `channelName` VARCHAR (255) NOT NULL,
    `basePrice` INT NOT NULL,
    PRIMARY KEY (`channelName`),
    CHECK (basePrice >= 0)
);

CREATE TABLE `director` (
    `aadharCard` BIGINT primary key,
    `joinDate` DATE not null,
    `salary` INT NOT NULL,
    `supervisorAadharCard` BIGINT,
    FOREIGN KEY (`aadharCard`) REFERENCES `person` (`aadharCard`) ON DELETE CASCADE,
    FOREIGN KEY (`supervisorAadharCard`) REFERENCES `director` (`aadharCard`) ON DELETE SET NULL,
    CHECK (salary >= 10000)
);

create table `product` (
	`name` varchar(255),
	`brandName` varchar(255),
	`description` varchar(255),
	`price` int,
	check (`price` >= 0),
	primary key (`name`, `brandName`),
	foreign key (`brandName`)
		references `brand` (`brandName`)
		on delete cascade
);

create table `phone` (
	`aadharCard` bigint,
	`phoneNo` bigint,
	primary key (`aadharCard`, `phoneNo`),
	foreign key (`aadharCard`)
		references `person` (`aadharCard`)
		on delete cascade
		on update cascade
);

CREATE TABLE `actor` (
  `aadharCard` BIGINT NOT NULL ,
  `experience` INT NOT NULL,
  `height` INT NOT NULL,
  `weight` INT NOT NULL,
  PRIMARY KEY (`aadharCard`),
  FOREIGN KEY (`aadharCard`) REFERENCES `person` (`aadharCard`) ON DELETE CASCADE,
CHECK (experience >= 0 and height > 0 and weight > 0)
);

CREATE TABLE `prefers`(
    `actorAadharCard` BIGINT NOT NULL,
    `brandName` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`actorAadharCard`, `brandName`),
    FOREIGN KEY (`actorAadharCard`) REFERENCES `actor` (`aadharCard`) ON DELETE CASCADE,
    FOREIGN KEY (`brandName`) REFERENCES `brand` (`brandName`) ON DELETE CASCADE
);

create table `production` (
	`adSerialNo` int auto_increment primary key,
	`actorAadharCard` bigint not null,
	`directorAadharCard` bigint not null,
	`productName` varchar(255) not null,
	`brandName` varchar(255) not null,
	`signingDate` date not null,
	`productionCost` int not null,
	check (`productionCost` >= 0),
	foreign key (`actorAadharCard`)
		references `actor` (`aadharCard`)
		on delete cascade,
	foreign key (`directorAadharCard`)
		references `director` (`aadharCard`)
		on delete cascade,
	foreign key (`productName`, `brandName`)
		references `product` (`name`, `brandName`)
		on delete cascade
);

create table `ad` (
	`serialNo` int primary key,
	`duration` int,
	check (`duration` > 0),
  foreign key (`serialNo`)
		references `production` (`adSerialNo`)
		on delete cascade
);

create table `adGenre` (
	`name` enum('Comedy', 'Thriller', 'Romance', 'Suspense', 'Sci-fi', 'Action', 'Horror', 'Fantasy'),
	`adSerialNo` int,
	primary key (`name`, `adSerialNo`),
	foreign key (`adSerialNo`)
		references `ad` (`serialNo`)
		on delete cascade
);

CREATE TABLE `show` (
  `date` DATE NOT NULL,
  `startTime` TIME NOT NULL,
  `channelName` VARCHAR(255) NOT NULL,
  `duration` INT NOT NULL,
  `surcharge` INT NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`date`, `startTime`, `channelName`),
  FOREIGN KEY (`channelName`) REFERENCES `channel` (`channelName`) ON DELETE CASCADE,
  CHECK (surcharge >= 0 and duration > 0)
);

CREATE TABLE `showGenre` (
  `name` enum('Comedy', 'Thriller', 'Romance', 'Suspense', 'Sci-fi', 'Action', 'Horror', 'Fantasy') NOT NULL,
  `showDate` DATE NOT NULL,
  `showStartTime` TIME NOT NULL,
  `channelName` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`showDate`, `showStartTime`, `channelName`, `name`),
  FOREIGN KEY (`showDate`, `showStartTime`, `channelName`) REFERENCES `show` (`date`, `startTime`, `channelName`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `displayedBetween` (
    `showDate` DATE NOT NULL,
    `showStartTime` TIME NOT NULL,
    `channelName` varchar(255) NOT NULL,
    `adSerialNo` INT NOT NULL,
    `timesShown` INT DEFAULT 1,
    PRIMARY KEY (
        `showDate`,
        `showStartTime`,
        `channelName`,
        `adSerialNo`
    ),
    FOREIGN KEY (`showDate`, `showStartTime`, `channelName`) REFERENCES `show` (`date`, `startTime`, `channelName`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`adSerialNo`) REFERENCES `ad` (`serialNo`) ON DELETE CASCADE,
    CHECK (timesShown > 0)
);

CREATE TABLE `juniorActor` (
  `aadharCard` BIGINT NOT NULL,
  PRIMARY KEY (`aadharCard`),
  FOREIGN KEY (`aadharCard`) REFERENCES `actor` (`aadharCard`) ON DELETE CASCADE
);

CREATE TABLE `guardianData` (
  `aadharCard` BIGINT NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` BIGINT NOT NULL,
  PRIMARY KEY (`aadharCard`)
);

CREATE TABLE `guardian` (
  `jActorAadharCard` BIGINT NOT NULL,
  `aadharCard` BIGINT NOT NULL,
  PRIMARY KEY (`aadharCard` , `jActorAadharCard`),
  FOREIGN KEY (`jActorAadharCard`) REFERENCES `juniorActor` (`aadharCard`) ON DELETE CASCADE,
  FOREIGN KEY (`aadharCard`) REFERENCES `guardianData` (`aadharCard`) ON DELETE CASCADE
);

DELIMITER $$
CREATE TRIGGER before_show_insert
BEFORE INSERT ON `show`
FOR EACH ROW
BEGIN
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
		signal sqlstate '45000' set message_text = 'The show is overlapping with other shows. Please change date, time or duration';
	end if;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER `before_displaying`
BEFORE INSERT ON `displayedBetween`
FOR EACH ROW
BEGIN
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
		signal sqlstate '45000' set message_text = 'Total Duration of Ads aired exceeds show duration';
	end if;

END$$
DELIMITER ;

INSERT INTO `person` (`aadharCard`,`name`,`accountNo`,`gender`,`DOB`) VALUES
(257691800359,"Forrest",293895034818,"Male","1993-09-12"),
(290722165251,"Imelda",195117667857,"Other","2004-02-12"),
(543278675609,"Dean",668334235465,"Male","2001-12-24"),
(475671876615,"Nigel",144083857152,"Male","2001-01-02"),
(897114443820,"Adam",99716021918,"Female","1981-07-11"),
(230687914469,"Lesley",852404298923,"Male","1983-05-31"),
(331440631972,"Indira",993432086651,"Female","1993-08-06"),
(261132474728,"Illana",630591625104,"Male","1990-06-15"),
(806784985109,"Dillon",356654289589,"Female","1993-10-25"),
(611761119375,"Allegra",268182069628,"Female","1988-06-30"),
(475546528070,"Baker",421251500464,"Male","1991-12-14"),
(743088703942,"Ralph",606985805090,"Female","1982-04-19"),
(289576609004,"Kamal",737758211018,"Male","1988-11-23"),
(987177520201,"Colby",521956628669,"Male","2001-11-05"),
(402264546504,"Kimberly",680176799652,"Male","1982-03-24"),
(288720001485,"Cynthia",522875225448,"Male","1996-04-08"),
(601609790887,"Zoe",33378897725,"Female","2004-07-06"),
(633703909581,"Boris",244114081678,"Male","1992-11-07"),
(696370762846,"Bruno",890939914812,"Male","1990-08-21"),
(315439533406,"Riley",879660132703,"Other","2006-11-24");

INSERT INTO `brand` (`brandName`,`pocEmail`,`pocPhone`) VALUES ("Nestle","netus@velesttempor.net","2903177783"),("Adidas","ultricies@placeratorcilacus.org","6620836486"),("Hamleys","vitae.semper.egestas@arcuSedeu.net","3919282002"),("tichnas","iaculis@penatibus.net","7069898351"),("McDonalds","sem.consequat@quamvelsapien.com","9623112183");

INSERT INTO `channel` (`channelName`,`basePrice`) VALUES ("Nickledeon",35527),("Disney",93317),("Aaj Tak",9691),("Sony",71950),("Animal Planet",5127);

INSERT INTO `director` (`aadharCard`, `joinDate`, `salary`, `supervisorAadharCard`) VALUES
(897114443820, "2001-01-10", 55000, NULL),
(230687914469, "2001-01-10", 55000, NULL),
(257691800359, "2002-03-12", 25000, 897114443820),
(543278675609, "2000-08-15", 25000, 897114443820),
(475671876615, "2000-09-14", 25000, 897114443820),
(331440631972, "2015-10-12", 25000, 230687914469),
(261132474728, "2015-10-12", 25000, 230687914469);

INSERT INTO `product` (`name`,`brandName`,`price`) VALUES ("Shoes","Hamleys",3298),("Maggi","Nestle",30),("Shoes","Adidas",5084),("T-Shirt","Adidas",4737),("T-Shirt","tichnas",1661),("Battery","tichnas",69647),("Book","Hamleys",872),("Nuggets","McDonalds",444),("Coffee","Nestle",600),("Shoes","tichnas",43843),("Laptop T17x","tichnas",268010);

INSERT INTO `phone` (`aadharCard`,`phoneNo`) VALUES (257691800359,5472368415),(290722165251,5478369821),(543278675609,2415789658),(475671876615,2547893214),(897114443820,2458963257),(230687914469,1257469825),(331440631972,3214536982),(261132474728,5874523698),(806784985109,2143698521),(611761119375,7587126985),(475546528070,2547369285),(743088703942,2478569821),(289576609004,2143698527),(987177520201,9876583216),(402264546504,4789685869),(288720001485,1225589876),(601609790887,2255479942),(633703909581,9988268745),(696370762846,8800565686),(315439533406,8800565685);

INSERT INTO `actor` (`aadharCard`, `experience`, `height`, `weight`) VALUES
(290722165251, 1, 150, 60),
(601609790887, 0, 145, 55),
(315439533406, 2, 120, 45),
(806784985109, 1, 155, 80),
(611761119375, 1, 157, 105),
(475546528070, 1, 160, 75),
(743088703942, 2, 165, 65),
(289576609004, 2, 172, 110),
(987177520201, 3, 162, 95),
(402264546504, 3, 152, 80),
(288720001485, 3, 165, 82),
(633703909581, 3, 90, 40),
(696370762846, 5, 155, 88);

INSERT INTO `prefers` (`brandName`,`actorAadharCard`) VALUES
("Nestle",290722165251),
("Nestle",315439533406),
("Nestle",402264546504),
("Adidas",601609790887),
("Adidas",315439533406),
("tichnas",290722165251),
("tichnas",601609790887),
("tichnas",315439533406),
("tichnas",402264546504),
("McDonalds",601609790887),
("McDonalds",402264546504);

INSERT INTO `production` (`actorAadharCard`,`directorAadharCard`,`productName`,`brandName`,`signingDate`,`productionCost`) VALUES
(290722165251,543278675609,"Shoes","Hamleys","2020-02-02",15000),
(601609790887,261132474728,"Book","Hamleys","2020-01-14",5000),
(315439533406,257691800359,"Nuggets","McDonalds","2020-03-20",7000),
(806784985109,543278675609,"Laptop T17x","tichnas","2020-04-07",18000),
(611761119375,261132474728,"Shoes","Hamleys","2020-02-18",2000),
(475546528070,331440631972,"T-Shirt","tichnas","2020-03-23",20000),
(987177520201,475671876615,"Shoes","Hamleys","2020-02-28",8000),
(987177520201,257691800359,"Coffee","Nestle","2020-02-04",4000),
(987177520201,257691800359,"Maggi","Nestle","2020-02-08",9000),
(475546528070,475671876615,"T-Shirt","Adidas","2020-10-02",12000);

INSERT INTO `ad` (`serialNo`,`duration`) VALUES (1,80),(2,108),(3,101),(4,73),(5,37),(6,29),(7,107),(8,48),(9,71),(10,78);

INSERT INTO `adGenre` (`adSerialNo`,`name`) VALUES (10,"Comedy"),(9,"Comedy"),(10,"Action"),(7,"Comedy"),(10,"Romance"),(1,"Comedy"),(7,"Suspense"),(4,"Comedy"),(3,"Thriller"),(5,"Romance"),(3,"Romance"),(8,"Suspense"),(6,"Comedy"),(4,"Action"),(4,"Thriller"),(6,"Fantasy"),(2,"Thriller");

INSERT INTO `show` (`date`,`startTime`,`channelName`,`duration`,`surcharge`,`name`) VALUES
(str_to_date("07-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",75,380,"Most Dangerous 10"),
(str_to_date("06-10-20", "%d-%m-%y"),"05:00:00","Animal Planet",75,843,"Deadliest in the Wild"),
(str_to_date("25-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",90,362,"Snakes"),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Animal Planet",105,631,"King of Jungle"),
(str_to_date("14-10-20", "%d-%m-%y"),"23:00:00","Sony",30,374,"Nach le India"),
(str_to_date("31-10-20", "%d-%m-%y"),"07:00:00","Sony",90,149,"Crime Patrol"),
(str_to_date("21-10-20", "%d-%m-%y"),"07:00:00","Aaj Tak",30,42,"Top 10"),
(str_to_date("08-10-20", "%d-%m-%y"),"09:00:00","Aaj Tak",120,838,"Aaj ki News"),
(str_to_date("19-10-20", "%d-%m-%y"),"07:00:00","Aaj Tak",105,68,"10 Breaking News"),
(str_to_date("14-10-20", "%d-%m-%y"),"05:00:00","Aaj Tak",60,183,"Jungle News"),
(str_to_date("19-10-20", "%d-%m-%y"),"18:00:00","Disney",120,489,"Doraemon"),
(str_to_date("22-10-20", "%d-%m-%y"),"11:00:00","Nickledeon",105,344,"Perman"),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Sony",75,280,"Pati Patni aur Wo"),
(str_to_date("06-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",90,182,"1000 years before"),
(str_to_date("07-10-20", "%d-%m-%y"),"18:00:00","Sony",90,712,"mollis"),
(str_to_date("17-10-20", "%d-%m-%y"),"18:00:00","Animal Planet",60,492,"Jungle Jungle"),
(str_to_date("13-10-20", "%d-%m-%y"),"15:00:00","Nickledeon",105,16,"Ninja Hattori"),
(str_to_date("20-10-20", "%d-%m-%y"),"18:00:00","Disney",120,143,"Shinchan"),
(str_to_date("02-10-20", "%d-%m-%y"),"18:00:00","Disney",90,435,"Jake and Pirate"),
(str_to_date("12-10-20", "%d-%m-%y"),"11:00:00","Nickledeon",105,729,"Art Attack");

INSERT INTO `showGenre` (`name`, `showDate`, `showStartTime`, `channelName`) VALUES
("Thriller", str_to_date("07-10-20", "%d-%m-%y"),"09:00:00","Animal Planet"),
("Thriller", str_to_date("06-10-20", "%d-%m-%y"),"05:00:00","Animal Planet"),
("Comedy", str_to_date("25-10-20", "%d-%m-%y"),"09:00:00","Animal Planet"),
("Thriller" ,str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Animal Planet"),
("Comedy", str_to_date("14-10-20", "%d-%m-%y"),"23:00:00","Sony"),
("Suspense", str_to_date("31-10-20", "%d-%m-%y"),"07:00:00","Sony"),
("Comedy", str_to_date("19-10-20", "%d-%m-%y"),"18:00:00","Disney"),
("Comedy", str_to_date("22-10-20", "%d-%m-%y"),"11:00:00","Nickledeon"),
("Comedy", str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Sony"),
("Romance", str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Sony"),
("Action", str_to_date("07-10-20", "%d-%m-%y"),"18:00:00","Sony"),
("Comedy", str_to_date("13-10-20", "%d-%m-%y"),"15:00:00","Nickledeon"),
("Comedy", str_to_date("20-10-20", "%d-%m-%y"),"18:00:00","Disney"),
("Comedy", str_to_date("02-10-20", "%d-%m-%y"),"18:00:00","Disney"),
("Comedy", str_to_date("12-10-20", "%d-%m-%y"),"11:00:00","Nickledeon");

INSERT INTO `displayedBetween` (`showDate`, `showStartTime`, `channelName`, `adSerialNo`, `timesShown`) VALUES
(str_to_date("07-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",1,2),
(str_to_date("07-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",3,3),
(str_to_date("07-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",5,4),
(str_to_date("07-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",7,1),
(str_to_date("07-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",8,1),
(str_to_date("06-10-20", "%d-%m-%y"),"05:00:00","Animal Planet",1,2),
(str_to_date("06-10-20", "%d-%m-%y"),"05:00:00","Animal Planet",3,2),
(str_to_date("06-10-20", "%d-%m-%y"),"05:00:00","Animal Planet",5,3),
(str_to_date("06-10-20", "%d-%m-%y"),"05:00:00","Animal Planet",7,3),
(str_to_date("06-10-20", "%d-%m-%y"),"05:00:00","Animal Planet",8,2),
(str_to_date("25-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",1,3),
(str_to_date("25-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",3,5),
(str_to_date("25-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",5,1),
(str_to_date("25-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",7,1),
(str_to_date("25-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",8,1),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Animal Planet",1,6),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Animal Planet",3,2),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Animal Planet",5,1),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Animal Planet",7,3),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Animal Planet",8,2),
(str_to_date("14-10-20", "%d-%m-%y"),"23:00:00","Sony",2,2),
(str_to_date("14-10-20", "%d-%m-%y"),"23:00:00","Sony",4,3),
(str_to_date("14-10-20", "%d-%m-%y"),"23:00:00","Sony",6,1),
(str_to_date("14-10-20", "%d-%m-%y"),"23:00:00","Sony",8,1),
(str_to_date("31-10-20", "%d-%m-%y"),"07:00:00","Sony",2,1),
(str_to_date("31-10-20", "%d-%m-%y"),"07:00:00","Sony",4,2),
(str_to_date("31-10-20", "%d-%m-%y"),"07:00:00","Sony",8,2),
(str_to_date("19-10-20", "%d-%m-%y"),"18:00:00","Disney",2,1),
(str_to_date("19-10-20", "%d-%m-%y"),"18:00:00","Disney",4,2),
(str_to_date("19-10-20", "%d-%m-%y"),"18:00:00","Disney",6,3),
(str_to_date("19-10-20", "%d-%m-%y"),"18:00:00","Disney",8,1),
(str_to_date("22-10-20", "%d-%m-%y"),"11:00:00","Nickledeon",2,4),
(str_to_date("22-10-20", "%d-%m-%y"),"11:00:00","Nickledeon",4,3),
(str_to_date("22-10-20", "%d-%m-%y"),"11:00:00","Nickledeon",6,1),
(str_to_date("22-10-20", "%d-%m-%y"),"11:00:00","Nickledeon",8,2),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Sony",2,2),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Sony",4,1),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Sony",6,1),
(str_to_date("05-10-20", "%d-%m-%y"),"23:00:00","Sony",8,1),
(str_to_date("06-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",1,2),
(str_to_date("06-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",3,1),
(str_to_date("06-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",5,1),
(str_to_date("06-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",7,2),
(str_to_date("06-10-20", "%d-%m-%y"),"09:00:00","Animal Planet",8,2),
(str_to_date("17-10-20", "%d-%m-%y"),"18:00:00","Animal Planet",1,4),
(str_to_date("17-10-20", "%d-%m-%y"),"18:00:00","Animal Planet",2,2),
(str_to_date("17-10-20", "%d-%m-%y"),"18:00:00","Animal Planet",8,2),
(str_to_date("13-10-20", "%d-%m-%y"),"15:00:00","Nickledeon",2,2),
(str_to_date("13-10-20", "%d-%m-%y"),"15:00:00","Nickledeon",4,5),
(str_to_date("13-10-20", "%d-%m-%y"),"15:00:00","Nickledeon",6,3),
(str_to_date("13-10-20", "%d-%m-%y"),"15:00:00","Nickledeon",8,1),
(str_to_date("20-10-20", "%d-%m-%y"),"18:00:00","Disney",2,4),
(str_to_date("20-10-20", "%d-%m-%y"),"18:00:00","Disney",4,5),
(str_to_date("20-10-20", "%d-%m-%y"),"18:00:00","Disney",6,2),
(str_to_date("20-10-20", "%d-%m-%y"),"18:00:00","Disney",8,2),
(str_to_date("02-10-20", "%d-%m-%y"),"18:00:00","Disney",2,6),
(str_to_date("02-10-20", "%d-%m-%y"),"18:00:00","Disney",4,4),
(str_to_date("02-10-20", "%d-%m-%y"),"18:00:00","Disney",6,2),
(str_to_date("02-10-20", "%d-%m-%y"),"18:00:00","Disney",8,2),
(str_to_date("12-10-20", "%d-%m-%y"),"11:00:00","Nickledeon",2,3),
(str_to_date("12-10-20", "%d-%m-%y"),"11:00:00","Nickledeon",4,2),
(str_to_date("12-10-20", "%d-%m-%y"),"11:00:00","Nickledeon",6,1),
(str_to_date("12-10-20", "%d-%m-%y"),"11:00:00","Nickledeon",8,1);

INSERT INTO `juniorActor` (`aadharCard`) VALUES (290722165251),(601609790887),(315439533406);

INSERT INTO `guardianData` (`aadharCard`,`name`,`phone`) VALUES (245369852145,"Rajesh",9868652145),(986321456325,"Mehak",9832145687),(523478235896,"Rahul",6845721398);

INSERT INTO `guardian` (`jActorAadharCard`,`aadharCard`) VALUES (290722165251,245369852145),(601609790887,986321456325),(315439533406,523478235896);

