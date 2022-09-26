# Базов клас:
class Alpha:
    # Конструктор:
    def __init__(self):
        self.set(100)
        print("Обект на класа Alpha:",self.number)
    # Методи:
    def set(self,n):
        self.number=n
    def show(self):
        print(self.__class__.__name__,self.number)
# Производен клас:
class Bravo(Alpha):
    # Конструктор:
    def __init__(self):
        self.set(200)
        print("Обект на класа Bravo:",self.number)
# Обект на базовия клас:
A=Alpha()
A.set(123)
A.show()
# Обект на производния клас:
B=Bravo()
B.set(321)
B.show()
