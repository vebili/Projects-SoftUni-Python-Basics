from tkinter import *
# Функция за определяне характеристиките на шрифта:
def getFont():
    # Празен списък:
    res=[]
    # Име на шрифта:
    name=lst.get(lst.curselection())
    # Размер на шрифта:
    size=scl.get()
    # Добавяне на елементите в списъка:
    res.append(name)
    res.append(size)
    # Ако е отметнато полето за прилагане на удебелен стил:
    if bold.get()!="":
        res.append(bold.get())
    # Ако е отметнато полето за прилагане на курсивен стил:
    if italic.get()!="":
        res.append(italic.get())
    # Резултат от функцията:
    return res
# Функция за прилагане на параметрите на шрифта:
def setAll(*args):
    # Изчисление на шрифта:
    fnt=getFont()
    # Прилагане на шрифта към текста в прозореца:
    lbl.configure(font=fnt)
    # Определяне на цвета за текста в прозореца:
    lbl.configure(fg=color.get())
    # Определяне на шаблонния текст:
    txt="\nШрифт "
    # Име на шрифта:
    txt+=fnt[0]
    # Размер на шрифта:
    txt+=" размер "+str(fnt[1])+"\n"
    # Ако се прилага удебелен стил:
    if "bold" in fnt:
        txt+=" удебелен"
    # Ако се прилага курсивен стил:
    if "italic" in fnt:
        txt+=" курсив"
    # Цвят на шрифта:
    if color.get()=="red":
        txt+=" червен"
    elif color.get()=="blue":
        txt+=" син"
    else:
        txt+=" черен"
    txt+=" цвят\n"
    # Показване на текста в прозореца:
    text.set(txt)
# Списък с характеристиките на шрифтовете:
fnt_1=["Arial",12,"italic"]
fnt_2=["Times New Roman",13,"bold","italic"]
# Списък с имената на шрифтовете за статичния списък:
fonts=["Times New Roman","Arial","Courier New"]
# Минимален размер на шрифта:
min_size=15
# Максимален размер на шрифта:
max_size=21
# Широчина и височина на прозореца:
W=640
H=420
# Височина на панела с шаблонния текст:
Hf=140
# Широчина и височина на панела със статичния списък:
Wl=W/3
Hl=H-Hf-15
# Височина на панела с бутона:
Hb=60
# Широчина и височина на панелите с плъзгача и 
# радиобутоните:
Ws=W-Wl-15
Hs=Hl-Hb-5
# Създаване на прозореца:
wnd=Tk()
wnd.title("Параметри на шрифта")
wnd.geometry(str(W)+"x"+str(H))
wnd.resizable(False,False)
# Създаване на панелите:
frm_scale=Frame(wnd,bd=3,relief=GROOVE)
frm_text=Frame(wnd,bd=3,relief=GROOVE)
frm_btn=Frame(wnd,bd=3,relief=GROOVE)
frm_list=Frame(wnd,bd=3,relief=GROOVE)
frm_check=Frame(frm_list,bd=3,relief=GROOVE)
# Променливи за определяне на текстовото съдържание
# в елементите за управление:
text=StringVar()
color=StringVar()
bold=StringVar()
italic=StringVar()
# Създаване на текстови етикети:
lbl_text=Label(frm_text,text="Примерен текст:",font=fnt_2)
lbl_color=Label(frm_scale,text="Цвят на текста:",font=fnt_2)
lbl_size=Label(frm_scale,text="Размер на текста:",font=fnt_2)
lbl_font=Label(frm_list,text="Име на шрифта:",font=fnt_2)
lbl_style=Label(frm_check,text="Стил на шрифта:",font=fnt_2)
# Етикет за шаблонния текст:
lbl=Label(frm_text,textvariable=text)
# Фон и рамка за етикета:
lbl.configure(bg="white",relief=RAISED)
# Радиобутони:
rb_1=Radiobutton(frm_scale,text="червен",variable=color)
rb_1.configure(value="red",font=fnt_1)
rb_2=Radiobutton(frm_scale,text="син",variable=color)
rb_2.configure(value="blue",font=fnt_1)
rb_3=Radiobutton(frm_scale,text="черен",variable=color)
rb_3.configure(value="black",font=fnt_1)
# Избиране на превключвател:
color.set("blue")
# Създаване на плъзгача:
scl=Scale(frm_scale,orient=HORIZONTAL)
# Диапазон за изменение на стойността:
scl.configure(from_=min_size,to=max_size)
# Интервал за разграфяване на скалата и стъпка на дискретност 
# за изменение:
scl.configure(tickinterval=1,resolution=1)
# Обработчик за събитието, свързано с изменение на плъзгача:
scl.config(command=setAll)
# Създаване на полетата за отметка и настройка на параметрите:
chb_1=Checkbutton(frm_check,text="удебелен",variable=bold)
chb_1.configure(onvalue="bold",offvalue="",font=fnt_1)
chb_2=Checkbutton(frm_check,text="курсив",variable=italic)
chb_2.configure(onvalue="italic",offvalue="",font=fnt_1)
# Начално състояние на полетата за отметка:
bold.set("")
italic.set("italic")
# Създаване на статичен списък:
lst=Listbox(frm_list,selectmode=SINGLE,font=fnt_1)
# Цвят на фона и цвят на селектираното поле:
lst.configure(bg="gray96",selectbackground="gray")
# Начин на селектиране на елемента и височина на списъка:
lst.configure(activestyle="none",height=len(fonts)+1)
# Запълване на статичния списък с елементи:
for n in fonts:
    lst.insert(END,n)
