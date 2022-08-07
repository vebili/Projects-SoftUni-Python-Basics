# Създаване на речници:
A = dict(zip([1, 2, 3], ['K', 'L', 'M']))
B = dict.fromkeys([10, 20, 30], 'Z')
# Показване на резултата:
print("A =", A)
print("B =", B)
# Сравняване на речници:
print("Сравнение на речници:")
print("A==B:", A == B)
print("A!=B:", A != B)
# Добавяне на един речник в друг:
A.update(B)
# Проверка на резултата:
print("Обединение на речници:")
print("A =", A)
# Проверка на съдържанието на речника:
print("Проверка на съдържанието на речника:")
print((20, 'Z') in A.items())
print(20 in A)
print('Z' in A)
print(5 not in A)
# Изчистване на речника:
A.clear()
# Проверка на резултата:
print("Речникът след изчистването:")
print("A =", A)