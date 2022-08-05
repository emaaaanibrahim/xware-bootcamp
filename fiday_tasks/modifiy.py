def  greet ():
    name = input('what is your name ? ' '\n' )

    if name=='Alice' or name=='Bob' :
        return "Hi , " + name
    else:
        return 'enter another name'


print (greet())
# else :
#     print ('TRY ANOTHER NAME')   