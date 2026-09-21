#31	Read month number (1–12) and print number of days in that month	Resource Link

month = int(input("enter number of month"))

days_in_month={1:31, 2:28, 3:31, 4:30 , 5:31 , 6:30, 7:31, 8:31, 9:30,
              10:31 , 11:30, 12:31 }

if month in days_in_month:
    print(f" days: {days_in_month[month]}")
else:
    print("invalid month")