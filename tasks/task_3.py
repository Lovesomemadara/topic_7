for i in range(2, 21, 2):
    print(i)

# Option 2
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Option 3
print(*range(2, 21, 2), sep='\n')
