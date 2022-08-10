def farm (n1,n2,n3):
    n1=n1*2
    n2=n2*4
    n3=n3*4
    return n1+n2+n3

chikens_legs=int(input('Enter number 1 : '))
cows_legs=int(input('Enter number 2 : '))
pigs_legs=int(input('Enter number 3 : '))

print (farm (chikens_legs,cows_legs,pigs_legs))