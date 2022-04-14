print("Операции със списък с числа...")
try:
    nums=eval(input("Въведете числов списък: "))
    print("Получена стойност: "+str(nums))
    a=int(nums[0])
    b=int(nums[3])
    print(str(a)+"/"+str(b)+"="+str(a/b))
except ZeroDivisionError:
    print("ZeroDivisionError: опит за деление на нула!")
except IndexError:
    print("IndexError: неверен индекс на елемента!")
except:
    print("Грешка!")
print("Край на програмата.")
