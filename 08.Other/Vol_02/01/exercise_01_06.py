# Описание на класа:
class MyClass:
    # Поле на класа:
    color="Червен"
    # Методи на класа:
    def set(txt):
        MyClass.color=txt
    def show():
        print(MyClass.color)
# Извикване на методите на класа:
MyClass.show()
MyClass.set("Зелен")
# Показване стойността на полето на класа:
print(MyClass.color)
# Нова стойност за полето на класа:
MyClass.color="Син"
# Извикване на метода на класа:
MyClass.show()
# Създаване на обекти на класа:
A=MyClass()
B=MyClass()
# Проверка на стойността на полето:
print("Клас:",MyClass.color)
print("Обект A:",A.color)
print("Обект B:",B.color)
# Присвояване на стойност на полето:
A.color="Бял"
# Проверка на стойността на полето:
print("Клас:",MyClass.color)
print("Обект A:",A.color)
print("Обект B:",B.color)
# Присвояване на стойност на полето:
MyClass.color="Жълт"
# Проверка на стойността на полето:
print("Клас:",MyClass.color)
print("Обект A:",A.color)
print("Обект B:",B.color)
# Изтриване на поле от обект A:
del A.color
# Проверка на стойността на полето:
print("Клас:",MyClass.color)
print("Обект A:",A.color)
print("Обект B:",B.color)
