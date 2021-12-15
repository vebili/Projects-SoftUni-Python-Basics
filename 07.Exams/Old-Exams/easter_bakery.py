bakers = int(input())
eggs = int(input())
kg_cake = int(input())

baker_price = 3.2
eggs_price = 4.35
eggs_color = 0.15
cake_price = 5.4

total_price = bakers * baker_price + cake_price * kg_cake + eggs * eggs_price + (eggs * 12) * eggs_color
print(f'{total_price:.2f}')
