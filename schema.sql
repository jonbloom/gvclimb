
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