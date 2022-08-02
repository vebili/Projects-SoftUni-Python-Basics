# Описание на клас:
class MyClass:
    def set(self,n):
        self.number=n
    def show(self):
        print("Поле number =",self.number)
# Създаване на обект:
obj=MyClass()
# Проверка за наличие на полето:
print("Наличие на полето number:",hasattr(obj,"number"))
try:
    # Проверка на стойността на полето:
    obj.show()
except AttributeError:
    print("В обекта няма поле number!")
# Присвояване на стойност на полето:
obj.number=123
# Проверка за наличие на полето:
print("Наличие на полето number:",hasattr(obj,"number"))
# Проверка на стойността на полето:
obj.show()
# Нова стойност на полето:
obj.set(321)
# Проверка на стойността на полето:
obj.show()
