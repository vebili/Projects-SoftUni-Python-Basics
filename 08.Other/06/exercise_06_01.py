# Функция без аргументи, която не връща резултат:
def next_day():
    txt=input("Кой ден от седмицата сме? ")
    txt=txt.lower().strip()
    if txt=="понеделник":
       new_txt="вторник"
    elif txt=="вторник":
       new_txt="сряда"
    elif txt=="сряда":
       new_txt="четвъртък"
    elif txt=="четвъртък":
       new_txt="петък"
    elif txt=="петък":
       new_txt="събота"
    elif txt=="събота":
       new_txt="неделя"
    elif txt=="неделя":
       new_txt="понеделник"
    else:
       print("Няма такъв ден от седмицата!")
       return
    print(f"Утре сме {new_txt}")
# Функция без аргументи, връщаща резултат:
def get_name():
    name=input("Добър ден! Как се казвате? ")
    if name.strip(" .,:;!?_")=="":
       name="Господин Хикс"
    return name
# Функция без аргументи, която не връща резултат:
def hello():
    name=get_name()
    print(f"Приятно ни е да се запознаем, {name}!")
    next_day()
# Извикване на функцията:
hello()
