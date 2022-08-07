from xml.dom.minidom import Element


list=[1,2,3,4,5]
element = int(input('enter the number u want to check'))
def check (l,elemnt):
    if element in list :
        return True 
    else:
        return False
print(check(list,element))
   
