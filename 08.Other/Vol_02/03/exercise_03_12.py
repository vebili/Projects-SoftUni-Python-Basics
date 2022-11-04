from threading import Thread
from time import sleep
# Производен клас:
class MyThread(Thread):
    # Конструктор:
    def __init__(self,count,time,text):
        # Извикване на конструктора на базовия клас:
        super().__init__()
        # Присвояване на стойности на полетата:
        self.count=count
        self.time=time
        self.text=text
    # Предефиниране на метода за изпълнение в нишката:
    def run(self):
        for k in range(self.count):
            sleep(self.time)
            print("[",k+1,"] ",self.text,sep="")
print("Започва изпълнението на програмата ")
# Създаване на обекти за дъщерните нишки:
A=MyThread(5,2,"Alpha")
B=MyThread(3,1.5,"Bravo")
# Стартиране на дъщерните нишки:
A.start()
B.start()
# Изчакване завършването на дъщерните нишки:
if A.is_alive():
    A.join()
if B.is_alive():
    B.join()
print("Край на изпълнението на програмата")
