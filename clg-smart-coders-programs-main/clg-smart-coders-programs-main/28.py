#Check if a triangle is equilateral, isosceles, or scalene given 3 sides
a = float(input("enter side A"))
b = float(input("enter side B"))
c = float(input("enter side C"))
if a==b==c:
    print("it is an equilateral triangle")
elif a==b or b==c or a==c:
    print("it is an isoceles triangle")
else:
    print("It is a scalene triangle")