from tkinter import *
 
class Paint(Frame):
    def __init__(self, parent):
         Frame.__init__(self, parent)
         self.parent = parent
         # Параметри на четката по подразбиране
         self.brush_size = 10
         self.brush_color = "red"
         self.color = "red"
         # Разполагаме UI компонентите
         self.setUI()
    # Метод за рисуване върху платното     
    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                          event.y - self.brush_size,
                          event.x + self.brush_size,
                          event.y + self.brush_size,
                          fill=self.color, outline=self.color)
    # Промяна на цвета на четката
    def set_color(self, new_color):
        self.color = new_color
    # Промяна на размера на четката
    def set_brush_size(self, new_size):
        self.brush_size = new_size
    def setUI(self):
        # Задаваме заглавие на прозореца
        self.parent.title("Simple Paint")
        # Поставяме активните елементи върху родителския прозорец
        self.pack(fill=BOTH, expand=1)  

        # Нека 7-ата колона да се разтяга, бутоните няма да се променят
        self.columnconfigure(6, weight=1)
        # Същото, но за третия ред
        self.rowconfigure(2, weight=1) 

        # Нашето платно, бял фон
        self.canv = Canvas(self, bg="white")

        # Прикрепяме платното с метод grid. То ще се намира на 
        # третия ред, първата колона, и ще заема 7 колони,
        # задаваме отстъпи по X и Y от по 5 пиксела и задаваме
        # да се разтяга при разтягане на целия прозорец
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)
        # Задаваме реакция на платното при натискане 
  # на левия бутон на мишката
        self.canv.bind("<B1-Motion>", self.draw)

        # Създаваме надпис за бутоните за промяна на цвета на четката
        color_lab = Label(self, text="Color: ")
        # Поставяме създадения надпис на първия ред в първата колона,
        # задаваме хоризонтален отстъп от 6 пиксела
        color_lab.grid(row=0, column=0, padx=6) 

        # Създаваме бутон:  Задаване на текст и широчина (10 символа)
        red_btn = Button(self, text="Red", width=10, command=lambda: self.set_color("red"))
        # Поставяме бутона на първия ред, втората колонка
        red_btn.grid(row=0, column=1) 
 
        # Създаваме останалите бутони по аналогичен начин
 
        green_btn = Button(self, text="Green", width=10, command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)
 
        blue_btn = Button(self, text="Blue", width=10, command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)
 
        black_btn = Button(self, text="Black", width=10, command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)
 
        white_btn = Button(self, text="White", width=10, command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=5)
 
        # Създаваме надпис за бутоните за промяна на размера на четката
        size_lab = Label(self, text="Size: ") 
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="2x", width=10, command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)
 
        two_btn = Button(self, text="5x", width=10, command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)
 
        five_btn = Button(self, text="7x", width=10, command=lambda: self.set_brush_size(7))
        five_btn.grid(row=1, column=3)
 
        seven_btn = Button(self, text="10x", width=10, command=lambda: self.set_brush_size(10))
        seven_btn.grid(row=1, column=4)
 
        ten_btn = Button(self, text="20x", width=10, command=lambda: self.set_brush_size(20))
        ten_btn.grid(row=1, column=5)
 
        twenty_btn = Button(self, text="50x", width=10, command=lambda: self.set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)

        clear_btn = Button(self, text="Clear", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

 
 
def main():
    root = Tk()
    root.geometry("800x600+300+300")
    app = Paint(root)
    root.mainloop()
 
if __name__ == "__main__":
    main()
