# Списък със стойностите на ключовете:
days=["Пн","Вт","Ср","Чт","Пт","Сб","Нд"]
# Създаване на речници:
week={days[s]:s for s in range(len(days))}
myweek={d:days.index(d) for d in days}
# Проверка на резултата:
print(week)
print(myweek)
# Създаване на още един речник:
sqrs={k:k**2 for k in range(1,11) if k%2!=0}
# Проверка на резултата:
print(sqrs)
