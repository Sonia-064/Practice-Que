n = 10
a, b = 0, 1
print(a, b, end=" ")

for _ in range(2, n):
    next_number = a + b
    print(next_number, end=" ")
    a, b = b, next_number


