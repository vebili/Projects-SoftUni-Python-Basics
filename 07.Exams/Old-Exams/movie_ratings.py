import sys

movies = int(input())
best_movie = 0
best_rating = 0
min_rating = sys.maxsize
rating_counter = 0
stupid_movie = 0
for movie in range(movies):
    movie_name = input()
    rating = float(input())
    if rating > best_rating:
        best_rating = rating
        best_movie = movie_name
    if rating < min_rating:
        min_rating = rating
        stupid_movie = movie_name
    rating_counter += rating

print(f"{best_movie} is with highest rating: {best_rating}")
print(f"{stupid_movie} is with lowest rating: {min_rating}")
print(f"Average rating: {rating_counter / movies:.1f}")
