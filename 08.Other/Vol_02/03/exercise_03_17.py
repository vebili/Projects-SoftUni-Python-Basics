from threading import *
from time import sleep
# Функция за изчисление на сума:
def mysum(n,N):
    res=0
    for k in range(N+1):
        res+=k**n
        sleep(0.1)
    return res
# Функция за изпълнение в дъщерна нишка:
def display(n,N):
    # Блокиране на блокиращия обект:
    mylock.acquire()
    # Получаване на референция към текущата нишка:
    t=current_thread()
    # Показване на името на нишката:
    print("Нишка:",t.name)
    print("Слагаеми:",N)
    print("Степен:",n)
    # Резултат от изчисленията:
    print("Сума:",mysum(n,N))
    print("-------------")
    # Разблокиране на блокиращия обект:
    mylock.release()
# Създаване на блокиращ обект:
mylock=Lock()
# Списък с имената на нишките:
names=["Alpha","Bravo","Charlie","Delta"]
# Създаване на списък с обекти на нишки:
T=[Thread(target=display,args=[k+1,10],name=names[k]) for k in range(len(names))]
# Стартиране на нишките:
for t in T:
    t.start()
# Изчакване края на изпълнението на нишките:
for t in T:
    t.join()
