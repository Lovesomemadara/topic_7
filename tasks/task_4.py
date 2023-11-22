n: int = int(input("Введите число: "))
i: int = 0
result: int = 0

if n <= 0:
    print("Число должно быть больше или равно 1")
elif n == 1:
    print(1)
else:
    while i != n:
        i += abs(1)
        result += i
    print(f"Сумма всех чисел от 1 до {n} равна: {result}")
