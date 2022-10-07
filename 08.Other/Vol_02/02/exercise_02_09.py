# Клас със специални методи:
class MyClass:
    # Конструктор:
    def __init__(self,val):
        self.value=val
    # Метод за привеждане към текстов тип:
    def __str__(self):
        return "Поле "+str(self.value)
    # Метод за привеждане към логически тип:
    def __bool__(self):
        if type(self.value)==int:
            return True
        else:
           return False
    # Метод за привеждане към целочислен тип:
    def __int__(self):
        if self:
            return self.value
        else:
            return 0
# Създаване на обекти и проверка на методите:
print("Обект A:")
A=MyClass(100)
print(A)
print("Число",int(A))
print("A - 1 =",int(A)-1)
print("Обект B:")
B=MyClass("B")
print(B)
print("Число",int(B))
print("B + 1 =",int(B)+1)
