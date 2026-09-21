# Given 3 sides, check if a valid triangle can be formed
a = float(input("enter side A"))
b = float(input("enter side B"))
c = float(input("enter side C"))
if a+b>c and b+c>a and a+c>b:
    print("it is a valid triangle")
else:
    print("not a triangle")