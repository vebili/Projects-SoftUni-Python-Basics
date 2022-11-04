from threading import Thread
from time import sleep
# Функции за изпълнение в дъщерните нишки:
def from_left():
    global first,last,L
    val=10
    while True:
        if first<last:
            L[first]=val
            val+=10
            first+=1
            sleep(0.3)
        else:
            break
def from_right():
    global first,last,L
    val="A"
    while True:
        if first<last:
            L[last]=val
            val=chr(ord(val)+1)
            last-=1
            sleep(0.3)
        else:
            break
# Размер на списъка:
size=11
# Създаване на списък:
L=["*" for k in range(size)]
# Начален и краен индекс:
first=0
last=len(L)-1
print("Списък за запълване:")
print(L)
# Създаване на обекти на дъщерните нишки:
A=Thread(target=from_left)
B=Thread(target=from_right)
# Стартиране на нишките:
A.start()
B.start()
# Изчакване нишките да завършат:
A.join()
B.join()
# Резултат от запълването на списъка:
print("Списъкът след запълването:")
print(L)
