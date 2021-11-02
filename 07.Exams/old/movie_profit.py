movie_name = input()
days = int(input())
tickets = int(input())
price_tickets = float(input())
percent_per_cinema = int(input())

profit = days * tickets * price_tickets
total_profit = profit * percent_per_cinema / 100
profit = profit - total_profit

print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")
