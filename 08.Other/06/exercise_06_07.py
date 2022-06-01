# Стойността по подразбиране за аргумента е списък:
def show(val=[0,1,2]):
    for k in range(len(val)):
       val[k]+=1;
    print(val)
# Извикване на функцията:
show()
show()
show()
