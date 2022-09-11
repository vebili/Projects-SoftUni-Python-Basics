# Функция, която получава референция към клас
# и връща като резултат референция към клас:
def F(Alpha):
    # Вътрешен клас:
    class Bravo:
        value=Alpha()
    Bravo.__name__="My"+Alpha.__name__
    return Bravo
# Описание на клас:
class Charlie:
    # Конструктор:
    def __init__(self):
        self.number=123
    # Метод за показване стойността на полето:
    def show(self):
        print("Поле number:",self.number)
# Създаване на обект на основата на клас,
# получен при извикването на функцията:
obj=F(Charlie)()
# Проверка на резултата:
obj.value.show()
print("Клас на обекта obj:",obj.__class__.__name__)
print("Клас на полето value:",obj.value.__class__.__name__)
