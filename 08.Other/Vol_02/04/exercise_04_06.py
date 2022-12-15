from tkinter import *
from tkinter.messagebox import *
# Клас за създаване на прозорец:
class MyApp:
    # Конструктор:
    def __init__(self):
        # Настройка на параметрите:
        self.setValues()
        # Създаване на главния прозорец:
        self.makeMainWindow()
        # Определяне на „променливите“ за обработка на 
          # събитията:
        self.setVars()
        # Създаване на главното меню:
        self.makeMainMenu()
        # Създаване на лента с инструменти:
        self.makeToolBar()
        # Създаване на спомагателен панел:
        self.makeFrame()
        # Създаване на контекстно меню:
        self.makePopupMenu()
        # Изчисление на параметрите на шаблонния текст:
        self.apply()
        # Режим на проследяване на „променливите“:
        self.traceVars()
        # Показване на главния прозорец:
        self.showMainWindow()
    # Метод за настройка на параметрите:
    def setValues(self):
        # Широчина и височина на прозореца:
        self.W=500
        self.H=200
        # Височина на лентата с инструментите:
        self.h=40
        # Размери на главния прозорец:
        self.position=str(self.W)+"x"+str(self.H)
        # Имена на шрифтовете:
        self.fonts=["Times New Roman","Arial","Courier New"]
        # Речник с имената на цветовете:
        self.colors={"red":"Червен","blue":"Син", "black":"Черен"}
        # Списък с имената на стиловете:
        self.style=[["bold","Удебелен"],["italic","Курсив"]]
        # Списък с имената на файловете с изображенията:
        self.imgFiles=["exit.png","bold.png","italic.png", "normal.png"]
        # Път към папката с файловете:
        self.path="H:\\Book\\Python\\Examples\\Pictures\\"
        # Основен шрифт:
        self.font=("Courier New",10,"bold")
    # Метод за създаване на главния прозорец:
    def makeMainWindow(self):
        self.wnd=Tk()
        self.wnd.title("Определяме шрифт")
        self.wnd.geometry(self.position)
        self.wnd.resizable(False,False)
    # Метод за показване на главния прозорец:
    def showMainWindow(self):
        self.wnd.mainloop()
    # Метод за създаване на главното меню:
    def makeMainMenu(self):
        # Създаване на обекта за лентата на менюто:
        self.menubar=Menu(self.wnd)
        # Създаване на елементите на менюто:
        self.mFont=Menu(self.wnd,font=self.font,tearoff=0)
        self.mStyle=Menu(self.wnd,font=self.font,tearoff=0)
        self.mColor=Menu(self.wnd,font=self.font,tearoff=0)
        self.mAbout=Menu(self.wnd,font=self.font,tearoff=0)
        # Запълване на елементите на менюто:
        self.setMenuFont(self.mFont)
        self.setMenuStyle(self.mStyle)
        self.setMenuColor(self.mColor)
        # Запълване на последния елемент на менюто:
        self.mAbout.add_command(label="За програмата",command=self.showDialog)
        # Добавяне на разделител:
        self.mAbout.add_separator()
        self.mAbout.add_command(label="Изход", command=self.clExit)
        # Добавяне на елементите в меню лентата:
        self.menubar.add_cascade(label="Шрифт", menu=self.mFont)
        self.menubar.add_cascade(label="Стил", menu=self.mStyle)
        self.menubar.add_cascade(label="Цвят", menu=self.mColor)
        self.menubar.add_cascade(label="Програма", menu=self.mAbout)
        # Задаваме главно меню за прозореца:
        self.wnd.config(menu=self.menubar)
    # Метод за създаване на лентата с инструментите:
    def makeToolBar(self):
        # Списък с имената на методите за обработка 
        # на събитията, свързани с натискане на бутоните:
        mt=[self.clExit,self.clBold,self.clItalic, self.clNormal]
        # Лента за бутоните:
        self.toolbar=Frame(self.wnd,bd=3,relief=GROOVE)
        # Списък с изображенията:
        self.imgs=[]
        # Списък с бутоните:
        self.btns=[]
        # Създаване на изображенията и бутоните:
        for f in self.imgFiles:
            # Създаване на изображенията:
            self.imgs.append(PhotoImage(file=self.path+f))
            # Създаване на бутоните:
            self.btns.append(Button(self.toolbar, image=self.imgs[-1]))
            # Добавяне на бутоните в лентата:
            self.btns[-1].pack(side="left",padx=2,pady=2)
        # Определяне на обработчици за бутоните:
        for k in range(len(mt)):
            self.btns[k].configure(command=mt[k])
        # Създаване на текстов етикет:
        self.lblSize=Label(self.toolbar,text="Размер на шрифта:",font=self.font)
        # Разполагане на етикета в панела:
        self.lblSize.pack(side="left",padx=2,pady=2)
        # Създаване на поле за избор на цифра:
        self.spnSize=Spinbox(self.toolbar,from_=15,to=20, font=self.font,width=3,justify="right", textvariable=self.size)
        # Разполагане на полето за избор на цифра в панела:
        self.spnSize.pack(side="left",padx=2,pady=2)
        # Разполагане на лентата в прозореца:
        self.toolbar.place(x=3,y=3,width=self.W-6, height=self.h)
    # Метод за създаване на спомагателен панел:
    def makeFrame(self):
        # Създаване на спомагателен панел:
        self.frame=Frame(self.wnd,bd=3,relief=GROOVE)
        # Създаване на етикет и добавянето му в панела:
        Label(self.frame,text="Примерен текст:", font=self.font).pack(side="top")
        # Създаване на етикет за шаблонния текст:
        self.lblText=Label(self.frame, textvariable=self.text,relief=GROOVE,bg="white",height=5)
        # Поставяне на етикета в спомагателния панел:
        self.lblText.pack(side="top",fill="both",padx=1, pady=1)
        # Разполагане на спомагателния панел в прозореца:
        self.frame.place(x=3,y=self.h+9,width=self.W-6, height=self.H-self.h-12)
    # Метод за създаване на контекстно меню:
    def makePopupMenu(self):
        # Създаване на обекта на контекстното меню:
        self.popup=Menu(self.wnd,tearoff=0,font=self.font)
        # Добавяне на команди в контекстното меню:
        self.setMenuFont(self.popup)
        # Добавяне на разделител:
        self.popup.add_separator()
        # Добавяне на команди в контекстното меню:
        self.setMenuStyle(self.popup)
        # Добавяне на разделител:
        self.popup.add_separator()
        # Добавяне на команди в контекстното меню:
        self.setMenuColor(self.popup)
        # Добавяне на разделител:
        self.popup.add_separator()
        # Добавяне на команда в контекстното меню:
        self.popup.add_command(label="Изход", command=self.clExit)
        # Определяне на обработчик за събитията
        # на контекстното меню:
        self.wnd.bind("<Button-3>",lambda evt: self.popup.tk_popup(evt.x_root,evt.y_root))
    # Метод за формиране на командите на менюто,
    # свързани с избора на шрифта:
    def setMenuFont(self,menu):
        for f in self.fonts:
            menu.add_radiobutton(label=f,value=f, variable=self.name)
        self.name.set(self.fonts[0])
    # Метод за формиране на командите на менюто,
    # свързани с избора на стил:
    def setMenuStyle(self,menu):
        for k in range(len(self.style)):
            menu.add_checkbutton(label=self.style[k][1], onvalue=True,offvalue=False,variable=self.bi[k])
        self.bi[0].set(True)
        self.bi[1].set(False)
    # Метод за формиране на командите на менюто,
    # свързани с избора на цвят:
    def setMenuColor(self,menu):
        for r in self.colors.keys():
            menu.add_radiobutton(label=self.colors[r], value=r,variable=self.color)
        self.color.set("blue")
    # Метод за определяне на параметрите на шрифта и
    # изчисление на шаблонния текст:
    def apply(self,*args):
        # Цвят за шрифта:
        clr=self.color.get()
        # Име на шрифта:
        nm=self.name.get()
        # Размер на шрифта:
        sz=self.size.get()
        # Прилагане на цвета към етикета:
        self.lblText.configure(fg=clr)
        # Списък с параметрите на шрифта:
        fnt=[nm,sz]
        # Формиране на шаблонния текст и определяне
        # параметрите на шрифта:
        txt=self.colors[clr]+" шрифт "+nm+"\n"
        for k in range(len(self.style)):
            if self.bi[k].get():
               fnt.append(self.style[k][0])
               txt+=self.style[k][1].lower()+" "
        txt+="размер "+str(sz)
        # Прилагане на шрифта към етикета:
        self.lblText.configure(font=fnt)
        # Задаваме текст за етикета:
        self.text.set(txt)
    # Метод за създаване на „променливите“ за събитията:
    def setVars(self):
        self.text=StringVar()
        self.name=StringVar()
        self.bi=[BooleanVar(),BooleanVar()]
        self.size=IntVar()
        self.color=StringVar()
    # Метод за преминаване в режим на следене
    # на стойностите на „променливите“:
    def traceVars(self):
        mt=self.apply
        self.name.trace("w",mt)
        self.color.trace("w",mt)
        for k in range(len(self.bi)):
            self.bi[k].trace("w",mt)
        self.size.trace("w",mt)
    # Метод за обработка на бутона за излизане от 
    # програмата:
    def clExit(self):
        self.wnd.destroy()
    # Метод за обработка на бутона
    # за прилагане/отмяна на удебелен стил:
    def clBold(self):
        self.bi[0].set(not self.bi[0].get())
    # Метод за обработка на бутона
    # за прилагане/отмяна на курсивен стил:
    def clItalic(self):
        self.bi[1].set(not self.bi[1].get())
    # Метод за обработка на бутона
    # за отмяна на удебеления и курсивния стил:
    def clNormal(self):
        self.bi[0].set(False)
        self.bi[1].set(False)
    # Метод за обработка на прозореца със съобщението:
    def showDialog(self):
        showinfo("За програмата","Много проста програма")
# Показване на прозореца на екрана:
MyApp()
