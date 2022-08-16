def years_in_house(year,moves):
    return round(year/(moves+1))
year=int(input())
moves=int(input())
print(years_in_house(year,moves))