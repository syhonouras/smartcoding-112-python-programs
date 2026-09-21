#swap using XOR
a=int(input("enter digit"))
b=int(input("enter digit"))
a=a^b
b=a^b
a=a^b
print(a,b)