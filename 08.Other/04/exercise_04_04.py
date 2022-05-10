# Създаване на множества:
A = {0, 5, 10, 15, 20}
B = {10, 15, 20, 25, 30}
# Съдържание на множествата:
print("Създадените множества:")
print("A =", A)
print("B =", B)
# Сечение на множества:
print("Сечение на множествата A и B:")
A.intersection_update(B)
print("A =", A)
# Обединение на множества:
print("Обединение с множеството {1,20,100}:")
A.update({1, 20, 100})
print("A =", A)
# Разлика на множества:
print("Разлика на множествата B и A:")
B.difference_update(A)
print("B =", B)
# Симетрична разлика на множества:
print("Симетрична разлика на множествата B и {30,35}:")
B.symmetric_difference_update({30, 35})
print("B =", B)