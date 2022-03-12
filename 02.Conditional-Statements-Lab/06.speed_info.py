num1 = float(input())
result = 'Invalid Speed Entrance!'

if num1 <= 10:
    result = 'slow'

elif 10 < num1 <= 50:
    result = 'average'

elif 50 < num1 <= 150:
    result = 'fast'

elif 150 < num1 <= 1000:
    result = 'ultra fast'

elif 1000 < num1:
    result = 'extremely fast'

print(result)
