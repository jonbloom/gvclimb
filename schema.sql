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
INSERT INTO orderkeys VALUES('10d',7);
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

CREATE TABLE setters (id INTEGER PRIMARY KEY, name );

CREATE TABLE tapeColors (
  cssName text NOT NULL,
  realName text NOT NULL
);

CREATE TABLE users (id integer PRIMARY KEY, username text, password text, is_admin integer, attempted_ids text, sent_ids text, vote_ids text);

