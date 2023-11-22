n: int = int(input("Введите число: "))
tabl: int = 0
print(f"Таблица умножения для числа {n} с помощью цикла for:")
for tabl in range(0, 10):
    tabl += 1
    print(f"{n} * {tabl} = {n * tabl}")

print("Таблица умножения для числа 5 с помощью цикла while:")
tabl2: int = 0
while tabl2 != 10:
    tabl2 += 1
    print(f"{n} * {tabl2} = {n * tabl2}")
