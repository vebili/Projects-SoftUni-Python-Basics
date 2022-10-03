# Базов клас:
class Alpha:
    # Методи:
    def display(self):
        print("Метод от Alpha")
        print("Поле code:",self.code)
    def show(self):
        self.display()
# Производен клас:
class Bravo(Alpha):
    # Предефиниране на метода:
    def display(self):
        print("Метод от Bravo")
        print("Поле name:",self.name)
# Създаване на обекти:
A=Alpha()
A.code=123
B=Bravo()
B.name="B"
# Извикване на методите:
A.show()
B.show()
