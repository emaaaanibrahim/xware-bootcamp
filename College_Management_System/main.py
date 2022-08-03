print ('WELCOME')

from college import *
from college.course import course
from college.exam import exam
from college.faculty import faculty
from college.professor import professor
from college.student import student
from college.subject import subject 


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






