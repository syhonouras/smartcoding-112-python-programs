#Nested if & switch-case	30	Build a simple calculator (+, −, ×, ÷) using switch-case	Resource Link

a = float(input("enter first number"))
b = float(input("enter second numbeer"))
op= input("enter operator(+,-,*,/): ")

match op:
    case'+':
        print(a+b)
    case'-':
      print(a-b)
    case'*':
            print(a*b)
    case'/':
        print(a/b)
    