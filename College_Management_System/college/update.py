from ast import Not
from tokenize import Number


def update (list_update):
        # try :
        #         number =int(input('Please Enter Number of functions u want to update:'))
        #         if number==1:
        #             return 
                     
        # except :
        #         print ('not updated,  not found ')
        
    try:    
        list_update=[]

        # for i in range (len(list_update)):       

        # while True:
        #     list_update.append((input()))
        #     print(list_update)

        count = int(input("Enter the total number of elements that u want to add  : "))
        index = int(input("Enter the index of the list : "))

        for i in range(count):
            user_input_value = input("Enter element {} : ".format(i))
            list_update.insert(index+i, user_input_value)

        print("your updated list is : {}".format(list_update))

    
    
    
    except Exception as e:
        print(e)
    

    
    
    # return list_update  