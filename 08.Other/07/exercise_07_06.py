# Импортиране на класа от модула:
from datetime import time
# Обект за реализация на момент от време:
mytime=time(13,35,20)
# Проверка на резултата:
print("Време:",mytime)
# Използване на полетата на обекта:
print("Часове:",mytime.hour)
print("Минути:",mytime.minute)
print("Секунди:",mytime.second)
# Създаване на нов обект на основата на съществуващ:
newtime=mytime.replace(15,second=45)
# Проверка на резултата:
print("Време:",newtime)
# Създаване на нов обект:
mytime=time.fromisoformat("12:34:56")
# Проверка на резултата:
print("Време:",mytime)
