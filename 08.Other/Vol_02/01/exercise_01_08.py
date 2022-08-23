# Първи клас:
class Alpha:
    pass
# Втори клас:
class Bravo:
    name="Bravo"
    def display():
        print("Поле name:",Bravo.name)
    def show(self):
        print("Поле value:",self.value)
    def __init__(self):
        self.value=123
# Създаване на обекти:
A=Alpha()
B=Bravo()
# Атрибути на първия клас:
print("Клас Alpha")
n=1
for s in Alpha.__dict__:
    print("["+str(n)+"] "+s+":",Alpha.__dict__[s])
    n+=1
# Атрибути на втория клас:
print("Клас Bravo")
n=1
for s in Bravo.__dict__:
    print("["+str(n)+"] "+s+":",Bravo.__dict__[s])
    n+=1
# Атрибути на обектите:
print("Обект A:",A.__dict__)
print("Обект B:",B.__dict__)
# Извикване на метода на класа:
Bravo.display()
# Създаване на атрибут на класа:
Alpha.display=Bravo.display
# Изтриване на атрибут на класа:
del Bravo.display
# Извикване на метода от обекта:
B.show()
# Създаване на атрибут на класа:
A.color="Червен"
# Създаване на атрибут на обекта:
B.show=lambda: print("Обект B:",B.value)
# Атрибути на първия клас:
print("Клас Alpha")
n=1
for s in Alpha.__dict__:
    print("["+str(n)+"] "+s+":",Alpha.__dict__[s])
    n+=1
# Атрибути на втория клас:
print("Клас Bravo")
n=1
for s in Bravo.__dict__:
    print("["+str(n)+"] "+s+":",Bravo.__dict__[s])
    n+=1
# Атрибути на обектите:
print("Обект A:",A.__dict__)
print("Обект B:",B.__dict__)
# Извикване на методи:
Alpha.display()
Bravo.show(B)
B.show()
