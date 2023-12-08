# asterisks: int = int(input("Введите целое положительное число: "))

# space = asterisks - 1
'''count = 1
for i in range(1, asterisks + 1):
    for j in range(1, space + 1):
        print(' ', end=' ')
    space -= 1
    for j in range(1, 2 * i):
        print("*", end=' ')
    print()'''

# ----------------------------

"""
stars = 1
space = asterisks - 1
while asterisks > 0:
    count = 1
    while count <= space:
        print(" ", end=" ")
        count += 1
    count = 1
    while count <= stars:
        print("*", end=" ")
        count += 1
    print()
    space -= 1
    stars += 2
    asterisks -= 1
"""

# -----------------------------

n: int = int(input("Введите целое положительное число: "))

i = 1
while i <= n:

    space = n - i
    j = 1
    while j <= space:
        print(' ', end=' ')
        j += 1

    stars = 2 * i
    k = 1
    while k < stars:
        print("*", end=' ')
        k += 1

    print()
    i += 1
