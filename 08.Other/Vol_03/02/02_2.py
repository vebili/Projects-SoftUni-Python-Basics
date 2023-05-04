import re

text = input()
pattern = r"(@|#)+(?P<color>[a-z]{3,})\W+/+(?P<amount>\d+)/+"

valid = [obj.groupdict() for obj in re.finditer(pattern, text)]

for text in valid:
    amount, color =(text["amount"], text["color"])
    print(f"You found {amount} {color} eggs!")