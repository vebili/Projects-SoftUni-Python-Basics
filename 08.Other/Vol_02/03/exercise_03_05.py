# Клас на изключение:
class MyError(Exception):
    # Конструктор:
    def __init__(self,code=0,msg="Изключение MyError"):
        self.code=code
        self.message=msg
    # Метод за привеждане в текстов формат:
    def __str__(self):
        txt=self.message+"\nКод на грешката: "+str(self.code)
        return txt
# Външен блок с контролируем код:
try:
    print("Създаваме собствена грешка")
    # Вътрешен блок с контролируем код:
    try:
        # Генериране на изключение:
        raise MyError(123)
    # Вътрешен блок за обработка на изключението:
    except MyError as error:
        print(error)
        # Изменение на параметрите на обекта на грешката:
        error.code=321
        error.message="Същата грешка MyError"
        # Повторно генериране на изключението:
        raise
# Външен блок за обработка на изключението:
except Exception as error:
    print(error)
