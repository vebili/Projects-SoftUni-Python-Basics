# Брой на числата в последователността:
n = 15
# Първите две числа:
a, b = 1, 1
# Показване на първите две числа:
print(a, b, end=" ")
# При всяка итерация се изчислява по едно ново число:
for k in range(n - 2):
    # Изчисление на ново число в последователността:
    a, b = b, a + b
    # Показване на новото число:
    print(b, end=" ")