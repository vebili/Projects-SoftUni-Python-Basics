from threading import *
from time import sleep


# Функция за изпълнение в нишка:
def display(txt):
    a = [1, 2]
    b = ["A", "B"]
    sleep(1)
    # Изчакване поставяне на флаг:
    myevent.wait()
    # Отмяна на флага:
    myevent.clear()
    for a in a:
        print("[", a, "] ", txt, sep="")
    # Поставяне на флаг:
    myevent.set()
    sleep(1)
    # Изчакване поставянето на флаг:
    myevent.wait()
    # Отмяна на флага:
    myevent.clear()
    for b in b:
        print("[", b, "] ", txt, sep="")
    # Поставяне на флаг:
    myevent.set()


# Създаване на обект:
myevent = Event()
# Поставяне на флаг:
myevent.set()
# Обекти на дъщерните нишки:
F = Thread(target=display, args=["Първа"])
S = Thread(target=display, args=["Втора"])
# Стартиране на дъщерните нишки:
F.start()
S.start()
# Изчакване приключването на дъщерните нишки:
F.join()
S.join()
