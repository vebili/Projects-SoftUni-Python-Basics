import re

text=input()

pattern = r"(#|@)+(?P<color>[a-z]{3,})(#|@)+([^A-Za-z0-9])*(/+?)(?P<amount>[0-9]+)(/+?)"

valid_eggs=re.finditer(pattern,text)
for egg in valid_eggs:
    current=egg.groupdict()
    print(f"You found {current['amount']} {current['color']} eggs!")