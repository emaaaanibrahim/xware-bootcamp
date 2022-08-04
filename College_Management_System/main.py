print ('WELCOME')

from college import *
from college.course import course
from college.department import department
from college.exam import exam
from college.faculty import faculty
from college.professor import professor
from college.student import student
from college.subject import subject
from college.update import update 








# print('faculty_info : NAME')
print(faculty())
print()
# print('professor_info : NAME , AGE , SALARY , DEPARTMENT ')
print(professor())
print()
# print('student_info : NAME , AGE ,PHONE , FACULTY ')
print(student())
print()
# print('subject_info : NAME ,DEPARTMENT , CODE ')
print(subject())
print()
# print('courses_info : NAME , PROFESSOR, SUBJECT , STUDENT ,DURATION')
print(course())
print()
# print('exams_info : DATE , TIME , DURATION ')
print(exam())
print()




faculty_list  = faculty()
department_list=department()
subject_list=subject()
exam_list=exam()
course_list=course()
student_list=student()
professor_list=professor()



try :
        number =int(input('Please Enter Number of functions u want to update:'))
        if number==1:
            print(update(faculty_list))
        if number==2:
            print(update(department_list))
        if number==3:
            print(update(subject_list))
        if number==4:
            print(update(course_list))
        if number==5:
            print(update(exam_list))
        if number==6:
            print(update(professor_list))
        if number==7:
            print(update(student_list))  
            
        

                            
except :
        print ('not updated,  not found ')
        




##############

"""


1. show name of faculty
2. show all professor_info
3. show all students_info 
4. show all sybjects _info
5. show all  courses_info
6. show all exams_info
7. update any list 
8. make function take the list needed to update as an input from user
9. assign new items in the list as an input from user 
10.return new list which has been asigned
11. import update.py in main
12. call the function and print it 




"""