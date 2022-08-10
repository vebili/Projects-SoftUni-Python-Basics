# Първи клас:
class Alpha:
    pass
# Втори клас:
class Bravo:
    pass
# На променливата се присвоява име на клас:
MyClass=Alpha
# Създаване на обект:
A=MyClass()
# На променливата се присвоява име на клас:
MyClass=Bravo
# Създаване на обект:
B=MyClass()
# Присвояване на класове:
Alpha=Bravo
# Създаване на обект:
C=Alpha()
# Получаване на референция към обекта за реализация на клас:
MyClass=A.__class__
# Създаване на обект:
D=MyClass()
# Проверка на типа на обектите:
print("Обект A:",type(A).__name__)
print("Обект B:",type(B).__name__)
print("Обект C:",type(C).__name__)
print("Обект D:",type(D).__name__)
# Изменение на имената на класовете:
MyClass.__name__="First"
Bravo.__name__="Second"
# Проверка на типа на обектите:
print("Обект A:",type(A).__name__)
print("Обект B:",type(B).__name__)
print("Обект C:",type(C).__name__)
print("Обект D:",type(D).__name__)
