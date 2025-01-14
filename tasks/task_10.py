low: int = int(input("Введите начало диапазона: "))
high: int = int(input("Введите конец диапазона: "))

if low == high or (low < 0 or high < 0):
    print("Некорректный диапазон")
else:
    if low > high:
        low, high = high, low

    for i in range(low, high + 1):
        sum_of_cubes = 0
        n = len(str(i))

        num = i
        while num > 0:
            digit = num % 10
            sum_of_cubes += digit ** n
            num //= 10

        if i == sum_of_cubes:
            print(i, end=' ')
