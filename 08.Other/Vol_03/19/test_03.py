cards = input().split(', ')
n = int(input())

for i in range(n):
    command = input().split(', ')

    if command[0] == 'Add':
        if command[1] in cards:
            print(f'Card is already in the deck')
        else:
            cards.append(command[1])
            print(f'Card successfully added')

    elif command[0] == 'Remove':
        if command[1] not in cards:
            print(f'Card not found')
        else:
            cards.remove(command[1])
            print(f'Card successfully removed')

    elif command[0] == 'Remove At':
        if not(0 <= int(command[1]) < len(cards)):
            print('Index out of range')
        else:
            print('Card successfully removed')
            cards.pop(int(command[1]))

    elif command[0] == 'Insert':
        if not(0 <= int(command[1]) < len(cards)):
            print('Index out of range')
        else:
            if command[2] in cards:
                print(f'Card is already added')
            else:
                cards.insert(int(command[1]), command[2])
                print(f'Card successfully added')

print(', '.join(cards))