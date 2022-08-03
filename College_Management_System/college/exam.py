# from datetime import date
# from time import time
def exam ():
        ex_list=[]
        try :
            number_of_exams=int(input('Please Enter exams Number:'))
            for i in range (number_of_exams):
                    ex={}
                    id = input("enter the id of the exam ")
                    date = input("enter name of the exam ")
                    time = input ("enter the time of exam ")
                    duration = int (input("enter duration of the exam " ))

                    ex['id']=id
                    ex['date']=date
                    ex['time']=time
                    ex['duration']=duration

                    ex_list.append(ex)


        except Exception as e:
            print(e)
            print('SOMETHING WENT WRONG , TRY AGAIN ')

    


        return ex_list
        
        
        
        