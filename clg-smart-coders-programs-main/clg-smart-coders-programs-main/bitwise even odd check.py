#Check if a number is even or odd using bitwise AND ( n & 1 )
num = int(input("enter a number: "))
if num&1:
    print("odd")
else:
    print("even")