sudo -u postgres psql 
\c information
insert into person (email) values ('john@example.com');
insert into person (email) values ('bob@example.com');
insert into person (email) values ('john@example.com');
insert into person (email) values ('john@example.com');


select * from person ;

 id |      email       
----+------------------
  1 | john@example.com
  2 | bob@example.com
  3 | john@example.com


delete from person a using person b where a.id>b.id and a.email=b.email;


select * from person ;
 id |      email       
----+------------------
  1 | john@example.com
  2 | bob@example.com

