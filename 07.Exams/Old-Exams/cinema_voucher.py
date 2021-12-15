voucher = int(input())
product = input()
movie = 0
other = 0
price = 0
while product != 'End':
    if len(product) > 8:
        for num, letter in enumerate(product):
            if num == 0:
                price += ord(letter)
            elif num == 1:
                price += ord(letter)
            else:
                break
        if price > voucher:
            break
        else:
            movie += 1
    else:
        for num, letter in enumerate(product):
            if num == 0:
                price += ord(letter)
        if price > voucher:
            break
        else:
            other += 1
    product = input()
print(movie)
print(other)
