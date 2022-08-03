def course ():
    list_co=[]

    try :

        number_of_professorss=int(input('Please Enter student Number:'))
        for i in range (number_of_professorss):
            co={}
            id = input("enter the id of the course " )
            name = input("enter name of the course ")
            professor = input ("enter the course's professor ")
            subject = input ("enter the subject of this course ")
            student = input ("enter the students of this corse ")
            duration = int (input("enter duration of the course " ))
            co['id']=id
            co['name']=name
            co['professor']=professor
            co['subject']=subject
            co['student']=student
            co['duration']=duration

            list_co.append(co)

    except :
        print('SOMETHING WENT WRONG , TRY AGAIN ')

    



    return  list_co       
        
        
    
        
       