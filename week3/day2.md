# Ex:1

### Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one. After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter. The query result format is in the following example.


```sql
sudo -u postgres psql 
``` 
```sql
\c information
```
```sql
insert into person (email) values ('john@example.com');
insert into person (email) values ('bob@example.com');
insert into person (email) values ('john@example.com');
insert into person (email) values ('john@example.com');
```

```
select * from person ;

 id |      email       
----+------------------
  1 | john@example.com
  2 | bob@example.com
  3 | john@example.com
```

```sql
delete from person a using person b where a.id>b.id and a.email=b.email;
```
```
select * from person ;

 id |      email       
----+------------------
  1 | john@example.com
  2 | bob@example.com
```
_________________________________________________________________________________________________________________________________________________________

# Ex:2
### Write an SQL query to report the latest login for all users in the year 2020. Do not include the users who did not login in 2020. Return the result table in any order.

```
create table logins (

   id int ,
   time_stamp timestamp ,
   PRIMARY KEY (id,time_stamp )


);
```

```sql
insert into logins (id,time_stamp) values (6,'2020-06-30 15:06:07');
insert into logins (id,time_stamp) values (6,'2021-04-21 14:06:06'); 
insert into logins (id,time_stamp) values (6,'2019-03-07 00:18:15'); 
insert into logins (id,time_stamp) values (8,'2020-02-01 05:10:53'); 
insert into logins (id,time_stamp) values (8,'2020-12-30 00:46:50'); 
insert into logins (id,time_stamp) values (2,'2020-01-16 02:49:50'); 
insert into logins (id,time_stamp) values (2,'2019-08-25 07:59:08 '); 
insert into logins (id,time_stamp) values (14,'2019-07-14 09:00:00'); 
```



```sql
select * from logins;
```

```
 id |     time_stamp      
----+---------------------
  6 | 2020-06-30 15:06:07
  6 | 2021-04-21 14:06:06
  6 | 2019-03-07 00:18:15
  8 | 2020-02-01 05:10:53
  8 | 2020-12-30 00:46:50
  2 | 2020-01-16 02:49:50
  2 | 2019-08-25 07:59:08
 14 | 2019-07-14 09:00:00
 14 | 2021-01-06 11:59:59
(9 rows)
```


```sql
select id , max(time_stamp) as last_stamp from logins where time_stamp >='2020-1-1'and time_stamp < '2021-1-1' group by id ;
```

```
id |     last_stamp      
----+---------------------
  2 | 2020-01-16 02:49:50
  6 | 2020-06-30 15:06:07
  8 | 2020-12-30 00:46:50
(3 rows)
```






























