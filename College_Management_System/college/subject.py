from re import sub


def subject ():
    list_sub= []

    try :
        number_of_subjects =int(input('Please Enter subject Number:'))
        for i in range (number_of_subjects):
            sub={}
            id = input("enter the id of the sybject " )
            name = input("enter name of the sybject")
            department = input ("enter the department of the sybject ")
            code = int (input("enter code of the sybject " ))
            sub['id']=id
            sub['name']=name
            sub['department']=department
            sub['code']=code

            list_sub.append(sub)

    except :
        print('SOMETHING WENT WRONG , TRY AGAIN ')

    


    return list_sub
        
        
        
        