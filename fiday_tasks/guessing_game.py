import random

r = random.randint(1,10)

num = int (input('Guess a number from 1 to 10 : '))

while num > 10 and num < 1:
    print ('Number not in specified range.')
    num = int(input('Guess a number from 1 to 10: '))


def guess ():
    if num > r:
        print ('higher than it')
    elif num < r:
        print ('lower thant it ')
    else:
        print ('BRAVOOOOO')   

