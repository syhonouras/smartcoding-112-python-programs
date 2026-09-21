# Smart Coders - 112 Practice Problems: Python Solutions

## Section 1: Operators

### Arithmetic Operators

**1. Read two numbers and print their sum, difference, product, quotient, and remainder**
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Remainder:", a % b)
```

**2. Calculate the area of a circle given radius (A = πr²)**
```python
import math
r = float(input("Enter radius: "))
area = math.pi * r ** 2
print(f"Area: {area:.2f}")
```

**3. Calculate simple interest given P, R, T → (P × R × T) / 100**
```python
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print(f"Simple Interest: {si:.2f}")
```

**4. Convert temperature from Celsius to Fahrenheit and vice versa**
```python
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print(f"{c}°C = {f}°F")

f2 = float(input("Enter temperature in Fahrenheit: "))
c2 = (f2 - 32) * 5/9
print(f"{f2}°F = {c2:.2f}°C")
```

**5. Divisibility Check: Check whether a number is divisible by 3, 5, both, or neither**
```python
n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
elif n % 3 == 0:
    print("Divisible by 3 only")
elif n % 5 == 0:
    print("Divisible by 5 only")
else:
    print("Not divisible by 3 or 5")
```

### Relational & Logical Operators

**6. Read two numbers and print which is greater (use relational operators)**
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are equal")
```

**7. Check if a number is positive, negative, or zero**
```python
n = float(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```

**8. Read three numbers and check if all three are equal**
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a == b and b == c:
    print("All three are equal")
else:
    print("Not all equal")
```

**9. Read age and check eligibility to vote (age ≥ 18)**
```python
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

**10. Check if a character is uppercase, lowercase, digit, or special character**
```python
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
```

### Bitwise Operators

**11. Check if a number is even or odd using bitwise AND (n & 1)**
```python
n = int(input("Enter a number: "))
if n & 1 == 0:
    print("Even")
else:
    print("Odd")
```

**12. Swap two numbers using XOR**
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swap: a={a}, b={b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swap: a={a}, b={b}")
```

**13. Find the value of n << 1 and n >> 1 — relate to multiply/divide by 2**
```python
n = int(input("Enter a number: "))
print(f"{n} << 1 = {n << 1}  (equivalent to {n} * 2)")
print(f"{n} >> 1 = {n >> 1}  (equivalent to {n} // 2)")
```

**14. Check if the Kth bit of a number is set or not**
```python
n = int(input("Enter a number: "))
k = int(input("Enter bit position (0-indexed): "))
if n & (1 << k):
    print(f"Bit {k} is SET")
else:
    print(f"Bit {k} is NOT set")
```

**15. Count the number of set bits in a number**
```python
n = int(input("Enter a number: "))
count = 0
temp = n
while temp:
    count += temp & 1
    temp >>= 1
print(f"Number of set bits in {n}: {count}")
# Alternative one-liner: bin(n).count('1')
```

## Section 2: Conditional Statements

### if / if-else

**16. Check if a number is even or odd**
```python
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**17. Check if a year is a leap year**
```python
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```

**18. Find the largest of two numbers**
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Largest:", a if a > b else b)
```

**19. Find the largest of three numbers**
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest:", largest)
```

**20. Check if a character is a vowel or consonant**
```python
ch = input("Enter a character: ").lower()
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")
```

**21. Ticket Pricing: Calculate ticket price based on the customer's age**
```python
age = int(input("Enter age: "))
if age < 5:
    price = 0
elif age < 12:
    price = 50
elif age < 60:
    price = 100
else:
    price = 60
print("Ticket price:", price)
```

**22. Age Category: Classify a person as a child, teenager, adult, or senior based on age**
```python
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

**23. Time Greeting: Given an hour, print Morning, Afternoon, Evening, or Night**
```python
hour = int(input("Enter hour (0-23): "))
if 5 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 21:
    print("Good Evening")
else:
    print("Good Night")
```

**24. Login Validator: Check whether a username and password combination is valid**
```python
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Invalid username or password")
```

### if-else if-else (Ladder)

**25. Given marks (0-100), print grade: A (>=90), B (>=80), C (>=70), D (>=60), F (<60)**
```python
marks = float(input("Enter marks: "))
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Grade:", grade)
```

**26. Read a number (1-7) and print the corresponding day of the week**
```python
day = int(input("Enter day number (1-7): "))
days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
        5: "Friday", 6: "Saturday", 7: "Sunday"}
