# Функция със стойности на аргументите по подразбиране:
def show(first,second="Bravo",third="Charlie"):
    print(f"[1] - {first}")
    print(f"[2] - {second}")
    print(f"[3] - {third}")
    print("-"*13)
# Извикване на функцията:
show("Alpha")
show("A","B","C")
show(10,20)
show(100,third=300)
show(third="трети",first="първи")
