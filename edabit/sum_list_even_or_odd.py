def sum_list_odd_or_even (list):
   x = sum (list)
   if x%2==0 :
    return 'even'
   else :
    return 'odd'
arr=[0,1,5]
print (sum_list_odd_or_even (arr))