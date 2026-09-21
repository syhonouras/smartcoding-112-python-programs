#10	Check if a character is uppercase, lowercase, digit, or special character
char=input("enter char to check")

if char.isupper():
    print("uppercase")
elif char.islower():
    print("lowercase")
elif char.isdigit():
    print("digit")
else:
    print("special character")