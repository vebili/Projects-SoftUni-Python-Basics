# Първи базов клас:
class Alpha:
    def alpha(self):
        print("Клас Alpha")
# Втори базов клас:
class Bravo:
    def bravo(self):
        print("Клас Bravo")
# Трети базов клас:
class Charlie:
    def charlie(self):
        print("Клас Charlie")
# Производен клас:
class Delta(Alpha,Bravo,Charlie):
    pass
# Йерархия на наследяванията:
print("Наследяване:")
k=1
for s in Delta.__mro__:
    print("["+str(k)+"]",s.__name__)
    k+=1
# Обект на производния клас:
obj=Delta()
# Извикване на методи:
obj.alpha()
obj.bravo()
obj.charlie()
