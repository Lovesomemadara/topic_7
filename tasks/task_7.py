num: float = float(input("Введите число: "))

divider: int = 2

while divider <= num:
    if num % divider == 0:
        print(divider, end=' ')
        num = num / divider
    else:
        divider += 1
