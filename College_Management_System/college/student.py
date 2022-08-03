def student ():
    list_stu=[]
    try :

        number_of_students=int(input('Please Enter student Number:'))
        for i in range (number_of_students):  
            stu={}
            id = input("enter the id of the student ")
            name = input("enter name of the student ")
            faculty = input ("enter the faculty of the student ")
            age = int (input("enter age of the student "))
            phone = int (input("enter phone of the student "))
            stu['id']=id
            stu['name']=faculty
            stu['department']=faculty
            stu['phone']=phone
            stu['age']=age

            list_stu.append(stu)


    except :
        print('SOMETHING WENT WRONG , TRY AGAIN ')

    

    return  list_stu




 