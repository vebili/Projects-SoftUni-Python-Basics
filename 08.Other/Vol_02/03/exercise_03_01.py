# Списък:
A=[10,20,30,40]
# Оператор за цикъл:
for k in [0,1,2,"три",4,3]:
    # Контролиран код:
    try:
        print("A["+str(k)+"] = ",end="")
        A[k]/=(k-1)
        print(A[k])
    # Обработка на изключения:
    except IndexError:
        print("няма такъв елемент")
    except ZeroDivisionError:
        A[k]=0.0
        print(A[k],"- деление на нула")
    except TypeError:
        print("неверен тип на индекса")
