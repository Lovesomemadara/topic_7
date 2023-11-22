num: int = int(input("Введите число: "))

ran: int = 0
result: int = 1

if num <= -1:
    print("Факториал определен только для натуральных чисел.")
else:
    while ran != num:
        ran += 1
        result *= ran
    print(f"Факториал числа {num} равен {result}")
