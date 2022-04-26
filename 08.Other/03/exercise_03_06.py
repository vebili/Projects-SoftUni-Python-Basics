# Импортиране на функция за генериране на случайни числа:
from random import *


# Функция за показване на вложен списък:
def show(A):
    for a in A:
        for s in a:
            print(s, end=" ")
        print()


# Функция за създаване на вложен списък от случайни числа:
def rands(m, n):
    res = [[randint(0, 9) for i in range(n)] for j in range(m)]
    return res


# Функция за създаване на вложен списък от букви:
def symbs(m, n):
    val = 'A'
    res = [['' for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j] = val
            val = chr(ord(val) + 1)
    return res


# Създаване на вложен списък:
A = [[(j + 1) * 10 + i + 1 for i in range(5)] for j in range(3)]
print("Списък A:")
# Показване на вложен списък:
show(A)
# Инициализация на генератор на случайни числа:
seed(2019)
# Списък със случайни числа:
B = rands(3, 4)
print("Списък B:")
# Показване на вложен списък:
show(B)
# Списък с букви:
C = symbs(3, 5)
print("Списък C:")
# Показване на вложен списък:
show(C)
# Списък, определящ броя на редовете във вложен списък:
size = [3, 5, 4, 6]
# Създаване на вложен списък:
D = [['*' for k in range(s)] for s in size]
print("Списък D:")
# Показване на вложен списък:
show(D)
