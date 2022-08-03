from unicodedata import name


def department():
    list_dep=[]
    try: 
        number_of_department=int(input('Please Enter department Number:'))
        for i in range (number_of_department):  
            dep={}
            dep_name = input("enter department name  ")
            id = input("enter department name  ")
            dep['id']=id
            dep['dep_name']=dep_name

            list_dep.append(dep)

    except :
        print('SOMETHING WENT WRONG , TRY AGAIN ')


    

    return list_dep