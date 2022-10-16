# Клас със специален метод:
class Alpha:
    # Методът се извиква, ако атрибутът не съществува:
    def __getattr__(self,name):
        return len(name)
# Клас със специален метод:
class Bravo:
    # Обикновен метод:
    def show(self,x):
        print("Метод show():",x)
    # Методът се извиква, ако атрибутът не съществува:
    def __getattr__(self,name):
        if len(name)<5:
            return lambda x: print("Първи метод:",x)
        else:
            return lambda x: print("Втори метод:",x*x)
# Създаване на обекти и обръщане към атрибутите им:
print("Обект A на класа Alpha")
A=Alpha()
A.value="Alpha"
print("Поле value:",A.value)
print("Поле color:",A.color)
print("Поле myattribute:",A.myattribute)
print("Обект B на класа Bravo")
B=Bravo()
B.show(10)
B.hi(10)
B.display(10)
