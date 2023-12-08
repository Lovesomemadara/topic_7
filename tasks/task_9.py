numbers: list = ["105", "42", "98", "120", "84", "80", "110", "119", "130", "99"]

result: str = ''

for i in numbers:
    num = int(i)
    if (num % 5 == 0 or num % 7 == 0) and num > 100:
        result += i + ' '
print(f"Числа, кратные 5 или 7 и больше 100: {result}")

# ----------------

print('Числа, кратные 5 или 7 и больше 100:', end=' ')
for i in numbers:
    num = int(i)
    if (num % 5 == 0 or num % 7 == 0) and num > 100:
        print(i, end=' ')
print()
