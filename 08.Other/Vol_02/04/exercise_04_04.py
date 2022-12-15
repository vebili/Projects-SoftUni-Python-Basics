# Импортиране на съдържанието на пакета:
from tkinter import *
# Импортиране на клас от подпакета:
from tkinter.ttk import Combobox
# Функция за обработката на събитията, свързани с избиране
# на елемент в падащия списък:
def change(evt):
    # Прочитане на избраната стойност в списъка:
    t=cb.get()
    # Определяне на изображението по избраната стойност:
    for k in range(len(names)):
        # Ако избраната стойност съвпада с текст в списъка:
        if t==names[k]:
            # Ново изображение в етикета:
            lbl.configure(image=imgs[k])
            # Край на оператора за цикъл:
            break
# Променлива с път към файловете с изображенията:
path="H:\\Book\\Python\\Examples\\Pictures\\"
# Имената на животните:
names=["Тигър","Лъв","Мечка"]
# Имената на файловете с изображенията:
files=["tiger.png","lion.png","bear.png"]
# Създаване на обект на прозореца:
wnd=Tk()
# Параметри на прозореца:
wnd.title("Хищници")
wnd.geometry("220x300")
wnd.resizable(False,False)
# Списък с обектите за изображенията:
imgs=[PhotoImage(file=path+f) for f in files]
# Индекс за избрания в началото елемент:
index=0
# Създаване на обект на етикета:
lbl=Label(wnd,image=imgs[index])
# Параметри на етикета и разполагането му в прозореца:
lbl.configure(relief=GROOVE)
lbl.place(x=10,y=10,width=200,height=200)
# Създаване на обект за падащия списък:
cb=Combobox(wnd,state="readonly")
# Съдържание на падащия списък:
cb.configure(values=names)
# Избраната в началото стойност (елемент):
cb.current(index)
# Шрифт за падащия списък:
cb.configure(font=("Arial",11,"bold"))
# Определяне на обработчик за събитието, свързано
# избиране на нова стойност в списъка:
cb.bind("<<ComboboxSelected>>",change)
# Разполагане на списъка в прозореца:
cb.place(x=10,y=220,width=200,height=30)
# Създаване на обект за бутона:
btn=Button(wnd,text="OK")
# Определяне на обработчик за събитието натискане на бутона:
btn.configure(command=wnd.destroy)
# Размери на бутона и разполагането му в прозореца:
btn.place(x=60,y=260,width=100,height=30)
# Показване на прозореца на екрана:
wnd.mainloop()
