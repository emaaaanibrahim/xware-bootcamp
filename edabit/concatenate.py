l1=[]
l2=[]
l1=input('first list = ')
l2= input('second list = ')
def concat (list1,list2):
    # return  list2 + ', ' + list1
    return "{}, {}".format(list2, list1)
print(str(concat(l1,l2)))