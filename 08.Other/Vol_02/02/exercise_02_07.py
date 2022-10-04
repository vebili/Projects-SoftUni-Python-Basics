# Първи клас:
class Alpha:
    # Конструктор:
    def __init__(self,num):
        self.code=num
        print("Присвоена е стойност на полето code")
    # Метод:
    def show(self):
        print("Поле code:",self.code)
# Втори клас:
class Bravo(Alpha):
    # Конструктор:
    def __init__(self,num,txt):
        # Извикване на конструктора на базовия клас:
        super().__init__(num)
        self.name=txt
        print("Присвоена е стойност на полето name")
    # Метод:
    def show(self):
        # Извикване на метода от базовия клас:
        super().show()
        print("Поле name:",self.name)
# Трети клас:
class Charlie(Bravo):
    # Конструктор:
    def __init__(self,num,txt,val):
        # Извикване на конструктора от базовия клас:
        super().__init__(num,txt)
        self.value=val
        print("Присвоена е стойност на полето value")
    # Метод:
    def show(self):
        # Извикване на метода от базовия клас:
        super().show()
        print("Поле value:",self.value)
# Създаване на обекти и извикване на методи:
print("Обект A")
A=Alpha(100)
A.show()
print("Обект B")
B=Bravo(200,"B")
B.show()
print("Обект C")
C=Charlie(300,"C",[1,2,3])
C.show()
