def is_plural(txt):
    if txt[-1]=='s':
        return True
    else :
        return False 
t=''
t=input()
print(is_plural(t))