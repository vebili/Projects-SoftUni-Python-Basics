# Описание на клас:
class MyClass:
    # Конструктор:
    def __init__(self):
        self.value = 123
        print("Създава се обект:", self.value)

    # Деструктор:
    def __del__(self):
        print("Изтрива се обект:", self.value)

    # Метод за присвояване на стойност на полето:
    def set(self, n):
        self.value = n

    # Метод за показване на стойността на полето:
    def show(self):
        print("Поле на обекта:", self.value)


# Създаване на обект:
obj = MyClass()
# Извикване на методите от обекта:
obj.show()
obj.set(100)
# Извикване на методите от класа:
MyClass.show(obj)
MyClass.set(obj, 200)
# Проверка на стойността на полето:
obj.show()
# Явно извикване на конструктора:
MyClass.__init__(obj)
# Явно извикване на деструктора:
MyClass.__del__(obj)
# Проверка на стойността на полето:
obj.show()
# Изменение на стойността на полето:
obj.value = 321
obj.show()
# Явно извикване на конструктора чрез обекта:
obj.__init__()
# Явно извикване на деструктора чрез обекта:
obj.__del__()
# Проверка на стойността на полето:
obj.show()
