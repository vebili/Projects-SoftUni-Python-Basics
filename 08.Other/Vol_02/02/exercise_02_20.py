# Създаване на итератор:
vals=iter([100,"A",[1,2]])
# Обхождане на итератора:
try:
    print("Първо:",next(vals))
    print("Второ:",next(vals))
    print("Трето:",next(vals))
    print("Четвърто:",next(vals))
except StopIteration:
    print("Няма повече стойности")
