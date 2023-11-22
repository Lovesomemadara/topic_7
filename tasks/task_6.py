num: int = abs(int(input("Введите целое число: ")))
length: int = 0

if num == 0:
    print("Количество цифр в числе: 1")
else:
    while num > 0:
        length += 1
        num //= 10
    print(f"Количество цифр в числе: {length}")
