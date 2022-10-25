# Клас със специален метод:
class Alpha:
    def __call__(self,n):
        s=0
        for k in range(len(self.nums)):
           s+=self.nums[k]**n
        return s
# Клас със специален метод:
class Bravo:
    def __call__(self,x,y):
       return self.num*x+self.val*y
# Създаване на обект:
A=Alpha()
A.nums=[1,2,3]
# Извикване на обекта:
print("A(1) =",A(1))
print("A(2) =",A(2))
# Създаване на обект:
B=Bravo()
B.num=2
B.val=3
# Извикване на обекта:
print("B(5,1) =",B(5,1))
print("B(3,4) =",B(3,4))
