from tkinter import *
from math import *
# Функция за обработка на събитието, свързано
# с поднасяне на курсора над областта за рисуване:
def msEnter(evt):
    # Смяна на изображението:
    cnv.itemconfig(Pct,image=img_2)
# Функция за обработка на събитието, свързано
# с излизане на курсора извън областта за рисуване:
def msLeave(evt):
    # Смяна на изображението:
    cnv.itemconfig(Pct,image=img_1)
    # Изтриване на „старите“ линии до курсора:
    cnv.delete("ln")
# Функция за обработка на събитието, свързано
# с преместване на курсора в областта за рисуване:
def msMotion(evt):
    # Координатите на курсора в областта за рисуване:
    x=evt.x
    y=evt.y
    # Изтриване на „старите“ линии:
    cnv.delete("ln")
    # Показване на линии:
    cnv.create_line(x,5,x,H-5,fill=clr_C1,width=2,tag="ln")
    cnv.create_line(5,y,W-5,y,fill=clr_C1,width=2,tag="ln")
    # Координати на правоъгълника:
    Rxy=cnv.coords(Rtn)
    # Координати на окръжността:
    Cxy=cnv.coords(Crl)
    # Координати на центъра на окръжността:
    x0=(Cxy[2]+Cxy[0])/2
    y0=(Cxy[3]+Cxy[1])/2
    # Разстоянието от курсора до центъра на окръжността:
    r=sqrt((x-x0)**2+(y-y0)**2)
    # Ако курсорът се намира в очертанията на окръжността:
    if r<R:
        # Бял цвят за запълване на окръжността:
        cnv.itemconfig(Crl,fill=clr_C2)
        # Червен цвят за запълване на правоъгълника:
        cnv.itemconfig(Rtn,fill=clr_C1)
        # Край на изпълнението на функцията:
        return
    # Ако курсорът се намира извън окръжността:
    else:
        # Червен цвят за запълване на окръжността:
        cnv.itemconfig(Crl,fill=clr_C1)
    # Ако курсорът се намира в очертанията на правоъгълника:
    if x>Rxy[0] and x<Rxy[2] and y>Rxy[1] and y<Rxy[3]:
        # Зелен цвят за запълване на правоъгълника:
        cnv.itemconfig(Rtn,fill=clr_R2)
    # Ако курсорът се намира извън правоъгълника:
    else:
        # Бял цвят за запълване на правоъгълника:
        cnv.itemconfig(Rtn,fill=clr_R1)
# Функция за обработка на събитието, свързано
# с натискане на клавиша „нагоре“:
def msUp(evt):
    # Групата с линиите се премества с един пиксел нагоре:
    cnv.move("Lns",0,-1)
    # Окръжността се премества с три пиксела надолу:
    cnv.move(Crl,0,3)
# Функция за обработка на събитието, свързано
# с натискане на клавиша „надолу“:
def msDown(evt):
    # Групата с линиите се премества с един пиксел надолу:
    cnv.move("Lns",0,1)
    # Окръжността се премества с три пиксела нагоре:
    cnv.move(Crl,0,-3)
# Функция за обработка на събитието, свързано
# с натискане на бутона „наляво“:
def msLeft(evt):
    # Текстът се премества с една позиция наляво:
    cnv.move(Txt,-1,0)
# Функция за обработка на събитието, свързано
# с натискане на бутона „надясно“:
def msRight(evt):
    # Текстът се премества с една позиция надясно:
    cnv.move(Txt,1,0)
# Широчина и височина на областта за рисуване:
W=600
H=400
# Широчина и височина на правоъгълника:
w=200
h=100
# Брой на линиите:
N=10
# Декремент за дължината на линиите:
d=20
# Радиус на окръжността:
R=30
# Шрифт:
fnt=("Arial",20,"bold")
# Текст:
txt="Син текст"
# Цвят за линиите:
clr="lightgreen"
# Цвят за фона на областта за рисуване:
clr_1="lightyellow"
clr_2="yellow"
# Цвят за запълване на окръжността:
clr_C1="red"
clr_C2="white"
# Цвят за запълване на правоъгълника:
clr_R1="white"
clr_R2="green"
# Създаване на обекта на прозореца:
wnd=Tk()
# Размери и разположение на прозореца:
wnd.geometry(str(W+10)+"x"+str(H+10)+"+400+300")
# Заглавие за прозореца:
wnd.title("Графика")
# Прозорецът е с постоянни размери:
wnd.resizable(False,False)
# Създаване на обекта на областта за рисуване:
cnv=Canvas(wnd,bg=clr_1,bd=3,relief=GROOVE)
# Разполагане на областта за рисуване в прозореца:
cnv.place(x=5,y=5,width=W,height=H)
# Предаване на фокус в областта за рисуване:
cnv.focus_set()
# Създаване на текстов елемент:
Txt=cnv.create_text(W/2,50,text=txt,font=fnt,fill="blue")
# Създаване на групата хоризонтални линии:
for k in range(N):
    # Координати на линиите:
    x1=70+k*d
    y1=H/4+10*k
    x2=W-70-d*k
    y2=H/4+10*k
    cnv.create_line(x1,y1,x2,y2,fill=clr,width=5,tag="Lns")
# Координати за окръжността:
x1=W/2-R
y1=H/2-R+30
x2=W/2+R
y2=H/2+R+30
# Създаване на окръжността:
Crl=cnv.create_oval(x1,y1,x2,y2,fill=clr_C1)
# Координати за правоъгълника:
x1=20
y1=H-h-20
x2=x1+w
y2=y1+h
# Създаване на правоъгълника:
Rtn=cnv.create_rectangle(x1,y1,x2,y2,fill=clr_R1)
# Създаване на обектите с изображенията:
img_1=PhotoImage(file="H:\\Book\\Python\\Examples\\Pictures\\sad.png")
img_2=PhotoImage(file="H:\\Book\\Python\\Examples\\Pictures\\smile.png")
# Създаване на обекта на изображението:
Pct=cnv.create_image(W-20,H-20,anchor=SE,image=img_1)
# Регистрация на обработчици:
cnv.bind("<Left>",msLeft)
cnv.bind("<Right>",msRight)
cnv.bind("<Up>",msUp)
cnv.bind("<Down>",msDown)
cnv.bind("<Enter>",msEnter)
cnv.bind("<Leave>",msLeave)
cnv.bind("<Motion>",msMotion)
cnv.bind("<Button-1>",lambda evt: cnv.config(bg=clr_2))
cnv.bind("<Button-3>",lambda evt: cnv.config(bg=clr_1))
# Показване на главния прозорец:
wnd.mainloop()
