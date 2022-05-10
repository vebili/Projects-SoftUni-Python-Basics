# Импортиране на функция за създаване на пълно копие:
from copy import deepcopy
# Изходен речник:
A={"едно":1,"две":"двойка","три":[3,4]}
# Повърхностно копие на речник:
B=dict(A)
C=A.copy()
# Пълно копие на речник:
D=deepcopy(A)
# Показване на резултата:
print("A =",A)
print("B =",B)
print("C =",C)
print("D =",D)
# Промяна на стойностите на елементите на изходния речник:
A["два"]=2
A["три"][1]=5
# Проверка на резултата:
print("A =",A)
print("B =",B)
print("C =",C)
print("D =",D)