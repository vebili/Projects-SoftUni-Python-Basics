# Функция за решение на линейно уравнение:
def solve(A, B):
    # Контролируем код:
    try:
        # Преобразуване към числов формат:
        a = float(A)
        b = float(B)
    # Обработка на изключения:
    except:
        # Генериране на изключение:
        raise ValueError("Неверен формат на данните")
    # Проверка на стойностите на коефициентите:
    if a == 0:
        if b != 0:
            # Генериране на изключение:
            raise ArithmeticError("Няма решение")
        else:
            # Генериране на изключение:
            raise Warning("Решение е всяко число")
    # Резултат на функцията:
    return b / a


# Използване на функцията за решение на уравнения:
print("* Решаваме линейни уравнения")
# Списъци с коефициентите за уравненията:
A = [2.5, 2, "три", 10, 0, 0.0]
B = [3.0, 4, 0, "пет", 5, 0]
# Извикване на функцията с различни аргументи:
for k in range(len(A)):
    a = A[k]
    b = B[k]
    print("[", k + 1, "] Уравнение: ", a, "*x = ", b, sep="")
    # Контролируем код:
    try:
        print("x =", solve(a, b))
    # Обработка на изключения:
    except ValueError as error:
        print("Неприятна ситуация №1")
        print(error)
    except ArithmeticError as error:
        print("Неприятна ситуация №2")
        print(error)
    except Warning as error:
        print("Странна ситуация")
        print(error)
print("* Всички уравнения са решени")
