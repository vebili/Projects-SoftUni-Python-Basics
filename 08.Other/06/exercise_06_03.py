# Функции:
def alpha():
    print("Това е Alpha!")
def bravo():
    print("Това е Bravo!")
def hello():
    print("А това е Hello!")
# Променлива с целочислена стойност:
num=123
# Извикване на функциите и проверка на 
# стойността на променливата:
print("В началото беше така:")
alpha()
bravo()
hello()
print("num =",num)
# Промяна на стойностите:
alpha,bravo=bravo,alpha
num=hello
hello=321
# Извикване на „функциите“ и проверка на стойността на
# „променливата“:
print("А стана така:")
alpha()
bravo()
num()
print("hello =",hello)
