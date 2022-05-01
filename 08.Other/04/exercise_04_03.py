# Създаване на множества:
A={2*k+1 for k in range(5)}
B={2*k for k in range(5)}
C={2*k+1 for k in range(3,8)}
# Съдържание на множествата:
print("Създадени са множествата:")
print("A =",A)
print("B =",B)
print("C =",C)
# Обединение на множества:
print("Обединение на множества:")
print("A | B =",A.union(B))
print("B | A =",B.union(A))
print("A | C =",A|C)
# Сечение на множества:
print("Сечение на множества:")
print("A & B =",A.intersection(B))
print("A & C =",A&C)
# Разлика на множества:
print("Разлика на множества:")
print("A - C =",A-C)
print("C - A =",C.difference(A))
# Симетрична разлика на множества:
print("Симетрична разлика на множества:")
print("A ^ C =",A^C)
print("C ^ A =",C.symmetric_difference(A))
# Изходни множества:
print("Изходни множества:")
print("A =",A)
print("B =",B)
print("C =",C)
