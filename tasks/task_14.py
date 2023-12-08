# asterisks: int = int(input("Введите целое положительное число: "))
#
# for i in range(asterisks):
#     print(" " * i + "*" * (2 * (asterisks - i) - 1))
# for i in range(asterisks - 2, -1, -1):
#     print(" " * i + "*" * (2 * (asterisks - i) - 1))


# i = 0
# while i < asterisks:
#     print(" " * i + "*" * (2 * (asterisks - i) - 1))
#     i += 1
# i = asterisks - 2
# while i >= 0:
#     print(" " * i + "*" * (2 * (asterisks - i) - 1))
#     i -= 1


# -------------------

n: int = 4

# top
i = 1
while i <= n:

    space = n - i
    j = 1
    while j <= space:
        print(' ', end='')
        j += 1

    stars = 2 * i
    k = 1
    while k < stars:
        print('*', end='')
        k += 1

    print()
    i += 1

# bottom
i = 1
while i <= n:

    space = n - i
    j = 1
    while j <= space:
        print(' ', end='')
        j += 1

    stars = 2 * i
    k = 1
    while k < stars:
        print('*', end='')
        k += 1

    print()
    i += 1
