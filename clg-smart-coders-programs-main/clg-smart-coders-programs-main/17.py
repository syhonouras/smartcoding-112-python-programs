def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(leap(2026))
print(leap(2014))