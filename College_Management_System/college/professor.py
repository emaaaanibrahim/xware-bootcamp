def professor ():
    
    list_pro=[]
    try :

        number_of_professorss=int(input('Please Enter student Number:'))
        for i in range (number_of_professorss):  
                pro={}
                id = input("enter the id of the Professor " )
                name = input("enter name of the Professor ")
                department = input ("enter the department of the Professor" )
                salary = input ("enter salary of the Professor ")
                age = int (input("enter age of the Professor " ))
                pro['id']=id
                pro['name']=name
                pro['department']=department
                pro['salary']=salary
                pro['age']=age



                list_pro.append(pro)


    except :
        print('SOMETHING WENT WRONG , TRY AGAIN ')


    




    return list_pro