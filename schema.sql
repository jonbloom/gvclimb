BEGIN TRANSACTION;
CREATE TABLE attempts (user NUMERIC, route_id NUMERIC);
CREATE TABLE colors(
  [7] text,
  [8] text,
  [9] text,
  [10a] text,
  [10b] text,
  [10c] text,
  [10d] text,
  [11a] text,
  [11b] text,
  [11c] text,
  [11d] text,
  [12a] text,
  [12b] text,
  [12c] text,
  [12d] text,
  [V0] text,
  [V1] text,
  [V2] text,
  [V3] text,
  [V4] text,
  [V5] text,
  [V6] text,
  [V7] text,
  [V8] text,
  [V9] text
);
INSERT INTO colors VALUES('hotpink','green','orange','blue','blue','black','black','red','red','yellow','yellow','white','white','purple','purple','hotpink','green','orange','blue','black','red','yellow','white','purple','purple');
CREATE TABLE orderkeys (rating TEXT, key INTEGER PRIMARY KEY);
INSERT INTO orderkeys VALUES(7,1);
INSERT INTO orderkeys VALUES(8,2);
INSERT INTO orderkeys VALUES(9,3);
INSERT INTO orderkeys VALUES('10a',4);
INSERT INTO orderkeys VALUES('10b',5);
INSERT INTO orderkeys VALUES('10c',6);
INSERT INTO orderkeys VALUES('10d
',7);
INSERT INTO orderkeys VALUES('11a',8);
INSERT INTO orderkeys VALUES('11b',9);
INSERT INTO orderkeys VALUES('11c',10);
INSERT INTO orderkeys VALUES('11d',11);
INSERT INTO orderkeys VALUES('12a',12);
INSERT INTO orderkeys VALUES('12b',13);
INSERT INTO orderkeys VALUES('12c',14);
INSERT INTO orderkeys VALUES('12d',15);
INSERT INTO orderkeys VALUES('V0',16);
INSERT INTO orderkeys VALUES('V1',17);
INSERT INTO orderkeys VALUES('V2',18);
INSERT INTO orderkeys VALUES('V3',19);
INSERT INTO orderkeys VALUES('V4',20);
INSERT INTO orderkeys VALUES('V5',21);
INSERT INTO orderkeys VALUES('V6',22);
INSERT INTO orderkeys VALUES('V7',23);
INSERT INTO orderkeys VALUES('V8',24);
INSERT INTO orderkeys VALUES('V9',25);
CREATE TABLE route_comm (route_id numeric, num_votes numeric);
INSERT INTO route_comm VALUES(87,0);
CREATE TABLE routes (id integer PRIMARY KEY, type text, rating text, rope integer, name text, date text, setter text, color_1 text, color_2 text, special_base text, blurb text, updater text);
INSERT INTO routes VALUES(4,'boulder','V3',1,'Rec Finals','10/15/13','Chloe Jelenc, David Foley','none','none','penguin','Rec Finals, V3, Rope 1','foleyda');
INSERT INTO routes VALUES(8,'boulder','V4',3,'The Apoplectic Rage of Nicolas Cage','10/20/13','Andrew Herring','hotpink','none','black','The Apoplectic Rage of Nicolas Cage, V4, Rope 3','herringa');
INSERT INTO routes VALUES(14,'boulder','V0',6,'Little Pink Elephants','10/20/13','Andrew Herring, Kelsey Evans','pink','none','hotpink','Little Pink Elephants, V0, Rope 6','herringa');
INSERT INTO routes VALUES(15,'boulder','V1',1,'Like Buttah','10/20/13','Andrew Herring','none','none','green','Like Buttah, V1, Rope 1','herringa');
INSERT INTO routes VALUES(16,'boulder','V1',7,'Half Dome','10/19/13','Joe Bitely','none','none','lightgreen','Half Dome, V1, Rope 7','herringa');
INSERT INTO routes VALUES(17,'boulder','V3',1,'Up Yours','10/19/13','Jordan Campbell','none','none','blue','Up Yours, V3, Rope 1','mcgeema');
INSERT INTO routes VALUES(18,'boulder','V9',3,360,'10/19/13','Jake Jensen','lightgreen','black','purple','360, V9, Rope 3','herringa');
INSERT INTO routes VALUES(20,'boulder','V0',11,60,'10/19/13','Joe Bitely','white','none','pink','60, V0, Rope 11','mcgeema');
INSERT INTO routes VALUES(21,'boulder','V8',4,340,'10/19/13','Guy Gordon','none','none','purple','340, V8, Rope 4','herringa');
INSERT INTO routes VALUES(22,'boulder','V8',2,350,'10/19/13','Kyle Stark','none','none','purple','350, V8, Rope 2','herringa');
INSERT INTO routes VALUES(25,'boulder','V7',5,330,'10/19/13','Jake Jensen','none','none','white','330, V7, Rope 5','herringa');
INSERT INTO routes VALUES(28,'boulder','V6',1,280,'10/19/13','Rob Veldman','none','none','yellow','280, V6, Rope 1','herringa');
INSERT INTO routes VALUES(29,'boulder','V6',4,300,'10/19/13','Rob Veldman','none','none','yellow','300, V6, Rope 4','jonbloom');
INSERT INTO routes VALUES(31,'boulder','V5',5,'Pumpkinception','10/19/13','Jordan Campbell','purple','none','red','Pumpkinception, V5, Rope 5','herringa');
INSERT INTO routes VALUES(33,'boulder','V1',4,120,'10/19/13','Kelsey Evans','none','none','lightgreen','120, V1, Rope 4','mcgeema');
INSERT INTO routes VALUES(34,'toprope','10a',2,'Top Rope Route 2','10/20/13','Dan Bologna','orange','white','blue','Top Rope Route 2, 5.10a, Rope 2','herringa');
INSERT INTO routes VALUES(36,'boulder','V1',10,100,'10/19/13','Becca Reyhl','pink','none','green','100, V1, Rope 10','mcgeema');
INSERT INTO routes VALUES(43,'toprope',8,8,'Mount Watkins (edit)','10/22/13','Joe Bitely','teal','none','green','Mount Watkins (edit), 8, Rope 8','jonbloom');
INSERT INTO routes VALUES(46,'toprope',9,2,'Orangellow','10/22/13','Jon Bloom','yellow','none','none','Orangellow, 5.9, Rope 2','jonbloom');
INSERT INTO routes VALUES(47,'boulder','V0',9,'Noo Bladder','10/19/13','Nick Chinzi','none','none','none','Noo Bladder, V0, Rope 9','jonbloom');
INSERT INTO routes VALUES(48,'boulder','V2',9,'Green Machine','10/19/13','Nick Chinzi','none','none','none','Green Machine, V2, Rope 9','herringa');
INSERT INTO routes VALUES(52,'toprope','10a',7,'Patty The Possum','10/22/13','Dan Bologna','lime','none','blue','Patty The Possum, 5.10a, Rope 7','herringa');
INSERT INTO routes VALUES(57,'toprope',9,7,'Free Hugs','10/23/13','Jon Bloom','blue','none','none','Free Hugs, 5.9, Rope 7','jonbloom');
INSERT INTO routes VALUES(58,'toprope',9,3,'Betty Nugs','10/29/13','Jordan Campbell','lightgreen','none','none','Betty Nugs, 5.9, Rope 3','herringa');
INSERT INTO routes VALUES(59,'toprope','10d',7,'Defibrilation','10/29/13','Andrew Herring','none','none','none','Defibrilation, 5.10d, Rope 7','herringa');
INSERT INTO routes VALUES(62,'boulder','V3',6,'Inspector Gadget','10/18/13','Joe Bitely','none','none','none','Inspector Gadget, V3, Rope 6','evankels');
INSERT INTO routes VALUES(63,'boulder','V3',5,210,'10/18/13','Becca Reyhl','none','none','lightblue','210, V3, Rope 5','evankels');
INSERT INTO routes VALUES(65,'toprope','10d',4,'Even I Got Pumped','10/31/13','Aaron Herndon','blue','none','none','Even I Got Pumped, 5.10d, Rope 4','foleyda');
INSERT INTO routes VALUES(66,'toprope','11a',4,'Strangely Reminiscent','11/03/13','Becca Reyhl','white','none','none','Strangely Reminiscent, 5.11a, Rope 4','foleyda');
INSERT INTO routes VALUES(68,'toprope','10a',3,'Trashin'' The Camp','11/13/13','Andrew Herring','none','none','teal','Trashin'' The Camp, 5.10a, Rope 3','herringa');
INSERT INTO routes VALUES(69,'boulder','V7',10,310,'10/19/13','Rob Veldman','none','none','none','310, V7, Rope 10','reyhlr');
INSERT INTO routes VALUES(70,'boulder','V1',4,'Santa Farts','11/19/13','Unknown','red','none','green','Santa Farts, V1, Rope 4','herringa');
INSERT INTO routes VALUES(71,'toprope','12b',4,'Venga, Venga!!','11/24/13','Andrew Herring','purple','none','white','Venga, Venga!!, 5.12b, Rope 4','herringa');
INSERT INTO routes VALUES(72,'toprope',9,1,'Turkey Baster','11/26/13','Dan Bologna','none','none','none','Turkey Baster, 5.9, Rope 1','reyhlr');
INSERT INTO routes VALUES(75,'toprope',9,3,'Jolly Old Sent Nick','12/05/13','Joe Bitely','purple','none','none','Jolly Old Sent Nick, 5.9, Rope 3','herringa');
INSERT INTO routes VALUES(76,'boulder','V2',3,'Ron Burgandy?','11/22/13','Climbing Class','teal','none','none','Ron Burgandy?, V2, Rope 3','herringa');
INSERT INTO routes VALUES(77,'boulder','V1',7,'Santa''s Crack','11/20/13','Climbing Class','red','none','none','Santa''s Crack, V1, Rope 7','herringa');
INSERT INTO routes VALUES(80,'toprope','10c',3,'Thin''N''Crispy','11/25/13','Dan Bologna','lightgreen','none','none','Thin''N''Crispy, 5.10c, Rope 3','herringa');
INSERT INTO routes VALUES(81,'boulder','V0',1,'Banana Split','11/20/13','Climbing Class','yellow','none','lightgreen','Banana Split, V0, Rope 1','herringa');
INSERT INTO routes VALUES(83,'toprope',9,4,'Best Route on Campus','10/22/13','Joe Bitely','none','none','none','Best Route on Campus, 5.9, Rope 4','reyhlr');
INSERT INTO routes VALUES(86,'toprope','10c',2,'Hand Tossed','11/25/13','Aaron Herndon','none','none','none','Hand Tossed, 5.10c, Rope 2','reyhlr');
INSERT INTO routes VALUES(87,'toprope',7,9,'HIPHOPOPOTOMUS','12/09/13','Cassie Miles','black','none','none','HIPHOPOPOTOMUS, 7, Rope 9','jonbloom');
INSERT INTO routes VALUES(88,'toprope','11a',11,'Down The Rabbit Hole','12/10/13','Andrew Herring','none','none','none','Down The Rabbit Hole, 5.11a, Rope 11','jonbloom');
INSERT INTO routes VALUES(89,'toprope','11a',6,'Elf''s Lament','12/12/13','Nick Anders','none','none','none','Elf''s Lament, 5.11a, Rope 6','herringa');
INSERT INTO routes VALUES(90,'toprope','10d',2,'Wahoooo','01/04/14','Aaron Tyner','lightgreen','white','none','Wahoooo, 5.10d, Rope 2','foleyda');
INSERT INTO routes VALUES(91,'boulder','V2',0,'Squiggle','01/04/14','Eric Carlson','lightgreen','none','none','Squiggle, V2, Rope ','foleyda');
INSERT INTO routes VALUES(92,'toprope','10b',5,'Dexter','01/04/14','Eric Carlson','hotpink','none','none','Dexter, 5.10b, Rope 5','foleyda');
INSERT INTO routes VALUES(93,'boulder','V3',10,'Who Put Dat Der??','01/09/14','Andrew Herring','none','none','none','Who Put Dat Der??, V3, Rope 10','jonbloom');
INSERT INTO routes VALUES(94,'boulder','V3',4,'Slightly Inappropiate','01/13/14','Andrew Herring','none','none','none','Slightly Inappropiate, V3, Rope 4','jonbloom');
INSERT INTO routes VALUES(95,'boulder','V7',11,'Kyle''s Route?','01/10/14','Kyle Stark','black','none','none','Kyle''s Route?, V7, Rope 11','foleyda');
INSERT INTO routes VALUES(96,'toprope',7,11,'Bask in the Glow','01/15/14','Jon Bloom','none','none','none','Bask in the Glow, 5.7, Rope 11','jonbloom');
INSERT INTO routes VALUES(97,'toprope','10a',1,'A Game of Risk','01/19/14','Golden Wrench','yellow','none','none','A Game of Risk, 5.10a, Rope 1','jonbloom');
INSERT INTO routes VALUES(98,'boulder','V3',1,'Golden Wrench 11','01/19/14','Golden Wrench','red','none','none','Golden Wrench 11, V3, Rope 1','jonbloom');
INSERT INTO routes VALUES(99,'boulder','V2',2,'Half and Half','01/19/14','Golden Wrench','hotpink','none','none','Half and Half, V2, Rope 2','jonbloom');
INSERT INTO routes VALUES(100,'boulder','V1',3,'The Sexy Carpenter','01/19/14','Golden Wrench','none','none','none','The Sexy Carpenter, V1, Rope 3','jonbloom');
INSERT INTO routes VALUES(101,'toprope',9,3,'It Gets Better (Or Not)','01/19/14','Golden Wrench','none','none','none','It Gets Better (Or Not), 5.9, Rope 3','jonbloom');
INSERT INTO routes VALUES(102,'boulder','V0',4,'My Valentine','01/20/14','Joe Bitely','red','none','none','My Valentine, V0, Rope 4','foleyda');
INSERT INTO routes VALUES(103,'toprope','10b',4,'24-Karats','01/19/14','Golden Wrench','blue','none','lightblue','24-Karats, 5.10b, Rope 4','jonbloom');
INSERT INTO routes VALUES(104,'boulder','V2',5,'Make Me Change The Tape','01/19/14','Golden Wrench','gray','none','none','Make Me Change The Tape, V2, Rope 5','jonbloom');
INSERT INTO routes VALUES(106,'boulder','V4',6,'Box','01/19/14','Golden Wrench','lime','none','none','Box, V4, Rope 6','jonbloom');
INSERT INTO routes VALUES(107,'boulder','V3',8,'The Blue Power Ranger','01/19/14','Golden Wrench','white','none','none','The Blue Power Ranger, V3, Rope 8','jonbloom');
INSERT INTO routes VALUES(108,'toprope',9,8,'It''s a 5.9?','01/19/14','Golden Wrench','white','none','none','It''s a 5.9?, 5.9, Rope 8','jonbloom');
INSERT INTO routes VALUES(109,'toprope','10a',8,'Pockets N'' StuF','01/19/14','Golden Wrench','black','none','none','Pockets N'' StuF, 5.10a, Rope 8','jonbloom');
INSERT INTO routes VALUES(110,'boulder','V4',9,'Alice in Wonderland','01/19/14','Golden Wrench','hotpink','none','none','Alice in Wonderland, V4, Rope 9','jonbloom');
INSERT INTO routes VALUES(111,'toprope',9,10,'Make-Out Point','01/19/14','Golden Wrench','lime','none','none','Make-Out Point, 5.9, Rope 10','jonbloom');
INSERT INTO routes VALUES(112,'toprope',8,10,'In the Cave','01/19/14','Joe Bitely','saddlebrown','none','none','In the Cave, 5.8, Rope 10','foleyda');
INSERT INTO routes VALUES(113,'toprope','10b',6,'6 Minutes to Spare','01/19/14','Golden Wrench','black','none','lightblue','6 Minutes to Spare, 5.10b, Rope 6','jonbloom');
INSERT INTO routes VALUES(114,'toprope','10b',3,'','03/20/14','Aaron Tyner, Andrew Herring, Andrew Zimny','none','none','none',', 10b, Rope 3','jonbloom');
INSERT INTO routes VALUES(115,'toprope',7,2,'adsf','03/04/14','Aaron Herndon, Aaron Tyner, Andrew Herring','none','none','none','adsf, 7, Rope 2','jonbloom');
CREATE TABLE setters (id INTEGER PRIMARY KEY, name );
INSERT INTO setters VALUES(6,'Joe Bitely');
INSERT INTO setters VALUES(7,'Mike Archer');
INSERT INTO setters VALUES(8,'Kyle Beall');
INSERT INTO setters VALUES(9,'Dan Bologna');
INSERT INTO setters VALUES(10,'Eric Carlson');
INSERT INTO setters VALUES(11,'Nick Chinzi');
INSERT INTO setters VALUES(12,'Carter del Rosario');
INSERT INTO setters VALUES(13,'Kelsey Evans');
INSERT INTO setters VALUES(14,'Guy Gordon');
INSERT INTO setters VALUES(15,'Clay Hansen');
INSERT INTO setters VALUES(17,'Andrew Herring');
INSERT INTO setters VALUES(18,'Chloe Jelenc');
INSERT INTO setters VALUES(19,'Jake Jensen');
INSERT INTO setters VALUES(20,'Maggie McGee');
INSERT INTO setters VALUES(21,'David Peterson');
INSERT INTO setters VALUES(22,'Becca Reyhl');
INSERT INTO setters VALUES(23,'Eli Smith');
INSERT INTO setters VALUES(24,'Kyle Stark');
INSERT INTO setters VALUES(25,'Aaron Tyner');
INSERT INTO setters VALUES(26,'Pete Watson');
INSERT INTO setters VALUES(27,'Andrew Zimny');
INSERT INTO setters VALUES(28,'Climbing Class');
INSERT INTO setters VALUES(29,'Unknown');
INSERT INTO setters VALUES(30,'Hanson Smith');
INSERT INTO setters VALUES(31,'David Foley');
INSERT INTO setters VALUES(32,'Rob Veldman');
INSERT INTO setters VALUES(33,'Rob Fortney');
INSERT INTO setters VALUES(34,'Jordan Campbell');
INSERT INTO setters VALUES(35,'Cassie Miles');
INSERT INTO setters VALUES(36,'Kristen Stauffer');
INSERT INTO setters VALUES(37,'Nick Anders');
INSERT INTO setters VALUES(38,'Golden Wrench');
INSERT INTO setters VALUES(40,'Aaron Herndon');
INSERT INTO setters VALUES(41,'Jon Bloom');
CREATE TABLE tapeColors (
  cssName text NOT NULL,
  realName text NOT NULL
);
INSERT INTO tapeColors VALUES('black','Black');
INSERT INTO tapeColors VALUES('white','White');
INSERT INTO tapeColors VALUES('blue','Dark Blue');
INSERT INTO tapeColors VALUES('lightblue','Light Blue');
INSERT INTO tapeColors VALUES('cyan','Sky Blue');
INSERT INTO tapeColors VALUES('gray','Gray');
INSERT INTO tapeColors VALUES('goldenrod','Gold');
INSERT INTO tapeColors VALUES('orange','Orange');
INSERT INTO tapeColors VALUES('purple','Purple');
INSERT INTO tapeColors VALUES('saddlebrown','Brown');
INSERT INTO tapeColors VALUES('yellow','Yellow');
INSERT INTO tapeColors VALUES('lightgreen','Light Green');
INSERT INTO tapeColors VALUES('green','Dark Green');
INSERT INTO tapeColors VALUES('lime','Lime Green');
INSERT INTO tapeColors VALUES('hotpink','Dark Pink');
INSERT INTO tapeColors VALUES('pink','Light Pink');
INSERT INTO tapeColors VALUES('red','Red');
INSERT INTO tapeColors VALUES('teal','Teal');
INSERT INTO tapeColors VALUES('plum','Light Purple');
CREATE TABLE users (id integer PRIMARY KEY, username text, password text, is_admin integer, attempted_ids text, sent_ids text, vote_ids text);
INSERT INTO users VALUES(0,'secret','d4defd57b629c3a67701650b7ec5179e',0,'','','');
INSERT INTO users VALUES(1,'jonbloom','0fd62be625eca7ce17abce14a1c58974',1,'11, 1, 1, 1, 45, 45, 43, 43, 96, 112, 72, 46, 58, 101, 75, 83, 57, 108, 111, 97, 34, 68, 52, 109, 103, 92, 113, 103, 113, 87, 87, 71, 87, 87, ','1, 45, 45, 45, 43, 96, 112, 72, 46, 58, 101, 75, 83, 57, 108, 111, 97, 34, 68, 52, 109, 92, 103, 113, 87, ','');
INSERT INTO users VALUES(9,'joebitely','384bbbd19b9141867cbaa5317b3fc635',1,'','','');
INSERT INTO users VALUES(35,'smitelij','8cc368b71de3966208f6d409511a2bfb',1,'','','');
INSERT INTO users VALUES(37,'maghrans','26a52342bc2ca85e4181922d1ac91275',0,'','','');
INSERT INTO users VALUES(39,'jelenc','c17d554a87596ae94f7b65485bb4b3aa',1,'','','');
INSERT INTO users VALUES(40,'mcgeema','357b19283454e19753c9b8c5c48eac20',1,'','','');
INSERT INTO users VALUES(41,'reyhlr','23d45b337ff85d0a326a79082f7c6f50',1,'59, 46, 27, 14, 47, 20, 3133, 16, 36, 3, 38, 48, 37, 4, 17, 63, 62, 6, 8, 8, 41, 40, 40, 11, 31, 31, 28, 28, 5, 25, 60, 18, 23, 19, 21, 22, 35, 15, 33, 29, 34, 12, 69, 44, ','59, 46, 27, 14, 47, 20, 3133, 16, 36, 3, 38, 48, 37, 4, 17, 63, 62, 6, 8, 41, 40, 11, 31, 28, 5, 35, 15, 33, 29, 34, 12, 69, 44, ','');
INSERT INTO users VALUES(42,'foleyda','5298e22a3f0c87d47ffda9c43e286542',1,'3, 4, 6, 14, 143, 7, 27, 47, 20, 333, 16, 36, 38, 48, 37, 17, 8, 41, 40, 44, 28, 29, 12, 25, 66, 59, 65, 56, 43, 45, 35, 15, 15, 35, 35, 35, 15, 33, 63, 62, 44, 31, 64, 64, 64, 5, 11, 29, 26, 26, 26, 26, 26, 67, 52, 57, ','3, 4, 6, 14, 143, 7, 27, 47, 20, 333, 16, 36, 38, 48, 37, 17, 8, 59, 56, 43, 45, 15, 35, 33, 63, 62, 44, 64, 5, 11, 29, 67, 52, 57, ','');
INSERT INTO users VALUES(44,'greenman','dd3597850291b6dc8632d1af7a1e4ef3',0,'','','');
INSERT INTO users VALUES(45,'appletest','8d8b2742ed44a7d5714c77036fb36d53',0,'','','');
INSERT INTO users VALUES(46,'testUser','098f6bcd4621d373cade4e832627b4f6',0,'','','');
INSERT INTO users VALUES(47,'evankels','64677c888a176e09c011b31a25cbf443',1,'','52, 27, 147, 20, 35, 15, 33, 16, 36, 38, 48, ','');
INSERT INTO users VALUES(48,'cosantoiri','0cae7a3215298f1e9195d7b85367e4a5',0,'','','');
INSERT INTO users VALUES(49,'amydyer','94d21537442390fd26143c06e2a1ae4e',0,'38, 38, 38, 48, 35, 15, 33, 16, 36, 27, 20, 14, 3, 37, 4, 8, 47, 27, 14, 20, ','38, 38, 38, 48, 35, 15, 33, 16, 36, 47, 27, 14, 20, ','');
INSERT INTO users VALUES(51,'morte239','112bdd960695aa1e3727a957a33f49f4',0,'','','');
INSERT INTO users VALUES(52,'dejongma','1acd63e559452432f852a793d8a8cfa2',0,'','','');
INSERT INTO users VALUES(53,'g01096867','eb1f0eca265f6261474e50313ba765ac',0,'','','');
INSERT INTO users VALUES(54,'GabRiel','bf4d586a05533a6a773bc08ac698a19a',0,'','','');
INSERT INTO users VALUES(55,'william.power.05','e84a4a960986b0a948f49b368455ce37',0,'','','');
INSERT INTO users VALUES(57,'herringa','b99b77857bfb4f480279f86112194957',1,'','','');
INSERT INTO users VALUES(58,'climberswag','74c915f87a5d597d99f4feb1e07cf353',0,'','','');
INSERT INTO users VALUES(59,'Jason','b0b34bd800698b63148346f23690501b',0,'','','');
INSERT INTO users VALUES(60,'jcorotis85','154e1fbbe07fdf28996792bb92db700c',0,'','','');
INSERT INTO users VALUES(61,'jewelhaji','d22858184095a8ba31c86fde0ed915b1',0,'','','');
INSERT INTO users VALUES(62,'moorend','d9b23ebbf9b431d009a20df52e515db5',0,'','','');
INSERT INTO users VALUES(63,'alecmmark','da443a0ad979d5530df38ca1a74e4f80',0,'','','');
INSERT INTO users VALUES(64,'Andy_Staff','0e8e174968faccbf4956e3d9e774c199',0,'','','');
INSERT INTO users VALUES(65,'thevince','e28bc10a4566f58b2f5224ad2dfd8718',0,'','','');
INSERT INTO users VALUES(66,'campbjor','6b9619a061a9ae0c6bb24dc91ce7d5a2',1,'','','');
INSERT INTO users VALUES(67,'MVP117','647a9dcff8b1d602f98a798448c123e2',0,'','','');
INSERT INTO users VALUES(68,'NGerk','d2c0e5def09525b0916bdebdf20fa97a',0,'24, 14, 15, 35, 36, 27, 33, 16, 39, 20, 48, 38, ','24, 14, 15, 35, 36, 27, 33, 16, 39, 20, 48, 38, ','');
INSERT INTO users VALUES(69,'alberto','83b4ef5ae4bb360c96628aecda974200',0,'','','');
INSERT INTO users VALUES(70,'Ethan','c29f9eefba0fb64a7d9bffb4924ab700',0,'15, 48, 7, 55, ','15, 48, 7, 55, ','');
INSERT INTO users VALUES(71,'caiti','5d8da1150c369db217ed0d253a239be7',0,'','','');
INSERT INTO users VALUES(72,'sophia','26d1f0835953d8076811a39ea5d8ae48',0,'','','');
INSERT INTO users VALUES(73,'bhberson','9d9c955824042fff1b5def3e83be8d9f',0,'','','');
INSERT INTO users VALUES(74,'AaronGreenman','9a48f0c8868feb6da80aa24c3943a17a',0,'27, 14, 24, 20, 35, 15, 33, 16, 36, 37, 47, 7, 45, 58, 38, 48, 3, 4, 6, 62, 56, 57, 38, 43, 67, 70, 17, ','27, 14, 24, 20, 35, 15, 33, 16, 36, 37, 47, 7, 45, 58, 62, 56, 38, 43, 70, ','');
INSERT INTO users VALUES(75,'sartinij','c3c362036e59ba269f2b13a161f34b43',0,'','','');
INSERT INTO users VALUES(76,'wujcik','deff070b8cea64ef517839e64c308e66',0,'52, 46, 45, 55, 7, 43, 56, 17, 14, 27, 4, 36, 59, 68, 58, 57, 47, 47, 62, 20, 16, 73, 72, 15, 3, 37, 78, 68, 34, 83, 83, 84, 84, 75, 75, 85, 92, ','52, 46, 45, 55, 7, 43, 56, 14, 27, 36, 34, 58, 57, 47, 62, 20, 16, 73, 72, 15, 37, 78, 68, 83, 84, 75, ','');
INSERT INTO users VALUES(77,'Josh','e9ada8c82495598e5943e8ebe1bd80fa',0,'27, 14, 8, 7, 45, 58, ','27, 14, 7, 45, 58, ','');
INSERT INTO users VALUES(78,'murpryan','a9b9d067512f021d1b524795b06b5835',0,'38, 3, 47, 45, 46, ','38, 47, 45, 46, ','');
INSERT INTO users VALUES(79,'sless','724de616bac0070cfa210c254c10561c',0,'16, 47, 14, 48, 27, 36, 3, 33, 35, 70, 4, 20, 81, 79, 77, 76, ','16, 38, 47, 14, 48, 27, 36, 33, 35, 20, 81, 79, 77, ','');
INSERT INTO users VALUES(80,'dt','e5645dd85deb100fd1d71d0e8d671091',0,'4, 4, 44, 8, 3, 28, 28, 63, 12, 12, 29, ','4, 44, 8, 3, 28, 63, 29, ','');
INSERT INTO users VALUES(81,'whitmanm','4372759b203facdba2e3705393f9c286',0,'14, 19, 7, 7, 7, 47, 47, 27, 16, 20, 36, 81, ','47, 20, 36, ','');
INSERT INTO users VALUES(82,'hennella','ed8b28e8ef2ae22d303cb499e71f5878',0,'14, 14, 56, 57, 27, 47, 36, 4, 45, 43, 52, 7, 33, 16, 70, 72, 81, 20, 77, 81, 76, 17, 31, 48, 79, 15, 102, 104, 83, 75, ','14, 56, 27, 47, 36, 43, 7, 16, 62, 72, 20, 77, 81, 48, 15, 102, 83, 75, ','');
INSERT INTO users VALUES(83,'','d41d8cd98f00b204e9800998ecf8427e',0,'','','');
INSERT INTO users VALUES(84,'taylortarbox','2f7b22bac3f5542bb48fb08b04141ecb',0,'','','');
INSERT INTO users VALUES(85,'beccasiwicki','bff1128067be882ae72c50756863e13e',0,'14, 14, 47, 16, 3, 16, 14, 4, ','16, 14, ','');
INSERT INTO users VALUES(86,'pataroc','aa0a3d0fd767b27a579c400cee7120e9',0,'','','');
INSERT INTO users VALUES(87,'radosevd ','d3c9f43c6f609f3407512bf0b22c8dc1',0,'77, 77, 77, 36, 36, 81, 81, ','77, 36, 81, ','');
INSERT INTO users VALUES(88,'hepnerj','aa41efe0a1b3eeb9bf303e4561ff8392',0,'','','');
INSERT INTO users VALUES(89,'Stephen Wineski','813502586c44a388d63e134989e8b469',0,'81, 47, 77, ','14, 14, 14, 14, 14, 14, 81, 47, 77, ','');
INSERT INTO users VALUES(90,'kellijo52','f84461954fa39ad94b2a365bc4d7f0da',0,'56, 45, 74, 16, 47, 15, 20, 20, 27, 33, 35, 36, 36, 82, 14, ','56, 45, 43, 74, 16, 47, 15, 20, 27, 33, 35, 36, 82, 14, ','');
INSERT INTO users VALUES(91,'kinterw','1a77b201f6a9ad5c756a966f8e3775a3',0,'','','');
INSERT INTO users VALUES(92,'tuckerau','ddebf14c5a5dc7f9cb91e3c38e74158a',0,'62, 62, 111, 111, ','62, 111, ','');
COMMIT;
