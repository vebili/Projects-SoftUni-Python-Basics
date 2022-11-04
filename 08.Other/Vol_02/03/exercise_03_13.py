from threading import *
from time import sleep
# Функция за изпълнение в нишка:
def calc(txt,op):
    # Глобална променлива:
    global number
    # Оператор за цикъл:
    for k in range(3):
        # Блокиране на ресурса:
        mylock.acquire()
        print(txt,": ресурсът е блокиран",sep="")
        # Контролируем код:
        try:
            # Прочитане стойността на променливата:
            print(txt,"прочетено:",number)
            # Запомняне на стойността на променливата:
            val=number
            # Пауза в изпълнението на нишката:
            sleep(1)
            # Изменение на стойността на променливата:
            if op:
                number=val+1
            else:
                number=val-1
            # Показване стойността на променливата:
            print(txt," записано:",number)
        # Кодът се изпълнява винаги:
        finally:
            print(txt,": ресурсът е разблокиран",sep="")
            print("-----------------------")
            # Разблокиране на ресурса:
            mylock.release()
        # Пауза в изпълнението на нишката:
        sleep(1)
# Начална стойност на глобалната променлива:
number=0
# Блокиращ обект:
mylock=Lock()
# Обекти на дъщерните нишки:
A=Thread(target=calc,args=["A",True])
B=Thread(target=calc,args=["B",False])
# Стартиране на дъщерните нишки:
A.start()
B.start()
# Изчакване приключването на нишките:
A.join()
B.join()