print(days.get(day, "Invalid day number"))
```

**27. Calculate electricity bill based on slab rates**
```python
units = float(input("Enter units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 300:
    bill = 100 * 1.5 + (units - 100) * 3
else:
    bill = 100 * 1.5 + 200 * 3 + (units - 300) * 5
print(f"Electricity bill: {bill:.2f}")
```

**28. Check if a triangle is equilateral, isosceles, or scalene given 3 sides**
```python
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
```

**29. Given 3 sides, check if a valid triangle can be formed**
```python
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a + b > c and b + c > a and a + c > b:
    print("Valid triangle")
else:
    print("Not a valid triangle")
```

### Nested if & switch-case

**30. Build a simple calculator (+, -, x, /) using switch-case (match-case in Python)**
```python
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

match op:
    case '+':
        print("Result:", a + b)
    case '-':
        print("Result:", a - b)
    case '*':
        print("Result:", a * b)
    case '/':
        print("Result:", a / b if b != 0 else "Error: division by zero")
    case _:
        print("Invalid operator")
```

**31. Read month number (1-12) and print number of days in that month**
```python
month = int(input("Enter month number (1-12): "))
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                  7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
if month in days_in_month:
    print(f"Days: {days_in_month[month]}")
else:
    print("Invalid month")
```

**32. Check if a number is positive, negative, or zero -- then if positive check even/odd**
```python
n = int(input("Enter a number: "))
if n > 0:
    if n % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```

**33. Given 3 numbers, print them in ascending order using only if-else**
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <= b and a <= c:
    first = a
    second, third = (b, c) if b <= c else (c, b)
elif b <= a and b <= c:
    first = b
    second, third = (a, c) if a <= c else (c, a)
else:
    first = c
    second, third = (a, b) if a <= b else (b, a)

print(f"Ascending order: {first}, {second}, {third}")
```

**34. Find the roots of a quadratic equation (check discriminant: real, equal, imaginary)**
```python
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two real roots: {root1:.2f}, {root2:.2f}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One repeated real root: {root:.2f}")
else:
    real = -b / (2*a)
    imag = math.sqrt(-discriminant) / (2*a)
    print(f"Complex roots: {real:.2f} + {imag:.2f}i, {real:.2f} - {imag:.2f}i")
```

### Mixed / Applied

**35. Check if a given character is an alphabet, digit, or special character**
```python
ch = input("Enter a character: ")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
```

**36. Read the cost price and selling price -- print profit, loss, or no profit no loss**
```python
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if sp > cp:
    print(f"Profit: {sp - cp:.2f}")
elif cp > sp:
    print(f"Loss: {cp - sp:.2f}")
else:
    print("No profit, no loss")
```

**37. Given coordinates (x, y), determine which quadrant the point lies in**
```python
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
```

**38. Check if a 3-digit number is an Armstrong number (e.g., 153)**
```python
n = int(input("Enter a 3-digit number: "))
s = str(n)
total = sum(int(d) ** 3 for d in s)
if total == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
```

**39. Given hours worked and rate, compute salary with overtime (>40 hrs at 1.5x rate)**
```python
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
if hours > 40:
    salary = 40 * rate + (hours - 40) * rate * 1.5
else:
    salary = hours * rate
print(f"Salary: {salary:.2f}")
```

**40. ATM Withdrawal: Approve or reject based on amount, balance, and minimum-balance rules**
```python
balance = float(input("Enter current balance: "))
amount = float(input("Enter withdrawal amount: "))
MIN_BALANCE = 500

if amount <= 0:
    print("Invalid amount")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100")
elif balance - amount < MIN_BALANCE:
    print("Transaction declined: insufficient balance (minimum balance rule)")
else:
    balance -= amount
    print(f"Withdrawal successful. New balance: {balance:.2f}")
```

**41. Clock Angle: Given hour and minute, calculate the smaller angle between the two hands**
```python
hour = int(input("Enter hour (0-12): "))
minute = int(input("Enter minute (0-59): "))

hour = hour % 12
hour_angle = 0.5 * (hour * 60 + minute)
minute_angle = 6 * minute
angle = abs(hour_angle - minute_angle)
angle = min(angle, 360 - angle)
print(f"Angle between hands: {angle:.2f} degrees")
```

**42. Scholarship Eligibility: Determine eligibility based on marks, attendance, and family income**
```python
marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

if marks >= 75 and attendance >= 80 and income <= 200000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
```

## Section 3: Loops

### Basic Counting & Iteration

**43. Print numbers from 1 to N**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(i)
```

**44. Print numbers from N to 1**
```python
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(i)
```

**45. Print all even numbers from 1 to N**
```python
n = int(input("Enter N: "))
for i in range(2, n + 1, 2):
    print(i)
```

**46. Print all odd numbers from 1 to N**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1, 2):
    print(i)
```

**47. Calculate the sum of first N natural numbers**
```python
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)
# Alternative: print(n * (n + 1) // 2)
```

### Digit-Based Problems

**48. Count the number of digits in a number**
```python
n = int(input("Enter a number: "))
count = 0
temp = abs(n)
if temp == 0:
    count = 1
while temp > 0:
    count += 1
    temp //= 10
print("Number of digits:", count)
```

**49. Find the sum of digits of a number**
```python
n = int(input("Enter a number: "))
temp = abs(n)
total = 0
while temp > 0:
    total += temp % 10
    temp //= 10
print("Sum of digits:", total)
```

**50. Reverse a number**
```python
n = int(input("Enter a number: "))
temp = abs(n)
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if n < 0:
    reversed_num = -reversed_num
print("Reversed number:", reversed_num)
```

**51. Check if a number is a palindrome**
```python
n = int(input("Enter a number: "))
temp = n
reversed_num = 0
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10
if n == reversed_num:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
```

**52. Happy Number: Repeatedly replace with sum of squares of digits; check if it reaches 1**
```python
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

n = int(input("Enter a number: "))
print(f"{n} is {'a happy' if is_happy(n) else 'not a happy'} number")
```

**53. Product of Digits: Find the product of all digits of a number using recursion**
```python
def product_of_digits(n):
    if n < 10:
        return n
    return (n % 10) * product_of_digits(n // 10)

n = int(input("Enter a number: "))
print("Product of digits:", product_of_digits(abs(n)))
```

**54. Extract and print each digit of a number from left to right**
```python
n = int(input("Enter a number: "))
digits = str(abs(n))
for d in digits:
    print(d)
```

### Math / Number Theory

**55. Find factorial of N**
```python
n = int(input("Enter N: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
```

**56. Check if a number is prime**
```python
n = int(input("Enter a number: "))
is_prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print(f"{n} is {'prime' if is_prime else 'not prime'}")
```

**57. Print all prime numbers from 1 to N**
```python
n = int(input("Enter N: "))
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
```

**58. Find GCD / HCF of two numbers**
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = a, b
while y:
    x, y = y, x % y
print("GCD:", x)
```

**59. Find LCM of two numbers**
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

lcm = (a * b) // gcd(a, b)
print("LCM:", lcm)
```

### Series & Patterns (Single Loop)

**60. Print Fibonacci series up to N terms**
```python
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
```

**61. Compute the sum: 1 + 1/2 + 1/3 + ... + 1/N**
```python
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += 1 / i
print(f"Sum: {total:.4f}")
```

**62. Compute: 1 - 2 + 3 - 4 + 5 - ... up to N terms**
```python
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        total += i
    else:
        total -= i
print("Sum:", total)
```

**63. Find x^n (power) without using built-in pow function**
```python
x = float(input("Enter base x: "))
n = int(input("Enter exponent n: "))
result = 1
for _ in range(abs(n)):
    result *= x
if n < 0:
    result = 1 / result
print(f"{x}^{n} = {result}")
```

**64. Compute: 1! + 2! + 3! + ... + N!**
```python
n = int(input("Enter N: "))
total = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += factorial
print("Sum of factorials:", total)
```

### Applied / Mixed Loop Problems

**65. Print the multiplication table of a given number**
```python
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

**66. Find the sum of even and odd numbers separately from 1 to N**
```python
n = int(input("Enter N: "))
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Sum of evens:", even_sum)
print("Sum of odds:", odd_sum)
```

**67. Check if a number is an Armstrong number (generalized for any digits)**
```python
n = int(input("Enter a number: "))
digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)
print(f"{n} is {'an Armstrong' if total == n else 'not an Armstrong'} number")
```

**68. Find the largest and smallest digit in a number**
```python
n = int(input("Enter a number: "))
digits = str(abs(n))
largest = max(digits)
smallest = min(digits)
print("Largest digit:", largest)
print("Smallest digit:", smallest)
```

**69. Print all factors / divisors of a number**
```python
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()
```

**70. Check if a number is a perfect number (sum of divisors == number)**
```python
n = int(input("Enter a number: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
print(f"{n} is {'a perfect' if total == n else 'not a perfect'} number")
```

**71. Convert decimal to binary**
```python
n = int(input("Enter a decimal number: "))
if n == 0:
    binary = "0"
else:
    binary = ""
    temp = n
    while temp > 0:
        binary = str(temp % 2) + binary
        temp //= 2
print("Binary:", binary)
```

**72. Convert binary to decimal**
```python
binary = input("Enter a binary number: ")
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)
print("Decimal:", decimal)
```

**73. Read numbers until user enters -1, print the count and average**
```python
count = 0
total = 0
while True:
    n = float(input("Enter a number (-1 to stop): "))
    if n == -1:
        break
    count += 1
    total += n

if count > 0:
    print("Count:", count)
    print(f"Average: {total / count:.2f}")
else:
    print("No numbers entered")
```

**74. Find the sum of a series: x - x^3/3! + x^5/5! - x^7/7! ... (sin series)**
```python
x = float(input("Enter x (in radians): "))
n_terms = int(input("Enter number of terms: "))

result = 0
sign = 1
for i in range(n_terms):
    power = 2 * i + 1
    factorial = 1
    for j in range(1, power + 1):
        factorial *= j
    term = (x ** power) / factorial
    result += sign * term
    sign *= -1

print(f"sin({x}) approx = {result:.6f}")
```

**75. Palindrome Check: Check whether a string is a palindrome using recursion**
```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

s = input("Enter a string: ")
print(f"'{s}' is {'a palindrome' if is_palindrome(s) else 'not a palindrome'}")
```

**76. Count Vowels: Count the number of vowels in a string using recursion**
```python
def count_vowels(s):
    if len(s) == 0:
        return 0
    first = 1 if s[0].lower() in 'aeiou' else 0
    return first + count_vowels(s[1:])

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
```

**77. Increasing + Decreasing: Using a single recursive function, print increasing then decreasing**
```python
def print_inc_dec(i, n):
    if i > n:
        return
    print(i, end=" ")
    print_inc_dec(i + 1, n)
    print(i, end=" ")

n = int(input("Enter N: "))
print_inc_dec(1, n)
print()
```

## Section 4: Nested Loops / Inner For Loops - Patterns

### Star Patterns

**78. Right-angled triangle (stars)**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print("*" * i)
```

**79. Inverted right-angled triangle**
```python
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print("*" * i)
```

**80. Right-aligned triangle**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
```

**81. Inverted right-aligned triangle**
```python
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)
```

**82. Pyramid (centered)**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

**83. Inverted pyramid**
```python
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

**84. Diamond shape**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

**85. Hollow rectangle**
```python
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if i == 1 or i == rows or j == 1 or j == cols:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**86. Hollow right-angled triangle**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**87. Sandglass / Hourglass**
```python
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

### Number Patterns

**88. Number triangle (row-wise)**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(str(i) * i)
```

**89. Sequential number triangle**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" ".join(str(j) for j in range(1, i + 1)))
```

**90. Floyd's triangle**
```python
n = int(input("Enter number of rows: "))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

**91. 1-0 alternating triangle**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(1 if j % 2 != 0 else 0, end=" ")
    print()
```

**92. Pascal's triangle**
```python
n = int(input("Enter number of rows: "))
for i in range(n):
    value = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()
```

**93. Number pyramid (centered)**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

**94. Inverted number triangle**
```python
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(" ".join(str(j) for j in range(1, i + 1)))
```

**95. Column-wise incrementing**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, end=" ")
    print()
