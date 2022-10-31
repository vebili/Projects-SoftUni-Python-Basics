# Списък:
A=[10,20,30,40]
# Оператор за цикъл:
for k in [0,1,2,"три",4,3]:
    # Контролируем код:
    try:
        print("* Стойност на елемент A["+str(k)+"]: ",end="")
        A[k]/=(k-1)
        print(A[k])
    # Обработка на изключения:
    except (TypeError,IndexError) as error:
        print()
        print("Изключение на класа",error.__class__.__name__)
        print(error.__doc__)
        print("Базов клас:", error.__class__.__bases__[0].__name__)
    except ZeroDivisionError as error:
        print()
        print("Стана грешка при деление на нула")
        print("Верига от наследявания:")
        for s in error.__class__.__mro__:
            print(s.__name__)
        A[k]=0.0
        print("На елемента е присвоена стойност",A[k])
