asterisks: int = int(input("Введите целое положительное число: "))
'''for i in range(asterisks):
    print(" " * i + "*" * (2 * (asterisks - i) - 1))
for i in range(asterisks - 2, -1, -1):
    print(" " * i + "*" * (2 * (asterisks - i) - 1))'''
i = 0
while i < asterisks:
    print(" " * i + "*" * (2 * (asterisks - i) - 1))
    i += 1
i = asterisks - 2
while i >= 0:
    print(" " * i + "*" * (2 * (asterisks - i) - 1))
    i -= 1
