if (num := int(input("Введите целое положительное число: "))) <= 0:
    print("Число не является положительным!")
else:
    for i in range(1, num + 1):
        for j in range(i):
            print(i, end=' ')
        print()
