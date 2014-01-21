
drop table if exists routes;
create table routes (
  id integer primary key,
  routeType text,
  rating text,
  rope integer,
  name text,
  dateSet text,
  setter text,
  color1 text,
  color2 text,
  specialBase text,
  blurb text,
  updater text 
);
create table colors(
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