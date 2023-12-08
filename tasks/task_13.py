num: int = int(input("Введите целое положительное число: "))

current_num = 1
'''for i in range(1, num + 1):
    for j in range(i):
        print(current_num, end=" ")
        current_num += 1
    print()'''
i = 1
while i <= num:
    j = 1
    while j <= i:
        print(current_num, end=" ")
        current_num += 1
        j += 1
    print()
    i += 1
