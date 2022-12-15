# Импортиране на класовете от пакета:
from tkinter import *
# Създаване на обект на прозореца:
wnd=Tk()
# Заглавие за прозореца:
wnd.title("Прозорец с бутон")
# Геометрични размери на прозореца:
wnd.geometry("250x150")
# Прозорец с постоянни размери:
wnd.resizable(False,False)
# Създаване на обекта на етикета:
lbl=Label(wnd,text="Привет!",font=("Arial Bold",20))
# Разполагане на етикета върху прозореца:
lbl.place(x=40,y=30)
# Обект на бутона:
btn=Button(wnd,text="Затвори",font=("Courier New Bold",13), command=wnd.destroy)
# Разполагане на обекта на бутона в прозореца:
btn.place(x=40,y=100,width=170,height=30)
# Показване на прозореца на екрана:
wnd.mainloop()
