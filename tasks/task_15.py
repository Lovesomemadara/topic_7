asterisks: int = int(input("Введите целое положительное число: "))
for i in range(1, asterisks + 1):
    print(" " * (asterisks - i) + "*" * (2 * i - 1))
for i in range(asterisks - 1, 0, -1):
    print(" " * (asterisks - i) + "*" * (2 * i - 1))
'''i = 1
while i <= asterisks:
    print(" " * (asterisks - i) + "*" * (2 * i - 1))
    i += 1
i = asterisks - 1
while i >= 1:
    print(" " * (asterisks - i) + "*" * (2 * i - 1))
    i -= 1'''
