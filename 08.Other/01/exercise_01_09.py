# Прочитане на броя на слагаемите:
n = input("Посочете броя на слагаемите: ")
# Променлива с текстова стойност:
txt = "1"
# Индексна променлива:
k = 1
# Оператор за цикъл за формиране на текста с израза
# за сумата на естествените числа:
while str(k) != n:
    # Увеличаване стойността на индексната променлива:
    k = k + 1
    # Добавяне на фрагмент към текста с израза
    # за сумата на естествените числа:
    txt = txt + "+" + str(k)
# Показване на резултата:
print(txt, "=", eval(txt))
# Нова версия
print(f"{txt} = {eval(txt)}")
