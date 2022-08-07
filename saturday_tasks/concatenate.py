list1=[1,2,3,4]
list2=[5,6,7,8]
def concatenate(l1,l2):
    for i in l2 :
        l1.append(i)
    return(l1)
print(concatenate(list1,list2))
