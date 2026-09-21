#kth bit
n = int(input("enter num: "))
k= int(input("enter k = "))

if (n & (1<<k)) !=0:
    print("set")
else:
    print("not set")