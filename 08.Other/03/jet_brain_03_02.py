# Създаване на списъци:
A=[10,20,30]
print("A:",A)
B=["Python",[1,2]]
print("B:",B)
# Изчисление на сума на списъци:
C=A+B
print("C:",C)
# Добавяне на елемент в края на списъка:
C+=[100]
print("C:",C)
# Изтриване на елемент от списъка:
C[1:2]=[]
print("C:",C)
# Добавяне на елемент в началото на списъка:
C=[200]+C
print("C:",C)
# Замяна на няколко елемента в списъка:
C[:3]=["A","B"]
print("C:",C)
# Вмъкване на елемент в списъка:
C[2:2]=[8,9]
print("C:",C)
# Присвояване на стойност на елемент на списъка:
C[2:3]=[7]
print("C:",C)
