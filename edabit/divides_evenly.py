
def divide_even(x,y):
    z= x/y
    if z%2==0 :
        return True
    else:
        return False
n1=int (input ())
n2= int (input())

print (divide_even(n1,n2))