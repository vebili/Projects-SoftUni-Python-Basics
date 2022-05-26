# Импортиране на функции за генериране на случайни числа:
from random import *
# Функция за показване съдържанието на списъци, множества,
# текст и речници:
def show(L,symb):
   for s in L:
      print(symb,s,sep="",end="")
   print(symb)
# Изходни данни:
A=[1,2,3,4,5]         # Списък
B={'A','B','C','D'}   # Множество
C="Python"            # Текст
D={"A":1,"B":2,"C":3} # Речник
# Извикване на функцията:
show(A,"|")
show(B,"/")
show(C,"*")
show(D,"#")
# Функция за създаване на списък с числа:
def get_nums(n,state):
    if type(n)!=int:
       return []
    if state:
        L=list(2*(k+1) for k in range(n))
    else:
        L=list(2*k+1 for k in range(n))
    return L
# Извикване на функцията:
print(get_nums(10,True))
print(get_nums(8,False))
print(get_nums(12.5,True))
# Функция за създаване на множество от случайни букви:
def get_symbs(n):
    if n>10 or n<1:
       num=10
    else:
       num=n
    S=set()
    Nmin=ord("A")
    Nmax=ord("Z")
    while len(S)<num:
       S.add(chr(randint(Nmin,Nmax)))
    return S
# Инициализация на генератора на случайни числа:
seed(2019)
# Извикване на функцията:
print(get_symbs(7))
print(get_symbs(-5))
print(get_symbs(15))
