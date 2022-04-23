# Кортеж с числа:
A = tuple(k for k in range(1, 21) if k % 3 != 0)
print(A)
# Списък с числа:
B = [2 ** (k // 2) if k % 2 == 0 else 3 ** (k // 2) for k in range(15)]
print(B)
# Списък с числа:
C = [0 if k == 0 or k == 1 else k ** 2 for k in range(13) if not k in [2, 5, 7]]
print(C)
# Кортеж в обратен порядък:
Alpha = A[::-1]
print(Alpha)
# Елементите се избират „през един“, започвайки от първия:
Bravo = B[::2]
print(Bravo)
# Елементите се избират „през един“, започвайки от втория:
Charlie = B[1::2]
print(Charlie)
