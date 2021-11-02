budget = float(input())
actor_name = input()

salary = 0
flag = True

while actor_name != 'ACTION':
    if len(actor_name) > 15:
        salary += budget * 0.2
    else:
        salary = float(input())
    if budget - salary > 0:
        budget -= salary
    else:
        print(f"We need {abs(budget - salary):.2f} leva for our actors.")
        flag = False
        break
    salary = 0
    actor_name = input()

if flag is True:
    print(f"We are left with {budget:.2f} leva.")
