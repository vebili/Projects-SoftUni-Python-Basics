# Импортиране на класа от модула:
from datetime import date

# Обект за реализация на дата:
myday = date(2019, 10, 22)
# Проверка на резултата:
print("Първа дата:", myday)
# Използване на полетата на обекта:
print("Година:", myday.year)
print("Месец:", myday.month)
print("Число:", myday.day)
# Определяне на деня от седмицата:
print("Ден от седмицата:", myday.weekday())
print("Ден от седмицата:", myday.isoweekday())
# Създаване на нов обект на основата на съществуващия:
newday = myday.replace(1985, day=15)
# Проверка на резултата:
print("Втора дата:", newday)
# Създаване на нов обект:
newday = date.fromisoformat("1998-08-12")
# Проверка на резултата:
print("Нова дата:", newday)
# Обект за текущата дата:
thisday = date.today()
# Проверка на резултата:
print("Днес:", thisday)
# Разлика на дати:
delta = myday - thisday
# Проверка на резултата:
print("До първата дата:", delta)
