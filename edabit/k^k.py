def power (n,k):
    if k**k==n:
        return True
    else:
        return False

x=int (input())
y=int(input())
print(power(x,y))
