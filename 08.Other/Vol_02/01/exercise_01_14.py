# Функция за създаване на обекти:
def create(fields,vals,name=None):
    # Ако последният аргумент не е текстов:
    if type(name)!=str:
        name="MisterX"
    # Ако първите два аргумента не са списъци:
    if type(fields)!=list or type(vals)!=list:
        # Вътрешен клас:
        class MyClass:
            # Метод:
            def show(self):
                print("Обект без полета ")
                print("Клас",self.__class__.__name__)
    # Ако първите два аргумента са списъци:
    else:
        # Втори клас:
        class MyClass:
            # Конструктор:
            def __init__(self):
                k=0
                for f in fields:
                    self.__dict__[f]=vals[k]
                    k+=1
            # Метод:
            def show(self):
                print("Обект с полета:")
                for s in dir(self):
                    if not s.startswith("_") and s!="show":
                        print(s,"=",self.__dict__[s])
                print("Клас",self.__class__.__name__)
    # Име на класа:
    MyClass.__name__=name
    # Резултат от функцията:
    return MyClass()
# Създаване на обект и проверка на полетата:
A=create(["red","green","blue"],[1,2,3],"MyColors")
A.show()
# Създаване на обект и проверка на полетата:
B=create(["alpha","bravo"],["Alpha","Bravo"])
B.show()
# Създаване на обект и проверка на полетата:
C=create(1,2,3)
C.show()
# Изменение на стойностите на полетата на обекта:
A.red=100
A.green=200
A.blue=300
A.show()
# Създаване на обект и проверка на полетата:
D=A.__class__()
D.show()
