movie = input()

counter = 0
points = 0
max_points = 0
favorite_movie = 0

while movie != 'STOP':
    counter += 1
    for letter in movie:
        points += ord(letter)
        if 96 < ord(letter) < 123:
            points -= (len(movie) * 2)
        elif 64 < ord(letter) < 91:
            points -= len(movie)
    if points > max_points:
        max_points = points
        favorite_movie = movie
    points = 0
    if counter == 7:
        print("The limit is reached.")
        break
    movie = input()

print(f'The best movie for you is {favorite_movie} with {max_points} ASCII sum.')
