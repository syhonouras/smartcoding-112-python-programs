#35 
ch = input("Enter a character: ")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

# 36

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if sp > cp:
    print(f"Profit: {sp - cp:.2f}")
elif cp > sp:
    print(f"Loss: {cp - sp:.2f}")
else:
    print("No profit, no loss")


#37

x = float(input("Enter x: "))
y = float(input("Enter y: "))
if x == 0 and y == 0:
    print("Point is at the origin")
elif x == 0:
    print("Point is on the Y-axis")
elif y == 0:
    print("Point is on the X-axis")
elif x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
else:
    print("Quadrant IV")


#38

n= int(input (" enter a number"))

s=str(n)
total = sum(int(d) ** 3 for d in s)
if total == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")



#39

hours= float(input("Enter hours worked: "))
rate =float(input("Enter hourly rate: "))
if hours>40:
    salary = 40* rate + (hours - 40) * rate * 1.5
else:
    salary =  hours * rate

print (f"salary = {salary:.2f}")

#40

bal= float(input("Enter current balance: "))
amt= float(input("Enter withdrawl amount: "))
min_bal= 500

if amt<= 0:
    print("invalid amount")
elif amt %100 !=0:
    print("must be in multiples of 100")
elif bal - amt < min_bal:
    print("insufficient funds")
else:
    bal -= amt
    print(f"Withdrawal successful. New balance: {bal:.2f}")


#41

hour = int(input("Enter hour (0-12): "))
minute = int(input("Enter minute (0-59): "))

hour = hour % 12
hour_angle = 0.5 * (hour * 60 + minute)
minute_angle = 6 * minute
angle = abs(hour_angle - minute_angle)
angle = min(angle, 360 - angle)
print(f"Angle between hands: {angle:.2f} degrees")


#42

marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

if marks >= 75 and attendance >= 80 and income <= 200000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")