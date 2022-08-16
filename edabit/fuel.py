
def calculate_fuel(n):
  fuel = n * 10
  if fuel > 100:
    return fuel
  else:
    return 100
n=int(input('enter the distance : '))
print (calculate_fuel(n))
