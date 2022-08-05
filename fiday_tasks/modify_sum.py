n= int (input('enter the number :  '))
sum = 0
if n==0:
    exit()
elif n %3 == 0 or n %5==0:    
    for i in range(1,n):
        sum+=i
    print(sum)

else :
    print('enter number can be divided on 3 or 5')


