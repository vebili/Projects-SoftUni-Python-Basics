# Клас със специални методи:
class Alpha:
    # Метод за четене на стойност по индекс:
    def __getitem__(self,index):
        return self.value[index]
    # Метод за присвояване на стойност по индекс:
    def __setitem__(self,index,val):
        self.value[index]=val
    # Метод за изтриване по индекс:
    def __delitem__(self,index):
        del self.value[index]
    # Метод за привеждане към текстов формат:
    def __str__(self):
        return str(self.value)
    # Метод за изчисление на „дължината“ на обекта:
    def __len__(self):
        return len(self.value)
# Създаване на обект:
A=Alpha()
# Поле списък за обекта:
A.value=[100,200,300]
# Проверка на съдържанието на обекта:
print(A)
# Операции с обекта с използване на индекс:
for k in range(len(A)):
    print(A[k],end=" ")
print()
A[1]="A"
print(A)
del A[0]
print(A)
