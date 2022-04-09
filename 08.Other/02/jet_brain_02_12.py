# Въвеждане на израз:
val=eval(input("Въведете израз: "))
# Използване на тернарен оператор:
a,b=(val[0],val[-1]) if type(val)==str else (val,type(val))
# Стойности на променливите:
print(a)
print(b)
