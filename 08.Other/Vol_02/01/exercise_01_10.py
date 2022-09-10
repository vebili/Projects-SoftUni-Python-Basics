# Първи клас:
class Alpha:
    "Това е клас Alpha"
    pass
# Втори клас:
class Bravo:
    "Това е клас Bravo"
    pass
# Информация за класовете:
print(Alpha.__doc__)
print(Bravo.__doc__)
# Обекти на класовете:
A=Alpha()
B=Bravo()
# Изменение на документиращия низ:
Alpha.__doc__="Първи клас"
B.__class__.__doc__="Втори клас"
# Информация за класовете:
print(A.__class__.__doc__)
print(B.__doc__)
