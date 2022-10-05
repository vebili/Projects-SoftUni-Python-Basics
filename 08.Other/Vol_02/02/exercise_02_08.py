# Първи клас:
class Alpha:
    # Конструктор:
    def __init__(self,num):
        self.code=num
    # Метод:
    def show(self):
        print("Клас Alpha:",self.code)
# Втори клас:
class Bravo(Alpha):
    # Предефиниране на метода:
    def show(self):
        print("Клас Bravo:",self.code)
        super().show()
# Трети клас:
class Charlie(Alpha):
    # Предефиниране на метода:
    def show(self):
        print("Клас Charlie:",self.code)
        super(Charlie,self).show()
# Четвърти клас:
class Delta(Bravo,Charlie):
    # Предефиниране на метода:
    def show(self):
        print("Клас Delta:",self.code)
        super().show()
        Charlie.show(self)
        super(Bravo,self).show()
# Функция за показване на веригата от наследявания:
def display(MyClass):
    print("Наследяване за "+MyClass.__name__+":")
    k=1
    for s in MyClass.__mro__:
        print("["+str(k)+"]",s.__name__)
        k+=1
# Показване на веригата от наследявания,
# създаване на обекти и извикване на метода:
display(Alpha)
A=Alpha(100)
A.show()
display(Bravo)
B=Bravo(200)
B.show()
display(Charlie)
C=Charlie(300)
C.show()
display(Delta)
D=Delta(400)
D.show()