# По подразбиране е избран първият елемент:
lst.select_set(0)
# Обработчик за статичния списък:
lst.bind("<<ListboxSelect>>",setAll)
# Създаване на бутон:
btn=Button(frm_btn,text="OK",font=fnt_2)
# Обработчик за бутона:
btn.configure(command=wnd.destroy)
# Разполагане на етикета и плъзгача в панелите:
lbl_text.pack(side="top",fill="x",padx=5,pady=5)
lbl.pack(side="top",fill="both",padx=5,pady=5)
lbl_color.pack(side="top",fill="x",padx=5,pady=5)
scl.pack(side="bottom",fill="x",padx=5,pady=5)
lbl_size.pack(side="bottom",fill="x",padx=5,pady=[25,5])
lbl_font.pack(side="top",fill="x",padx=5,pady=5)
lbl_style.pack(side="top",fill="x",padx=5,pady=5)
# Разполагане на радиобутоните:
rb_1.pack(side="left",fill="x",padx=5,pady=5)
rb_2.pack(side="left",fill="x",padx=5,pady=5)
rb_3.pack(side="left",fill="x",padx=5,pady=5)
# Разполагане на полетата за отметка:
chb_1.pack(side="left",fill="x",padx=5,pady=5)
chb_2.pack(side="left",fill="x",padx=5,pady=5)
# Разполагане на статичния списък:
lst.pack(side="top",fill="x",padx=5,pady=5)
# Разполагане на бутона:
btn.pack(side="bottom",fill="x",padx=50,pady=10)
# Разполагане на панелите:
frm_text.place(x=5,y=5,width=W-10,height=Hf)
frm_check.pack(side="bottom",fill="both",padx=5,pady=5)
frm_list.place(x=5,y=Hf+10,height=Hl,width=Wl)
frm_scale.place(x=Wl+10,y=Hf+10,width=Ws,height=Hs)
frm_btn.place(x=Wl+10,y=Hf+Hs+15,width=Ws,height=Hb)
# Прилагане на параметрите на шрифта към шаблонния текст:
setAll()
# Режим на проследяване на стойностите на променливите:
color.trace("w",setAll)
bold.trace("w",setAll)
italic.trace("w",setAll)
# Показване на прозореца:
wnd.mainloop()
