def sum_less (list):
   s=sum(list)
   if s<100:
    return True
   else:
    return False

arr=[5,57]
print (sum_less (arr))