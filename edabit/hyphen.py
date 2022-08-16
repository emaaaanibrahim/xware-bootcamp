def hyphen(x):
    if x >=1 and x<=60 :
        return x*'-'
    else  :
        return 'not valid number'
x= int (input())
print (hyphen(x))