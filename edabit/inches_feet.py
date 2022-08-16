def inches_feet(x):
    if x<12 :
        return 0
    elif x==12:
        return 1
    else :
        return x//12
x= int (input())
print(inches_feet(x))