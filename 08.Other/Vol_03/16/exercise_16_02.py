    def setUI(self):
        # Задаваме име на прозореца
        self.parent.title("Simple Paint")
        # Поставяме активни елементи върху родителския прозорец
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

        # Създаваме надпис за бутоните за промяна на цвета на четката
        color_lab = Label(self, text="Color: ")
        # Поставяме създадения надпис на първия ред в първата колона,
        # задаваме хоризонтален отстъп от 6 пиксела
        color_lab.grid(row=0, column=0, padx=6) 

        # Създаваме бутон: Задаване на текст и широчина (10 символа)
        red_btn = Button(self, text="Red", width=10)
        # Поставяме бутона на първия ред, втората колонка
        red_btn.grid(row=0, column=1) 
 
        # Създаваме останалите бутони по аналогичен начин
 
        green_btn = Button(self, text="Green", width=10)
        green_btn.grid(row=0, column=2)
 
        blue_btn = Button(self, text="Blue", width=10)
        blue_btn.grid(row=0, column=3)
 
        black_btn = Button(self, text="Black", width=10)
        black_btn.grid(row=0, column=4)
 
        white_btn = Button(self, text="White", width=10)
        white_btn.grid(row=0, column=5)
 
        # Създаваме надпис за бутоните за промяна на размера на четката
        size_lab = Label(self, text="Size: ") 
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="2x", width=10)
        one_btn.grid(row=1, column=1)
 
        two_btn = Button(self, text="5x", width=10)
        two_btn.grid(row=1, column=2)
 
        five_btn = Button(self, text="7x", width=10)
        five_btn.grid(row=1, column=3)
 
        seven_btn = Button(self, text="10x", width=10)
        seven_btn.grid(row=1, column=4)
 
        ten_btn = Button(self, text="20x", width=10)
        ten_btn.grid(row=1, column=5)
 
        twenty_btn = Button(self, text="50x", width=10)
        twenty_btn.grid(row=1, column=6, sticky=W)
