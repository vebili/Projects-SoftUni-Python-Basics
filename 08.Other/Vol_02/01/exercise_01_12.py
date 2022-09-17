# Функция за декоратора:
def F(Alpha):
    class Bravo:
        value=Alpha()
    Bravo.__name__="My"+Alpha.__name__
    return Bravo
# Клас с декоратор:
@F
class Charlie:
    def __init__(self):
        self.number=123
    def show(self):
        print("Поле number:",self.number)
# Създаване на обект:
obj=Charlie()
# Проверка на резултата:
obj.value.show()
print("Клас на обекта obj:",obj.__class__.__name__)
print("Клас на полето value:",obj.value.__class__.__name__)
