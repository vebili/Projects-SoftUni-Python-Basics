budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())

price_per_video_card = 250 * video_card
price_per_processor = price_per_video_card * 0.35
price_per_ram = price_per_video_card * 0.1
total_price = price_per_video_card + price_per_processor * processor + price_per_ram * ram
if video_card > processor:
    total_price *= 0.85
total = abs(budget - total_price)
if budget >= total_price:
    print(f'You have {total:.2f} leva left!')
else:
    print(f"Not enough money! You need {total:.2f} leva more!")
