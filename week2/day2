# day2
#### thi is solution for ex:1


create table if not exists faculty (
	id serial primary key ,
  	name varchar(40) NOT NULL default 'hello'
);
create table if not exists student 
	(
	id serial primary key ,
  	name varchar(40) NOT NULL default 'hello',
	age int NOT NULL ,
	address varchar (60) NOT NULL,
	phone varchar (11) NOT NULL,
	image bytea NOT NULL,
	birth_date varchar (30),
	course_id int not null ,
	foreign key (course_id) references course (id),
	address_id int not null ,
	foreign key (address_id) references address (id)	
) ; 
create table if not exists professor (

    id serial primary key ,
	name varchar (50) not null default 'hello' , 
    salary float not null default '0.0',
	age int NOT NULL ,
	image bytea NOT NULL,
	faculty_id int not null ,
	foreign key (faculty_id) references faculty (id),
    department_id int not null ,
	foreign key (department_id) references department (id)
);

create table if not exists department (

    id serial primary key ,
	name varchar (50) not null default 'hello', 
    faculty_id int not null ,
	foreign key (faculty_id) references faculty (id)


);
	
	
create table if not exists address (
	id serial primary key ,
  	city varchar(50) NOT NULL default'city',
	governate varchar(50) NOT NULL default'city',
	line_address1 varchar(50) NOT NULL default 'city',
	line_address2 varchar(50) NOT NULL default'city',
	student_id int not null ,
	foreign key (student_id) references student (id)
);
create table if not exists subject (
	id serial primary key ,
  	name varchar(40) NOT NULL default 'hello',
	code int NOT NULL unique,
	faculty_id int not null ,
	foreign key (faculty_id) references faculty (id)

);	
	
create table if not exists course (
	id serial primary key ,
  	duration int NOT NULL,
	student_id int not null ,
	foreign key (student_id) references student (id),
	subject_id int not null ,
	foreign key (subject_id) references subject (id)
	
);

	
create table if not exists exams (
	id serial primary key ,
	duration int NOT NULL ,
	time int NOT NULL  ,
	date varchar(20) NOT NULL ,
	course_id int references Course (id)


);		
	
create table if not exists student_address (
    id serial primary key , 
	student_id int references student (id),
	address_id int references address (id)

);	

create table if not exists course_enrollment (
    id serial primary key , 
	course_id int references course (id),
	student_id int references student (id)

);	

________________________________________________________________________________________________________________________________________________________
##### this is solution  of ex :2 :

### link : https://pgexercises.com/questions/basic/selectall.html
solution select * from cd.facilities;

### link : https://pgexercises.com/questions/basic/selectspecific.html
solution  select name, membercost from cd.facilities;

### link  : https://pgexercises.com/questions/basic/where.html
solution select facid, name, membercost, guestcost, initialoutlay, monthlymaintenance from cd.facilities where membercost>0;
 
### link : https://pgexercises.com/questions/basic/where4.html
solution select * from cd.facilities where facid in (1,5);  

### link : https://pgexercises.com/questions/basic/date.html
solution : select memid, surname, firstname, joindate from cd.members where joindate > '2012-08-29';

### link : https://pgexercises.com/questions/basic/unique.html
solution :select distinct surname from cd.members order by surname limit 10;


###link : https://pgexercises.com/questions/basic/union.html
solution : select surname from cd.members union select name from cd.facilities;
 
### link : https://pgexercises.com/questions/basic/agg.html 
solution : select max(joindate) as latest from cd.members;
