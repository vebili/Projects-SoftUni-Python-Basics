from math import pi

figure = input("")

if figure == "square":
    a = float(input())
    area1 = a*a
    print(f'{area1:.3f}')
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area2 = a*b
    print(f'{area2:.3f}')
elif figure == "circle":
    r = float(input())
    area3 = pi * (r*r)
    print(f'{area3:.3f}')
elif figure == "triangle":
    b = float(input())
    h = float(input())
    area4 = b / 2 * h
    print(f'{area4:.3f}')