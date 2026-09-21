#Divisibility Check : Check whether a number is divisible by 3, 5, both, or neither
n=int(input("enter number to be divided: "))

if n%3==0 and n%5==0:
    print("divisible by 3 and 5 ")
elif n%3==0 :
    print("divisble by 3")
elif n%5==0:
    print("divisible by 5")
else:
    print("not divisible")
