# Функции генератори:
def names():
    yield "Чичо Фьодор"
    yield "Кучето Шарик"
    yield "Котаракът Матроскин"
def colors():
    L=["Червен","Жълт","Зелен","Син"]
    for clr in L:
        yield clr
def myrange(n):
    for k in range(n):
        yield 2*k+1
# Използване на функции генератори:
print("Те са от Простоквашино:")
for name in names():
    print(name)
print(list(names()))
R=colors()
print("Цветови спектър:")
for r in R:
    print(r,end=" ")
print("\nОще един опит...")
for r in R:
    print(r,end=" ")
print("Няма нищо? Това е нормално.")
print("Нечетни числа:")
print(list(myrange(10)))
print(tuple(myrange(10)))
N=myrange(8)
A=list(N)
print("A =",A)
B=list(N)
print("B =",B)
for num in myrange(8):
    print(num,end=" ")
print()
