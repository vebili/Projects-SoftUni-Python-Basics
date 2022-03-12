bitcoin = int(input())
chinese = float(input())
commission = float(input())

bitcoin = (bitcoin * 1168) / 1.95
chinese = ((chinese * 0.15) * 1.76) / 1.95
euro = bitcoin + chinese - ((bitcoin + chinese) * (commission / 100))
print(f'{euro:.2f}')
