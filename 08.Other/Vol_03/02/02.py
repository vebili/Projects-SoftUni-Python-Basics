import re
input_text = input()

regex = r"[@#]+(?P<color>[a-z]{3}[a-z]*)[@#]\W*\D*\/(?P<amount>[0-9]+)\/"
matches = re.finditer(regex, input_text)

for match in matches:
    color = match.group("color")
    amount = int(match.group("amount"))
    print(f"You found {amount} {color} eggs!")
