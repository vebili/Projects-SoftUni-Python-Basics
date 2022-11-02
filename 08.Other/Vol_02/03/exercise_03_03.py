# Списък:
A = [10, 20, 30, 40]
# Оператор за цикъл:
for k in [0, 1, 2, "три", 4, 3]:
    # Външен блок:
    try:
        print("* Стойност на елемент A[" + str(k) + "]:")
        # Вътрешен блок:
        try:
            A[k] /= (k - 1)
            print(A[k])
        # Вътрешен блок за обработка:
        except ZeroDivisionError:
            print("Опит за деление на нула")
            A[k] = 0.0
            print("Нова стойност", A[k])
        # Блокът се изпълнява, ако не възникне грешка:
        else:
            print("Грешка при деление на нула няма")
        # Блокът се изпълнява винаги:
        finally:
            print("# Край на вътрешния блок")
    # Външен блок за обработка:
    except:
        print("Нещо се обърка")
print("Край на изпълнението на програмата")
