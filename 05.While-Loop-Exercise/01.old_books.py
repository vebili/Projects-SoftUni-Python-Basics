book = input()
num_checks = 0
current_book = input()
book_is_found = False

while current_book != "No More Books":
    if current_book == book:
        book_is_found = True
        break
    num_checks += 1
    current_book = input()
if book_is_found:
    print(f'You checked {num_checks} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {num_checks} books.')
