# Функции с произволно количество аргументи:
def sqr_sum(*n):
    s=0
    for a in n:
       s+=a*a
    return s
def get_sum(*n):
    s=0
    for a in n:
        if type(a)==int:
           s+=a
    return s
def get_text(*t):
    return " ".join(t)
# Извикване на функциите:
print("Сума на квадратите:",sqr_sum(1,3,5))
print("Сума на квадратите:",sqr_sum(2,4,6,8,10))
print("Сума на числата:",get_sum(2,"A",4,"B",6))
print("Сума на числата:",get_sum(1,[2,3],4))
print("Сума на числата:",get_sum())
print("Текст:",get_text("Привет","на всички"))
print("Текст:",get_text("A","B","C","D"))
