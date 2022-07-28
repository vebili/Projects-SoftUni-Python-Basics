# Импортиране на класа от модула:
from datetime import datetime

# Обект за реализация на дата и време:
md = datetime(2019, 10, 22, 13, 27, 45)
# Проверка на резултата:
print("Дата и време:", md)
# Използване на полетата на обекта:
print("Година:", md.year)
print("Месец:", md.month)
print("Число:", md.day)
print("Часове:", md.hour)
print("Минути:", md.minute)
print("Секунди:", md.second)
# Определяне на деня от седмицата:
print("Ден от седмицата:", md.weekday())
print("Ден от седмицата:", md.isoweekday())
# Дата:
d = md.date()
# Проверка на резултата:
print("Дата:", d)
# Време:
t = md.time()
# Проверка на резултата:
print("Време:", t)
# Създаване на нов обект на основата на съществуващ:
nd = md.replace(1985, day=3, second=15)
# Проверка на резултата:
print("Дата и време:", nd)
# Създаване на нов обект:
nd = datetime.fromisoformat("1998-08-12 11:25:36")
# Проверка на резултата:
print("Нова дата и време:", nd)
# Обект за текущата дата и време:
td = datetime.today()
# Проверка на резултата:
print("Днес и сега:", td)
# Разлика на дати:
delta = md - td
# Проверка на резултата:
print("Интервал от време:", delta)
print("Дни:", delta.days)
print("Секунди:", delta.seconds)
print("Интервал в секунди:", delta.total_seconds())
