txt=input("Въведете текст: ")
symb=input("Каква буква да намеря? ")
num=txt.count(symb)
if num==0:
    print("В текста няма такава буква!")
else:
    print(f"В текста има {num} буква(и) '{symb}'")
