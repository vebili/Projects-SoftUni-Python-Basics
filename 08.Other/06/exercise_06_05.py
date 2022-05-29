# Функции:
def shift(val):
    print("Функция shift()")
    print("Изходна стойност:",val)
    val=["A","B","C"]
    print("Крайна стойност:",val)
def change(val):
    print("Функция change()")
    print("Изходна стойност:",val)
    if type(val)==list:
        for k in range(len(val)):
            val[k]+=1
    else:
        val+=1
    print("Крайна стойност:",val)
# Променлива:
num=100
# Списък:
L=[10,20,30]
# Извикване на функциите:
print(f"Променлива num={num}")
change(num)
print(f"Променлива num={num}")
print(f"Списък L={L}")
shift(L)
print(f"Списък L={L}")
change(L)
print(f"Списък L={L}")