```

**96. Reverse number triangle**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print(j, end=" ")
    print()
```

**97. Binary number triangle**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()
```

### Alphabet Patterns

**98. Alphabet triangle (row repeat)**
```python
n = int(input("Enter N: "))
for i in range(n):
    print(chr(65 + i) * (i + 1))
```

**99. Alphabet triangle (sequential)**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
```

**100. Reverse alphabet triangle**
```python
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
```

**101. Right-aligned alphabet triangle**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
```

**102. Alphabet pyramid (centered)**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()
```

### Advanced Patterns (Nested Logic)

**103. Butterfly pattern**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
```

**104. Hollow diamond inside rectangle**
```python
n = int(input("Enter N (even number recommended): "))
size = 2 * n
for i in range(size):
    for j in range(size):
        dist = abs(i - n) + abs(j - n)
        if dist == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**105. Number diamond**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
```

**106. Zigzag pattern**
```python
rows = 3
n = int(input("Enter N (length): "))
matrix = [[0] * n for _ in range(rows)]
row = 0
going_down = True
for col in range(n):
    matrix[row][col] = 1
    if going_down:
        row += 1
        if row == rows:
            row = rows - 2
            going_down = False
    else:
        row -= 1
        if row < 0:
            row = 1
            going_down = True

for r in matrix:
    print(" ".join("*" if v else " " for v in r))
```

**107. Spiral number matrix (4x4)**
```python
n = 4
matrix = [[0] * n for _ in range(n)]
top, bottom, left, right = 0, n - 1, 0, n - 1
num = 1
while top <= bottom and left <= right:
    for j in range(left, right + 1):
        matrix[top][j] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for j in range(right, left - 1, -1):
        matrix[bottom][j] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(" ".join(f"{v:2}" for v in row))
```

**108. Right arrow pattern**
```python
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * i)
```

**109. X pattern**
```python
n = int(input("Enter N: "))
for i in range(n):
    for j in range(n):
        if j == i or j == (n - 1 - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**110. Plus (+) pattern**
```python
n = int(input("Enter N (odd number): "))
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

**111. Heart shape pattern**
```python
# Uses the heart curve formula: (x^2 + y^2 - 1)^3 - x^2*y^3 <= 0
for y in range(15, -15, -1):
    yy = y / 10
    row = ""
    for x in range(-15, 16):
        xx = x / 10
        val = (xx**2 + yy**2 - 1)**3 - (xx**2) * (yy**3)
        row += "*" if val <= 0 else " "
    print(row)
```

**112. Square with diagonals marked**
```python
n = int(input("Enter N: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```
