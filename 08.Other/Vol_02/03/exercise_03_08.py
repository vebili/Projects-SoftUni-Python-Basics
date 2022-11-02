# Клас на изключение:
class MyError(Exception):
    # Конструктор:
    def __init__(self):
        self.values=[]
    # Методът обработва операцията събиране:
    def __add__(self,val):
        self.values.append(val)
        return self
# Функция с рекурсивно извикване, генерираща изключение:
def getMyError(n):
    # Контролируем код:
    try:
        if n<=1:
            # Генериране на изключение:
            raise MyError
        # Рекурсивно извикване на функцията:
        getMyError(n-1)
    # Обработка на изключение:
    except MyError as error:
        # Генериране на изключение:
        raise error+n
# Функция за създаване на списък:
def getList(n):
    # Контролируем код:
    try:
        # Извикване на функцията, генерираща изключение:
        getMyError(n)
    # Обработка на изключението:
    except MyError as error:
        # Резултат от функцията:
        return error.values
# Създаване на списъци:
A=getList(10)
print(A)
B=getList(7.5)
print(B)
