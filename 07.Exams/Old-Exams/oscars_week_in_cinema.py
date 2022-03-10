movie = input()
room = input()
tickets = int(input())
price = 0

if movie == 'A Star Is Born':
    if room == 'normal':
        price = 7.50
    elif room == 'luxury':
        price = 10.50
    else:
        price = 13.50
elif movie == 'Bohemian Rhapsody':
    if room == 'normal':
        price = 7.35
    elif room == 'luxury':
        price = 9.45
    else:
        price = 12.75
elif movie == 'Green Book':
    if room == 'normal':
        price = 8.15
    elif room == 'luxury':
        price = 10.25
    else:
        price = 13.25
else:
    if room == 'normal':
        price = 8.75
    elif room == 'luxury':
        price = 11.55
    else:
        price = 13.95
print(f'{movie} -> {tickets * price:.2f} lv.')
