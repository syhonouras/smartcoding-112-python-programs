#65
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")




#66

even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Sum of evens:", even_sum)
print("Sum of odds:", odd_sum)


#67

digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)
print(f"{n} is {'an Armstrong' if total == n else 'not an Armstrong'} number")


#68

digits = str(abs(n))
largest = max(digits)
smallest = min(digits)
print("Largest digit:", largest)
print("Smallest digit:", smallest)


#69

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()


#70

total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
print(f"{n} is {'a perfect' if total == n else 'not a perfect'} number")

#71

if n == 0:
    binary = "0"
else:
    binary = ""
    temp = n
    while temp > 0:
        binary = str(temp % 2) + binary
        temp //= 2
print("Binary:", binary)

#72

binary = input("Enter a binary number: ")
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)
print("Decimal:", decimal)


#73

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


#74
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



#75

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

s = input("Enter a string: ")
print(f"'{s}' is {'a palindrome' if is_palindrome(s) else 'not a palindrome'}")


#76

def count_vowels(s):
    if len(s) == 0:
        return 0
    first = 1 if s[0].lower() in 'aeiou' else 0
    return first + count_vowels(s[1:])

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))


#77


def print_inc_dec(i, n):
    if i > n:
        return
    print(i, end=" ")
    print_inc_dec(i + 1, n)
    print(i, end=" ")

n = int(input("Enter N: "))
print_inc_dec(1, n)
print()