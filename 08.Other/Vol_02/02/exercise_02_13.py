# Клас със специални методи:
class Alpha:
    # Метод за получаване на достъп до атрибут:
    def __getattribute__(self,name):
        print("Alpha: заявка за полето",name)
        return object.__getattribute__(self,name)
    # Методът се извиква, ако атрибутът не съществува:
    def __getattr__(self,name):
        print("Няма такова поле!")
        return "Alpha: "+name
# Клас със специални методи:
class Bravo:
    # Метод за получаване на достъп до атрибут:
    def __getattribute__(self,name):
        print("Bravo: заявка за полето",name)
        try:
            res=object.__getattribute__(self,name)
        except AttributeError:
            res="Bravo: не съществува поле "+name
        return res
# Създаване на обекти и обръщане към полетата:
print("Обект A на класа Alpha")
A=Alpha()
A.value=123
print("Поле value:",A.value)
print("Още веднъж:",object.__getattribute__(A,"value"))
A.value=321
print("Поле value:",A.value)
print(A.color)
print("Обект B на класа Bravo")
B=Bravo()
B.mylist=[1,2,3]
print("Поле mylist:",B.mylist)
print("Още веднъж:",object.__getattribute__(B,"mylist"))
B.mylist=["A","B","C"]
print("Поле mylist:",B.mylist)
print(B.myset)
