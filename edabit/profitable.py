def profitable(x,y,z):
    if x*y > z :
        return True
    else :
        return False

n1= float(input())
n2= int(input())
n3= int(input())
print(profitable(n1,n2,n3))