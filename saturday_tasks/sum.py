list=[1,2,3,4,5]
def total (list):
    sum=0
    new_list =[]
    for i in range (0,len(list)):
        sum+=list[i]
        new_list.append(sum)
    return new_list
print(total(list))