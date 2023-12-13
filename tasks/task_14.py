n: int = int(input("Введите целое положительное число: "))

# top
for i in range(n, 0, -1):
    space = n - i
    stars = 2 * i

    for j in range(space):
        print(' ', end='')

    for k in range(stars - 1):
        print('*', end='')

    print()

# bottom
for i in range(2, n + 1):
    space = n - i
    stars = 2 * i - 1

    for j in range(space):
        print(' ', end='')

    for k in range(stars):
        print('*', end='')

    print()

# ----------------------------------

'''
# top
i = n
while i > 1:

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
    i -= 1

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
'''
