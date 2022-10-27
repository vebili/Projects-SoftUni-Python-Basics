# Първи клас:
class Alpha:
    # Конструктор:
    def __init__(self,*vals):
        L=[]
        for v in vals:
           if type(v)==int:
               L.append(v)
        self.nums=L
    # Методът се извиква при извикване на функция iter():
    def __iter__(self):
        return Bravo(self.nums)
# Втори клас:
class Bravo:
    # Конструктор:
    def __init__(self,nums):
        L=[]
        for n in nums:
            if n<10 and n>0:
                L.append(n)
        self.digits=L
        self.position=-1
    # Методът се извиква при извиква на функция next():
    def __next__(self):
        self.position+=1
        if self.position<len(self.digits):
            return self.digits[self.position]
        else:
            raise StopIteration
# Създаване на обект на класа Alpha:
A=Alpha(2,"A",12,7,-3,"Hello",9,5,"Alpha")
# Създаване на обект на класа Bravo:
B=iter(A)
# Извикване на функция next():
try:
    while True:
        print(next(B),end=" ")
except StopIteration:
    print()
