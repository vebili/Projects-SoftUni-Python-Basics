number1 = int(input())
number2 = int(input())

units1 = number1 % 10
tens1 = number1 // 10 % 10
hundreds1 = number1 // 100 % 10
thousands1 = number1 // 1000

units2 = number2 % 10
tens2 = number2 // 10 % 10
hundreds2 = number2 // 100 % 10
thousands2 = number2 // 1000

for thousands in range(thousands1, thousands2 + 1):
    for hundreds in range(hundreds1, hundreds2 + 1):
        for tens in range(tens1, tens2 + 1):
            for units in range(units1, units2 + 1):
                check1 = units % 2 != 0
                check2 = tens % 2 != 0
                check3 = hundreds % 2 != 0
                check4 = thousands % 2 != 0
                if check1 and check2 and check3 and check4:
                    print(f'{thousands}{hundreds}{tens}{units}', end=' ')
