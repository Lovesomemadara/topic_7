begin: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите начало диапазона: "))


if begin == end and begin % 2 != 0:
    print(0)
elif begin == end and begin % 2 == 0:
    print(begin)
else:
    if begin > end:
        begin, end = end, begin
        for i in range(begin, end + 1, -1):
            if i % 2 == 0:
                print(i)
    for i in range(begin, end + 1):
        if i % 2 == 0:
            print(i)
