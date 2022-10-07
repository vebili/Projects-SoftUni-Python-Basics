# Клас със специални методи:
class MyClass:
    # Конструктор:
    def __init__(self,num):
        self.code=num
    # Метод за преобразуване в текстов формат:
    def __str__(self):
        return str(self.code)
    # Метод за презареждане на оператора за събиране:
    def __add__(self,n):
        if type(n)==int:
            val=self.code+n
        else:
            val=0
        return MyClass(val)
# Създаване на обект и проверка на методите:
A=MyClass(100)
print("Обект A:",A)
# Към обекта се прибавя число:
B=A+25
print("Обект B:",B)
# Към обекта се прибавя текст:
C=A+"Hello"
print("Обект C:",C)
