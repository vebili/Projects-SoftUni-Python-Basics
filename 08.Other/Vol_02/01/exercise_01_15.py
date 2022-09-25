# Клас:
class MyClass:
    # Конструктор:
    def __init__(self,name,n=1):
        self.name=name
        if n==1:
            self.next=None
        else:
            self.next=MyClass(self.name,n-1)
        self.set()
    # Деструктор:
    def __del__(self):
        print("Изтриване:",self.code)
    # Метод за запълване на веригата с кодове:
    def set(self,num=1):
        self.code=self.name+"["+str(num)+"]"
        if self.next!=None:
            self.next.set(num+1)
     # Метод за показване на кодовете на обектите 
     # във веригата:
    def show(self):
        print(self.code)
        if self.next!=None:
            self.next.show()
# Създаване на верига обекти:
print("Един обект:")
A=MyClass("Alpha")
A.show()
print("Верига обекти:")
B=MyClass("Bravo",5)
B.show()
print("Започвайки от третия обект:")
B.next.next.show()
# Изтриване на обекти:
print("Изтриване на обекти:")
del A
del B
