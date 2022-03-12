tax_per_year = int(input())

sneakers = tax_per_year * 0.6
equipment = sneakers * 0.8
ball = equipment / 4
accessory = ball / 5
total = tax_per_year + sneakers + equipment + ball + accessory

print(f'{total:.2f}')
