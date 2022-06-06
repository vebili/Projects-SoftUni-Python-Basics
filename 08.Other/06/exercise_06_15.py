# Функции за използване в декоратори:
def A(h):
    return lambda x: h(x)*h(7-x)
def B(h):
    return lambda x,y: h(x,y)+h(y,x)
def C(h):
    return lambda x: h(x,10-x)
# Функции с декоратори:
@A
def f(x):
    return 2*x-1
@B
def F(x,y):
    return (8-x)*(y+1)
@C
def H(x,y):
    return x*y
# Проверка на резултата:
print("f(3) =",f(3))
print("F(5,7) =",F(5,7))
print("H(6) =",H(6))
