length: int = 0

if (num := int(input("Введите целое число: "))) == 0:
    length = 1
else:
    if num < 0:
        num *= -1
    while num > 0:
        length += 1
        num //= 10

print(f"Количество цифр в числе: {length}")
