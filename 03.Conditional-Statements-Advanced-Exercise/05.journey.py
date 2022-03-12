budget = float(input())
season = input()
sleep_price = 0
destination = 0
where_to_sleep = 0

if season == 'summer':
    if budget <= 100:
        sleep_price = budget * 0.3
        destination = 'Bulgaria'
    elif budget <= 1000:
        sleep_price = budget * 0.4
        destination = 'Balkans'
    elif budget > 1000:
        sleep_price = budget * 0.9
        destination = 'Europe'
elif season == 'winter':
    if budget <= 100:
        sleep_price = budget * 0.7
        destination = 'Bulgaria'
    elif budget <= 1000:
        sleep_price = budget * 0.8
        destination = 'Balkans'
    elif budget > 1000:
        sleep_price = budget * 0.9
        destination = 'Europe'
if season == 'summer' and not destination == 'Europe':
    where_to_sleep = 'Camp'
else:
    where_to_sleep = 'Hotel'

print(f'Somewhere in {destination} \n{where_to_sleep} - {sleep_price:.2f}')
