# Импортиране на класа Thread:
from threading import Thread
# Импортиране на функция sleep():
from time import sleep
# Функция за извикване в главната нишка:
def alpha():
    for k in range(5):
        # Пауза в изпълнението на нишката:
        sleep(1.5)
        print("[",k+1,"] Alpha",sep="")
# Функция за изпълнение в дъщерната нишка:
def bravo():
    for k in range(5):
        print("[",k+1,"] Bravo",sep="")
        # Пауза в изпълнението на нишката:
        sleep(1)
# Създаване на обект на дъщерната нишка:
t=Thread(target=bravo)
# Стартиране на дъщерната нишка:
t.start()
# Извикване на функцията в главната нишка:
alpha()
