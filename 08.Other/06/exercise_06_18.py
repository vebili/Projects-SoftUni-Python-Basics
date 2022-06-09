# Функция с анотации:
def show(txt:"Текст"="Функция show()")->"Няма резултат":
    print(txt)
# Извикване на функцията:
show()
# Речник с анотациите:
print(show.__annotations__)
# Анотации:
for k in show.__annotations__:
    print(k,"-",show.__annotations__[k])
