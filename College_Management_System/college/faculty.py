def faculty():
    list_fac=[]
    try:  
        number_of_faclties =int(input('Please Enter faculty Number:'))
        for i in range (number_of_faclties):
            fac={}
            faculty_name = input("enter faculty name  ")
            id = input("enter id of faculty  ")
            fac['id']=id
            fac['faculty_name']=faculty_name
            list_fac.append(fac)
    except :
        print('SOMETHING WENT WRONG , TRY AGAIN ')

    return list_fac

    



