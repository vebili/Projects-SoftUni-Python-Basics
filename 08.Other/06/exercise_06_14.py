# Функции с рекурсивно извикване.
# Функция за изчисляване на сумата на числа:
def mysum(n):
    if n==0:
        return 0;
    else:
        return n+mysum(n-1)
# Функция за изчисляване на числата на Фибоначи:
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
# Функция за инверсно показване на текст/списък:
def show(txt):
    if len(txt)==0:
        print("|")
    else:
        print("|",txt[-1],end="",sep="")
        show(txt[:-1])
# Извикване на функции:
print("Сума на числата:")
for k in range(12):
    print(mysum(k),end=" ")
print("\nЧисла на Фибоначи:")
for k in range(15):
    print(fib(k+1),end=" ")
print("\nИнверсия на текст:")
show("Hello Python")
print("Инверсия на списък:")
show([1,2,3,4,5])
