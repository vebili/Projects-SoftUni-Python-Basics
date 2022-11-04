from threading import Thread
from time import sleep
# Клас за създаване на обект, който може да се извиква:
class MyClass:
    # Конструктор:
    def __init__(self,text):
        self.text=text
    # Методът се извиква при извикването на обекта:
    def __call__(self,count,time):
        for k in range(count):
            sleep(time)
            print("[",k+1,"] ",self.text,sep="")
print("Започва изпълнението на програмата")
# Създаване на обект:
obj=MyClass("Дъщерна нишка")
# Създаване на обект на дъщерната нишка:
t=Thread(target=obj,kwargs={"time":2,"count":5})
# Стартиране на дъщерната нишка:
t.start()
# Извикване на анонимен обект в главната нишка:
MyClass("Главна нишка")(3,1.5)
# Изчакване приключването на дъщерната нишка:
if t.is_alive():
    t.join()
print("Край на изпълнението на програмата")
