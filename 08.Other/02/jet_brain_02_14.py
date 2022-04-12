print("Операции със списък с числа...")
# Контролируем код:
try:
    nums = eval(input("Въведете числов списък: "))
    print("Получена стойност: " + str(nums))
    a = int(nums[0])
    b = int(nums[3])
    print(str(a) + "/" + str(b) + "=" + str(a / b))
# Обработка на изключения:
except ValueError:
    print("ValueError: грешка при преобразуване!")
except ZeroDivisionError:
    print("ZeroDivisionError: опит за деление на нула!")
except TypeError:
    print("TypeError: недопустима операция!")
except IndexError:
    print("IndexError: неверен индекс на елемента!")
except SyntaxError:
    print("SyntaxError: невъзможно е изразът да бъде изчислен!")
except NameError:
    print("NameError: неверен идентификатор!")
print("Край на програмата.")
