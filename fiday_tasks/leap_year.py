from calendar import isleap


current_year=2017
number_of_leap_year=20

def is_leap (year):
    if year % 400 ==0 and year %100==0 :
        return True
    elif year %4==0  and year % 100 !=0 :
        return True
    else :
        return False
def next_leap_years (year,num_year):
    n=0
    while n < num_year:
        if is_leap(year):
            n+=1
            print (year)
        year+=1
print (next_leap_years(current_year,number_of_leap_year))
