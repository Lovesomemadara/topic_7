n: int = int(input("Введите число: "))
print(f"Таблица умножения для числа {n} с помощью цикла for:")

for tabl in range(1, 11):
    print(f"{n} * {tabl} = {n * tabl}")

print(f"Таблица умножения для числа {n} с помощью цикла while:")
tabl_1: int = 0
while tabl_1 <= 10:
    tabl_1 += 1
    print(f"{n} * {tabl_1} = {n * tabl_1}")
