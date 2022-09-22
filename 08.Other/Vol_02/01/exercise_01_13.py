# Описание на клас:
class MyClass:
    # Конструктор:
    def __init__(self,val):
        # Ако аргументът е целочислен:
        if type(val)==int:
            self.number=val
        # Ако аргументът е текстов:
        elif type(val)==str:
            self.name=val
        # Ако аргументът е реално число:
        elif type(val)==float:
            self.value=val
        # Останалите случаи:
        else:
            self.data=val
    # Метод за показване на стойността на полето:
    def show(self):
        # Списък с имената на полетата:
        L=["number","name","value","data"]
        # Обхождане на имената на полетата:
        for s in L:
            # Ако полето съществува:
            if s in dir(self):
                # Показване на името и стойността на полето:
                print(s,"=",self.__dict__[s])
                # Край на оператора за цикъл:
                break
        # Ако полето не е намерено:
        else:
            print("Странен обект")
# Създаване на обекти и проверка на полетата:
A=MyClass(123)
A.show()
del A.number
A.show()
B=MyClass("Обект B")
B.show()
C=MyClass(2.5)
C.show()
D=MyClass([1,2,3])
D.show()
