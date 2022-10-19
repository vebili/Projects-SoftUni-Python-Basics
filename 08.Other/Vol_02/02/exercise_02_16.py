# Клас със специални методи:
class Alpha:
    # Методът се извиква, ако атрибутът не съществува:
    def __getattr__(self,name):
        return "такъв атрибут не съществува"
    # Методът се извиква при изтриване на атрибут:
    def __delattr__(self,name):
        if name=="number":
            print("Не може да бъде изтрит!")
        else:
            object.__delattr__(self,name)
# Създаване на обект:
A=Alpha()
# Операции с полетата на обекта:
A.value="обект A"
print("value:",A.value)
del A.value
print("value:",A.value)
A.number=123
print("number:",A.number)
del A.number
print("number:",A.number)
del A.__dict__["number"]
print("number:",A.number)
