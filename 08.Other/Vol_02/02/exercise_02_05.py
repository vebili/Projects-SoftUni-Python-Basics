# Първи клас:
class Alpha:
    # Поле на класа:
    code=123
    # Конструктор:
    def __init__(self,num):
        print("Конструктор №1")
        self.number=num
        print("Създаден е обект")
        self.show()
    # Метод:
    def show(self):
        print("Метод №1")
        print("Клас:",self.__class__.__name__)
        print("Код на класа:",self.__class__.code)
        print("Поле number:",self.number)
# Втори клас:
class Bravo(Alpha):
    # Поле на класа:
    code=456
# Трети клас:
class Charlie(Bravo):
    # Конструктор:
    def __init__(self,num,txt):
        print("Конструктор №2")
        self.number=num
        self.name=txt
        print("Нов обект")
        self.show()
    # Предефиниране на метода:
    def show(self):
        print("Метод №2")
        print("Клас:",self.__class__.__name__)
        print("Код на класа:",self.__class__.code)
        print("Поле number:",self.number)
        print("Поле name:",self.name)
# Четвърти клас:
class Delta(Charlie):
    # Поле на класа:
    code=789
# Създаване на обект:
A=Alpha(100)
# Създаване на поле на обекта:
A.code=321
print("След командата A.code=321")
# Извикване на метода:
A.show()
# Създаване на обекти:
B=Bravo(200)
C=Charlie(300,"C")
D=Delta(400,"D")
