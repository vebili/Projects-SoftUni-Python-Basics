# Клас за изчисление на числата на Фибоначи:
class Fibs:
    # Методът се извиква при индексиране на обекта:
    def __getitem__(self, n):
        a = 1
        b = 1
        for k in range(n - 2):
            a, b = b, a + b
        return b


# Създаване на обект:
F = Fibs()
# Изчисление на числата на Фибоначи:
for k in range(1, 16):
    print(F[k], end=" ")
print()
