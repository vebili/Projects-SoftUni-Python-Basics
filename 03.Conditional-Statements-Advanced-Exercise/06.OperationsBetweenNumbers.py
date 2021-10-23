n1 = int(input())
n2 = int(input())
operator = input()
area = 0
ev_od = 0
if n2 == 0 and operator == '/' or n2 == 0 and operator == '%':
    print(f'Cannot divide {n1} by zero')
elif operator == '-':
    area = n1 - n2
    if area % 2 == 0:
        ev_od = 'even'
    else:
        ev_od = 'odd'
elif operator == '+':
    area = n1 + n2
    if area % 2 == 0:
        ev_od = 'even'
    else:
        ev_od = 'odd'
elif operator == '*':
    area = n1 * n2
    if area % 2 == 0:
        ev_od = 'even'
    else:
        ev_od = 'odd'
elif operator == '/':
    area = n1 / n2
    print(f"{n1} / {n2} = {area:.2f}")
elif operator == '%':
    area = n1 % n2
    print(f"{n1} % {n2} = {area}")
if operator == '-' or operator == '+' or operator == '*':
    print(f"{n1} {operator} {n2} = {area} - {ev_od}")