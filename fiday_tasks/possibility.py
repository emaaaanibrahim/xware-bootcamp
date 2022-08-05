n=int(input('enter the number : '))

choice= int (input ('enter 1 if u want to sum choice , enter 2 if u want product choice '))

def sum (n):
    sum = 0
    if n==0:
        exit()

    for i in range(1,n+1):
        sum+=i
    return sum


def product (n) :
    product= 1 
    for i in range(1,n+1):
        product*=i
    return product

if choice == 1 :
    print(sum(n))
if choice == 2 :
    print (product(n))