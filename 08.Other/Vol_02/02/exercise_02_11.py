# Клас с презаредени оператори:
class Alpha:
    # Конструктор:
    def __init__(self,lst):
        self.vals=[]
        if type(lst)==list:
            for n in lst:
               self.vals.append(n)
    # Метод за привеждане към текстов формат:
    def __str__(self):
        return str(self.vals)
    # Унарен оператор "плюс":
    def __pos__(self):
        x=self.vals[0]
        del self.vals[0]
        self.vals.append(x)
        return self
    # Унарен оператор "минус":
    def __neg__(self):
        x=self.vals[-1]
        del self.vals[-1]
        self.vals.insert(0,x)
        return self
    # Умножение на обект с операнд:
    def __mul__(self,v):
        self.vals.append(v)
        return self
    # Умножение на операнд с обект:
    def __rmul__(self,v):
        self.vals.insert(0,v)
        return self
    # Съкратена форма на операцията за умножение:
    def __imul__(self,v):
        return self*v
# Създаване на обект:
A=Alpha([1,"A",2])
# Изпълнение на операции с обекта:
print(A)
print(+A)
print(-A)
print(A*3)
print(4*A)
A*="Alpha"
print(A)
