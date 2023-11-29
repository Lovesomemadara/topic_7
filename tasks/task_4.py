if (n := int(input("Введите число: "))) <= 0:
    print("Число должно быть больше или равно 1")
elif n == 1:
    print(1)
else:
    i: int = 1
    result: int = 0
    while i <= n:
        result += i
        i += 1
    print(f"Сумма всех чисел от 1 до {n} равна: {result}")
