# Описание на класа:
class MyClass:
    # Конструктор:
    def __init__(self,n="Бял"):
        self.name=n;
        print("Създаден е обект:",self.name)
    # Деструктор:
    def __del__(self):
        print("Изтрит е обект:",self.name)
# Функция:
def create(n):
    obj=MyClass(n)
# Създаване на обекти:
A=MyClass()
B=MyClass("Червен")
C=MyClass("Син")
# Извикване на функция:
create("Жълт")
# На полето се присвоява нова стойност:
C.name="Зелен"
# Изтриване на обектите:
del A
del B
del C
