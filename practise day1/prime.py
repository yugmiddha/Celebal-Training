A = int(input("Enter a number: "))
B = int(input("Enter another number: "))
count = 0
for i in range(A, B + 1):
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if (i % j) == 0:
                break
        else:
            count += 1
print(count)