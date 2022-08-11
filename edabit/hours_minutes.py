def convert (n1,n2):
    n1=n1*60*60
    n2= n2*60
    return n1+n2

num1=int(input('enter number 1 : '))
num2=int(input('enter number 2 : '))

print (convert (num1,num2))