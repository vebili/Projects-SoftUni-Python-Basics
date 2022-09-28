# Първи клас:
class Alpha:
    code=123
    def alpha(self):
        print("Alpha:",self.code)
# Втори клас:
class Bravo(Alpha):
    def bravo(self):
        print("Bravo:",self.code)
# Трети клас:
class Charlie(Bravo):
    def charlie(self):
        print("Charlie:",self.code)
# Функция за показване на йерархията на наследяването:
def show(MyClass):
    print("Класс",MyClass.__name__,end=":\n")
    for s in MyClass.__mro__:
        print("<",s.__name__,">",end="",sep="")
    print()
# Йерархия на наследяването на класовете:
show(Alpha)
show(Bravo)
show(Charlie)
# Създаване на обекти:
A=Alpha()
B=Bravo()
C=Charlie()
# Извикване на методи:
print("Обект A")
A.alpha()
print("Обект B")
B.alpha()
B.bravo()
print("Обект C")
C.alpha()
C.bravo()
C.charlie()
# Присвояване на стойност на полето:
Bravo.code=321
print("Изпълнена е командата Bravo.code=321")
# Извикване на методи:
print("Обект C")
C.alpha()
C.bravo()
C.charlie()
print("Обект A")
A.alpha()
