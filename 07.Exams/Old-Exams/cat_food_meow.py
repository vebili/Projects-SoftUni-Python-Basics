n = int(input())

points = n - 1
slashes = n
lang = n * 2
brackets = n
spaces = 0

for i in range(1, 2 * n + 7):
    if i == 1 or i == 2 * n + 6:
        print('.' * points + '|' + '\\/' * slashes + '|' + '.' * points)
    if i == 2 or i == 2 * n + 5:
        print('.' * points + '|' + '~' * lang + '|' + '.' * points)
    if i == n + 3:
        print('.' * points + '|' + ' ' * (n - 2) + 'MEOW' + ' ' * (n - 2) + '|' + '.' * points)
    if i == n + 4:
        print('.' * points + '|' + ' ' * (n - 2) + 'FOOD' + ' ' * (n - 2) + '|' + '.' * points)
        spaces -= 1
        brackets += 1
    if 2 < i < n + 3:
        print('.' * points + '|' + ' ' * spaces + '{}' * brackets + ' ' * spaces + '|' + '.' * points)
        spaces += 1
        brackets -= 1
    if n + 4 < i < 2 * n + 5:
        print('.' * points + '|' + ' ' * spaces + '{}' * brackets + ' ' * spaces + '|' + '.' * points)
        spaces -= 1
        brackets += 1
