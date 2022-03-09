type_of_food = input()

if type_of_food == 'banana' or type_of_food == 'apple' or type_of_food == 'kiwi' \
        or type_of_food == 'cherry' or type_of_food == 'lemon' or type_of_food == 'grapes':
    print('fruit')
elif type_of_food == 'tomato' or type_of_food == 'cucumber' or type_of_food == 'pepper' or type_of_food == 'carrot':
    print('vegetable')
else:
    print('unknown')
