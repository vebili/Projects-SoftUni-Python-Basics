# Клас на итератора:
class MyClass:
    # Конструктор:
    def __init__(self,*vals):
        L=[]
        for v in vals:
           if type(v)==int:
               if v<10 and v>0:
                   L.append(v)
        self.digits=L
        self.position=-1
    # Методът се извиква при извикване на функция iter():
    def __iter__(self):
        return self
    # Методът се извиква при извикване на функция next():
    def __next__(self):
        self.position+=1
        if self.position<len(self.digits):
            return self.digits[self.position]
        else:
            raise StopIteration
# Създаване на итератор:
A=MyClass(2,"A",12,7,-3,"Hello",9,5,"Alpha")
# Извикване на функция next():
try:
    while True:
        print(next(A),end=" ")
except StopIteration:
    print()
# Създаване на итератор:
B=MyClass(5,"B",1.2,11,-1,"Hi",8,4,"Bravo",3)
# Оператор за цикъл:
for s in B:
    print(s,end=" ")
print()
