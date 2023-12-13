begin: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите начало диапазона: "))

if begin > end:
    begin, end = end, begin

for i in range(begin, end + 1):
    if i % 2 == 0:
        print(i)
    elif begin == end:
        print(0)
