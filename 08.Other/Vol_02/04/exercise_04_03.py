from tkinter import *
# Функция за обработка на натискането на бутона:
def clicked():
    global t
    # Прочитане на съдържанието на текстовото поле
    t=txt.get()
    # Затваряне на прозореца:
    wnd.destroy()
# Създаване на обект за първия прозорец:
wnd=Tk()
# Параметри на прозореца:
wnd.title("Да се запознаем")
wnd.geometry("300x120")
wnd.resizable(False,False)
# Шрифтове:
fnt_1=("Arial",13,"bold")
fnt_2=("Arial",13,"italic")
fnt_3=("Arial",10,"bold")
# Променлива за записване на текста от полето за въвеждане:
t=""
# Създаване на обект за текстовия етикет:
lbl=Label(master=wnd,text="Как се казвате?")
# Шрифт за етикета:
lbl.configure(font=fnt_1)
# Добавяне на етикета в прозореца:
lbl.place(x=10,y=20)
# Създаване на обект за полето за въвеждане:
txt=Entry(master=wnd,width=30)
# Шрифт за полето за въвеждане:
txt.configure(font=fnt_2)
# Разполагане на текстовото поле в прозореца:
txt.place(x=10,y=50)
# Създаване на обекти за бутоните:
btn_1=Button(master=wnd,text="OK")
btn_2=Button(master=wnd,text="Отмени")
# Параметри на бутоните:
btn_1.configure(font=fnt_3)
btn_1.configure(command=clicked)
btn_2.configure(font=fnt_3)
btn_2.configure(command=wnd.destroy)
# Разполагане на бутоните в прозореца:
btn_1.place(x=40,y=80,width=100,height=30)
btn_2.place(x=150,y=80,width=100,height=30)
# Показване на първия прозорец на екрана:
wnd.mainloop()
# Ако потребителят е въвел текст:
if t!="":
    # Създаване на обект за втория прозорец:
    msg=Tk()
    # Параметри на втория прозорец:
    msg.title("Запознанството се състоя")
    msg.geometry("320x100")
    msg.resizable(False,False)
    # Етикет със съобщението за втория прозорец:
    lbl=Label(master=msg,text="Много ни е приятно, "+t+"!", relief=GROOVE)
    # Шрифт за етикета:
    lbl.configure(font=fnt_1)
    # Разполагане на етикета във втория прозорец:
    lbl.place(x=10,y=10,height=40,width=300)
    # Създаване на обект за бутона:
    btn=Button(master=msg,text="OK")
    # Шрифт за бутона:
    btn.configure(font=fnt_3)
    # Метод за обработка на натискането на бутона:
    btn.configure(command=msg.destroy)
    # Разполагане на бутона във втория прозорец:
    btn.place(x=110,y=60,width=100,height=30)
    # Показване на втория прозорец на екрана:
    msg.mainloop()
