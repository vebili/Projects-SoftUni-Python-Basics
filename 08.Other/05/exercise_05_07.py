txt=input("Въведете текст: ")
symb=input("Каква буква да намеря? ")
num=txt.find(symb)
L=[]
while num!=-1:
    L.append(num)
    num=txt.find(symb,num+1)
if len(L)==0:
    print("Такава буква в текста няма!")
else:
    print(f"Позиции на буквата '{symb}' в текста: {L}")
