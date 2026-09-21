#60

n = int(input("Enter a number: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
#61

total = 0
for i in range(1, n + 1):
    total += 1 / i
print(f"Sum: {total:.4f}")

#62

total = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        total += i
    else:
        total -= i
print("Sum:", total)


#63

x = float(input("Enter base x: "))
n = int(input("Enter exponent n: "))
result = 1
for _ in range(abs(n)):
    result *= x
if n < 0:
    result = 1 / result
print(f"{x}^{n} = {result}")

#64

total = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += factorial
print("Sum of factorials:", total)


