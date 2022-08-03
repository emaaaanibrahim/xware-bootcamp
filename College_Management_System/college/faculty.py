def faculty():
    fac={}
    try:   
        faculty_name = input("enter faculty name  ")
        id = input("enter id of faculty  ")
        fac['id']=id
        fac['faculty_name']=faculty_name

    except :
        print('SOMETHING WENT WRONG , TRY AGAIN ')


    list_fac=[fac]

    return fac ,list_fac

    



