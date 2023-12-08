# Вложенные циклы


width = 5  # ширина
height = 3  # высота

for i in range(height):
    for j in range(width):
        print('*', end=' ')
    print()

# -----------------------

height = 5
row = 1
while row <= height:
    space = height - row

    count = 1
    while count <= space:
        print(' ', end=' ')
        count += 1

    k = 0
    while k < row:
        print('*', end=' ')
        k += 1

    print()
    row += 1
