# Импортиране на функции:
from copy import *
# Описание на класа:
class MyClass:
    pass
# Създаване на обект:
A=MyClass()
# Полета на обекта:
A.value=100
A.nums=[1,2,3]
# Присвояване на референция към обекта:
B=A
# Копие на обекта:
C=copy(A)
# Пълно копие на обекта:
D=deepcopy(A)
print("Създадени са обектите")
# Полета на обектите:
print("A:",A.value,"и",A.nums)
print("B:",B.value,"и",B.nums)
print("C:",C.value,"и",C.nums)
print("D:",D.value,"и",D.nums)
print("A.value=200 и A.nums[1]=0")
# Нови стойности за полетата:
A.value=200
A.nums[1]=0
# Полета на обектите:
print("A:",A.value,"и",A.nums)
print("B:",B.value,"и",B.nums)
print("C:",C.value,"и",C.nums)
print("D:",D.value,"и",D.nums)
print("Изтрива се A")
# Изтриване на променлива:
del A
print("B.value=300 и B.nums[2]=4")
# Нови стойности за полетата:
B.value=300
B.nums[2]=4
# Полета на обектите:
print("B:",B.value,"и",B.nums)
print("C:",C.value,"и",C.nums)
print("D:",D.value,"и",D.nums)
