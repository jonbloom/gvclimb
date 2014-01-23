CREATE TABLE attempts (user TEXT, route_id NUMERIC);
CREATE TABLE colors(
  [7] text,  [8] text,  [9] text, 
  [10a] text,  [10b] text,  [10c] text,  [10d] text,
  [11a] text,  [11b] text,  [11c] text,  [11d] text,
  [12a] text,  [12b] text,  [12c] text,  [12d] text,
  [V0] text,   [V1] text,   [V2] text,   [V3] text,
  [V4] text,   [V5] text,   [V6] text,   [V7] text,
  [V8] text,   [V9] text
);
CREATE TABLE orderkeys (
  rating TEXT, key INTEGER PRIMARY KEY
);
CREATE TABLE routes (
  id integer PRIMARY KEY, type text, rating text, 
  rope integer, name text, date text, setter text, 
  color_1 text, color_2 text, special_base text, 
  blurb text, updater text)
;
CREATE TABLE setters (
  id INTEGER PRIMARY KEY, name 
);
CREATE TABLE tapeColors (
  cssName text NOT NULL,
  realName text NOT NULL
);
CREATE TABLE users (id integer PRIMARY KEY, 
  username text, password text, is_admin integer, 
  attempted_ids text, sent_ids text)
;