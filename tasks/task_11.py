if (num := int(input("Введите целое положительное число: "))) <= 0:
    print("Число не является положительным!")
else:
    '''for i in range(1, num + 1):
        for j in range(i):
            print(i, end=' ')
        print()'''
    count = 1
    while count <= num:
        inner_count = 1
        while inner_count <= count:
            print(count, end=' ')
            inner_count += 1
        print()
        count += 1
