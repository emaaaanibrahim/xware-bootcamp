### Create a new transaction :
```sql
begin;
```
________________________________________________________________________________________________________________________________________________________
### Insert a new record into the Professor table :
```sql insert into professor  (name,age,image,faculty_id,department_id)  values ('soad',30,bytea('/home/eman/Templates'),1,2);
```
_________________________________________________________________________________________________________________________________________________________
### Insert a new record into the Student table :
```sql insert into student  (name,age,address,phone,image,birth_date,course_id,address_id,height)  values ('lara',22,'eeee',0012,bytea('/home/eman/Templates'),20,18,1,160);
```
_________________________________________________________________________________________________________________________________________________________
### Select all the Professors and students :
```sql select * from professor;
select * from student;
```
_________________________________________________________________________________________________________________________________________________________
### Return to the first session and delete the Professors with the salary greater than 20000 :
```sql delete from professor where salary > 2000;
```
_________________________________________________________________________________________________________________________________________________________
Return to the first session and rollback the transaction :
```sql rollback; 
```
_________________________________________________________________________________________________________________________________________________________
### Return to the first session Start a new transaction :
```sql begin;
```
_________________________________________________________________________________________________________________________________________________________
### Insert a new record into the Professor table :
### Insert a new record into the Student table :
```sql insert into professor  (name,age,image,faculty_id,department_id)  values ('salwa',30,bytea('/home/eman/Templates'),1,2);
insert into student  (name,age,address,phone,image,birth_date,course_id,address_id,height)  values ('samar',22,'eeee',0012,bytea('/home/eman/Templates'),20,18,1,160);
```
_________________________________________________________________________________________________________________________________________________________
### Commit the transaction :
```sql commit;
```
________________________________________________________________________________________________________________________________________________________
### Select Subject id, Subject Name, Subject Code, Course Duration in One Query :
```sql select subject.name,subject.code,course.duration from subject inner join course on subject.id=course.subject_id;
```
________________________________________________________________________________________________________________________________________________________
### Select Subject id, Subject Name, Subject Code, Course Duration, Professor First_name, Professor Last_name, in One Query :
```sql select subject.name,subject.code,course.duration ,professor.name from subject inner join course on subject.id=course.subject_id inner join professor on subject.id=professor.id;
```
________________________________________________________________________________________________________________________________________________________
### Select All Students With Thier Address In one Query
```sql select select student.address from student inner join course on subject.id=course.subject_id inner join on professor subject.id=professor.id;
SELECT * FROM student FULL OUTER JOIN address on address.id = student.id;
```
________________________________________________________________________________________________________________________________________________________
### Select All Student Name In Every Couse.
```sql SELECT * FROM student FULL OUTER JOIN address on address.id = student.id; 
```
__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


### link : https://pgexercises.com/questions/joins/simplejoin.html
  solution : ```sql select cd.bookings.starttime from cd.bookings inner join cd.members on cd.members.memid=cd.bookings.memid where cd.members.firstname='David'and cd.members.surname='Farrell';  ```
  
### link : https://pgexercises.com/questions/joins/simplejoin2.html
   solution : ```sql select cd.bookings.starttime ,cd.facilities.name from cd.bookings inner join cd.facilities on cd.facilities.facid=cd.bookings.facid where cd.facilities.name like '%Tennis Court %' and cd.bookings.starttime >= '2012-09-21' and cd.bookings.starttime < '2012-09-22'  order by cd.bookings.starttime;
   ```
