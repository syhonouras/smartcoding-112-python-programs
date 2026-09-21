### Number Patterns
#88. Number triangle (row-wise)
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(str(i) * i)

#89 Sequential number triangle
for i in range(1, n + 1):
    print(" ".join(str(j) for j in range(1, i + 1)))


#90. Floyd's triangle

num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#91. 1-0 alternating triangle

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(1 if j % 2 != 0 else 0, end=" ")
    print()

#92. Pascal's triangle
for i in range(n):
    value = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()

#93  Number pyramid (centered)
for i in range(n):
    value = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()

#94. Inverted number triangle
for i in range(n, 0, -1):
    print(" ".join(str(j) for j in range(1, i + 1)))


#95. Column-wise incrementing
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, end=" ")
    print()

#96. Reverse number triangle

for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print(j, end=" ")
    print()


#97 Binary number triangle
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()
