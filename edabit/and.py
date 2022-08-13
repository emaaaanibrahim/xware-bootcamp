def And(a,b):
	if a == True:
		if b == True:
			return True
		else:
			return False
	else:
		return False

print (And(False,False))