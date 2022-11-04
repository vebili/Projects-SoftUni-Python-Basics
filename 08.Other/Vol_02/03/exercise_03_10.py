from threading import Thread
from time import sleep
# Функция с три аргумента:
def display(count,time,text):
    for k in range(count):
        # Пауза в изпълнението на нишката:
        sleep(time)
        print("[",k+1,"] ",text,sep="")
print("Започва изпълнението на програмата")
# Създаване на обект на дъщерната нишка:
t=Thread(target=display,args=(5,2,"Дъщерна нишка"))
# Стартиране на дъщерната нишка:
t.start()
# Извикване на функцията в главната нишка:
display(3,1.5,"Главна нишка")
# Изчакване на дъщерната нишка да приключи:
t.join()
print("Край на изпълнението на програмата")
