#Ticket Pricing : Calculate ticket price based on the customer's age.
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child ticket 400")
elif age <= 19:
    print("Teenager ticket 800")
elif age <= 64:
    print("Adult ticket 1200")
else:
    print("Senior ticket 2000")