
```
import code


print ('WELCOME')
faculty_info =input ('Please Enter Faculty Name:')


number_of_department = int(input("How Many Department in The Faculty: "))
dep_info = []
for i in range (number_of_department):
    dep_name = input("enter department name  " + str(i + 1) + " : ")
    dep_info.append(dep_name)


number_of_professor=int(input('Please Enter Professor Number:'))
pro_info =[]

for i in range (number_of_professor):
        id = input("enter the id of the Professor " + str (i+1) + " : ")
        name = input("enter name of the Professor "+ str (i+1) + " : ")
        department = input ("enter the department of the Professor "+ str (i+1) + " : ")
        salary = input ("enter salary of the Professor "+ str (i+1) + " : ")
        age = int (input("enter age of the Professor " + str (i+1) + " : "))
        pro_info.append([name,age,salary,department])

        
number_of_students=int(input('Please Enter students Number:'))
stu_info =[]
for i in range (number_of_students):
        id = input("enter the id of the student " + str (i+1) + " : ")
        name = input("enter name of the student "+ str (i+1) + " : ")
        faculty = input ("enter the faculty of the student "+ str (i+1) + " : ")
        age = int (input("enter age of the student " + str (i+1) + " : "))
        phone = int (input("enter phone of the student " + str (i+1) + " : "))
        stu_info.append([name,age,faculty,phone])

        


number_of_sybjects=int(input('Please Enter subjects Number:'))
sub_info =[]
for i in range (number_of_sybjects):
        id = input("enter the id of the sybject " + str (i+1) + " : ")
        name = input("enter name of the sybject"+ str (i+1) + " : ")
        department = input ("enter the department of the sybject "+ str (i+1) + " : ")
        code = int (input("enter code of the sybject " + str (i+1) + " : "))
        sub_info.append([name,code,department])

       


number_of_courses=int(input('Please Enter courses Number:'))
cors_info =[]
for i in range (number_of_courses):
        id = input("enter the id of the course " + str (i+1) + " : ")
        name = input("enter name of the course "+ str (i+1) + " : ")
        professor = input ("enter the course's professor "+ str (i+1) + " : ")
        subject = input ("enter the subject of this course "+ str (i+1) + " : ")
        student = input ("enter the students of this corse "+ str (i+1) + " : ")
        duration = int (input("enter duration of the course " + str (i+1) + " : "))
        cors_info.append([name,professor,subject,student,duration])



        

number_of_exams=int(input('Please Enter courses Number:'))
ex_info =[]
for i in range (number_of_exams):
        id = input("enter the id of the exam " + str (i+1) + " : ")
        date = input("enter name of the exam "+ str (i+1) + " : ")
        time = input ("enter the time of exam "+ str (i+1) + " : ")
        duration = int (input("enter duration of the exam " + str (i+1) + " : "))
        ex_info.append([date,time,duration])




print('professor_info : NAME , AGE , SALARY , DEPARTMENT ')
print(pro_info)
print('student_info : NAME , AGE ,PHONE , FACULTY ')
print(stu_info)
print('subject_info : NAME ,DEPARTMENT , CODE ')
print(sub_info)
print('courses_info : NAME , PROFESSOR, SUBJECT , STUDENT ,DURATION')
print(cors_info)
print('exams_info : DATE , TIME , DURATION ')
print(ex_info)


```
