

st=[1,2,3,4,5,6,7,8,9,10]

def odd (ist):
    # ist=[]
    # for i in range(1,len(ist),2):
    #     ist.append(ist[i])
    #     return ist
    odd_elemnts=ist[0::2]
    return odd_elemnts

print(odd(st))