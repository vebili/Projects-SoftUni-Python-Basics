command = input()
count_of_steps = 0

while command != 'Going home':
    steps = int(command)
    count_of_steps += steps
    if count_of_steps >= 10000:
        break
    command = input()
else:
    steps_to_home = int(input())
    count_of_steps += steps_to_home

if count_of_steps >= 10000:
    surplus_steps = count_of_steps - 10000
    print('Goal reached! Good job!')
    print(f'{surplus_steps} steps over the goal!')
else:
    needed_steps = 10000 - count_of_steps
    print(f'{needed_steps} more steps to reach goal.')
