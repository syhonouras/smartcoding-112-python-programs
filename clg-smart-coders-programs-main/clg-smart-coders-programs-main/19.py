a=(int(input("enter digit 1: ")))
b=(int(input("enter digit 2: ")))
c= (int(input("enter digit 3: ")))
if a>b and a>c:
    print("digit 1 is largest")
elif b>a and b>c:
    print("digit 2 is largest")
elif c>a and c>b:
    print("digit 3 is largest")
else:
    print("all are equal")