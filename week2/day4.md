# Exercise 1
Try To Normalize Student, Professor Table in College Management System. How de we do that? 

create table grade_student (

   id serial primary key ,
   age varchar(50)  ,
   birth_date int  ,
   student_id int references student(id) 
);

insert into grade_student (age,birth_date,student_id)values(20,14,1),(7,20,6),(10,20,7);

select * from grade_student;
id | age | birth_date | student_id 
----+-----+------------+------------
  1 | 20  |         14 |          1
  2 | 7   |         20 |          6
  3 | 10  |         20 |          7



select * from student;
 id | name | age | address | phone |                   image                    | birth_date | course_id | address_id | height 
----+------+-----+---------+-------+--------------------------------------------+------------+-----------+------------+--------
  1 | eman |  20 | helali  | 1111  | \x2f686f6d652f656d616e2f54656d706c61746573 | 14         |        18 |          1 |       
  6 | lara |   7 | eeee    | 12    | \x2f686f6d652f656d616e2f54656d706c61746573 | 20         |        18 |          1 |    160
  7 | lara |  10 | eeee    | 12    | \x2f686f6d652f656d616e2f54656d706c61746573 | 20         |        18 |          1 |    160



alter table student  drop column age ; 
alter table student  drop column birth_date ; 
select * from student;
id | name | address | phone |                   image                    | course_id | address_id | height 
----+------+---------+-------+--------------------------------------------+-----------+------------+--------
  1 | eman | helali  | 1111  | \x2f686f6d652f656d616e2f54656d706c61746573 |        18 |          1 |       
  6 | lara | eeee    | 12    | \x2f686f6d652f656d616e2f54656d706c61746573 |        18 |          1 |    160
  7 | lara | eeee    | 12    | \x2f686f6d652f656d616e2f54656d706c61746573 |        18 |          1 |    160
(3 rows)


select student.id , student.name, student.address,student.phone,student.image,student.course_id,student.address_id,student.height,grade_student.age,grade_student.birth_date from student inner join grade_student on student.id = grade_student.student_id;

 id | name | address | phone |                   image                    | course_id | address_id | height | age | birth_date 
----+------+---------+-------+--------------------------------------------+-----------+------------+--------+-----+------------
  1 | eman | helali  | 1111  | \x2f686f6d652f656d616e2f54656d706c61746573 |        18 |          1 |        | 20  |         14
  6 | lara | eeee    | 12    | \x2f686f6d652f656d616e2f54656d706c61746573 |        18 |          1 |    160 | 7   |         20
  7 | lara | eeee    | 12    | \x2f686f6d652f656d616e2f54656d706c61746573 |        18 |          1 |    160 | 10  |         20


_______________________________________________________________________________________________________________________________________________________________________________

create table retired_professor (

   id serial primary key ,
   age varchar(50)  ,
   professor_id int references professor(id) 
);



select * from professor;
id | name  | age |                   image                    | faculty_id | department_id 
----+-------+-----+--------------------------------------------+------------+---------------
  6 | sara  |  20 | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             1
 11 | soad  |  10 | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 12 | soad  |  15 | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 13 | soad  | 100 | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 14 | soad  | 150 | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 15 | soad  |  15 | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 16 | soad  |  13 | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 17 | salwa | 180 | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             1



select * from retired_professor;
insert into retired_professor (age,professor_id)values(20,6),(10,11),(15,12),(100,13),(150,14),(15,15),(13,16),(180,17);
id | age | professor_id 
----+-----+--------------
  1 | 20  |            6
  2 | 10  |           11
  3 | 15  |           12
  4 | 100 |           13
  5 | 150 |           14
  6 | 15  |           15
  7 | 13  |           16
  8 | 180 |           17
  
  
  
 alter table professor  drop column age ; 
 select * from professor;
id | name  |                   image                    | faculty_id | department_id 
----+-------+--------------------------------------------+------------+---------------
  6 | sara  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             1
 11 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 12 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 13 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 14 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 15 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 16 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2
 17 | salwa | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             1
(8 rows)

select professor.id , professor.name, professor.image,professor.faculty_id,professor.department_id,retired_professor.age from professor inner join retired_professor on professor.id = retired_professor.professor_id ;

id | name  |                   image                    | faculty_id | department_id | age 
----+-------+--------------------------------------------+------------+---------------+-----
  6 | sara  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             1 | 20
 11 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2 | 10
 12 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2 | 15
 13 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2 | 100
 14 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2 | 150
 15 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2 | 15
 16 | soad  | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             2 | 13
 17 | salwa | \x2f686f6d652f656d616e2f54656d706c61746573 |          1 |             1 | 180



________________________________________________________________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________________________________________________________________


create table person (

   id serial primary key ,
    firstname varchar(50) ,
	lastname varchar(50) 


);

create table address (

   id serial primary key ,
   city varchar(50)  ,
   state varchar (50) ,
   person_id int references person(id) 
);

insert into person (firstname,lastname) values ('Allen','Wang');
insert into person (firstname,lastname) values ('Bob','Alice');
select * from person ;
id | firstname | lastname 
----+-----------+----------
  1 | Allen     | Wang
  2 | Bob       | Alice

insert into address (city,state,person_id) values ('New York City','New York',2) ;

insert into address (city,state,person_id) values ('Leetcode','California',1) ;

select * from address ;
 id |     city      |   state    | person_id 
----+---------------+------------+-----------
  1 | New York City | New York   |         2
  5 | Leetcode      | California |         1


select person.firstname,person.lastname,address.city,address.state from person inner join address on person.id =address.person_id;

 firstname | lastname |     city      |   state    
-----------+----------+---------------+------------
 Bob       | Alice    | New York City | New York
 Allen     | Wang     | Leetcode      | California
(2 rows)

