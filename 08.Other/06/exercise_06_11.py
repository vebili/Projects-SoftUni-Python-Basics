# Функция с вложена функция:
def mysum(*a):
    # Списък:
    txt=["числата","квадратите","кубовете"]
    # Вложена функция:
    def calc(n):
        s=0
        for m in range(len(a)):
            s+=a[m]**n
        return s
    # Извикване на вложената функция:
    for k in range(len(txt)):
        print("Сума на ",txt[k]+":",calc(k+1))
# Извикване на функцията:
mysum(1,3,5,7)
