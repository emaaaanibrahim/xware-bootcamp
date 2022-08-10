from ast import Num


def calculate_exponent(num, exp):
	return num ** exp
num=int(input('Enter number 1 : '))
exp=int(input('Enter number 2 : '))
print (calculate_exponent (num,exp))