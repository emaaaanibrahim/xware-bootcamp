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
