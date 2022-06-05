# Аргумент на функция - функция (и две числа):
def display(f,a,b):
    for k in range(a,b+1):
        print("{0:4}".format(f(k)),end=" ")
    print()
# Резултат от функция - функция:
def mypow(n):
    return lambda x: x**n
# Аргументи на функцията - функции. Резултат - функция:
def apply(f,h):
    def calc(x):
        return f(h(x))
    return calc
# Определяне на функции:
A=mypow(2)
B=mypow(3)
C=apply(lambda x: 2*x+1,lambda x: 2*x)
# Проверка на резултата:
print("x   ",end="")
display(lambda x: x,1,5)
print("A(x)",end="")
display(A,1,5)
print("B(x)",end="")
display(B,1,5)
print("C(x)",end="")
display(C,1,5)
# Определение на функции:
F=lambda f: lambda x: f(f(x))
# Проверка на резултата:
print("F(x->x*x)(5): ",F(lambda x: x*x)(5))
print("F(x->2*x+1)(5):",F(lambda x: 2*x+1)(5))
