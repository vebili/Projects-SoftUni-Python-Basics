import math

word = input()

collection = 0
flag = False
powerful_word = 0
max_point = 0

while word != 'End of words':
    for num, letter in enumerate(word):
        collection += ord(letter)
        if num == 0:
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y' \
                    or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' \
                    or letter == 'Y':
                flag = True
            else:
                flag = False
    if flag is True:
        collection *= len(word)
    if flag is not True:
        collection = math.floor(collection / len(word))
    if max_point < collection:
        max_point = collection
        powerful_word = word
    collection = 0
    word = input()
print(f"The most powerful word is {powerful_word} - {max_point}")
