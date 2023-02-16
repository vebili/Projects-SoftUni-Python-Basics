from tkinter import *
import random

# Някои глобални променливи
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True
apples = 0


# Спомагателни функции
def create_block():
    """ Създава храна за змията - ябълка """
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)
    BLOCK = c.create_oval(posx, posy,
                          posx+SEG_SIZE, posy+SEG_SIZE,
                          fill="red")


def main():
    """ Управлява игровия процес """
    global IN_GAME
    global apples
    if IN_GAME:
        s.move()
        # Определяме координатите на главата
        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords
        # Сблъсък с краищата на игралното поле
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        # Изяждане на ябълка
        elif head_coords == c.coords(BLOCK):
            s.add_segment()
            apples += 1
            c.delete(BLOCK)
            create_block()
        # Змията се ухапва 
        else:
            for index in range(len(s.segments)-1):
                if head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False
        root.after(100, main)
    # Не IN_GAME -> извеждаме съобщение
    else:
        t = "Game over!\nScore: " + str(apples)
        c.create_text(WIDTH/2, HEIGHT/2,
                      text=t,
                      font="Arial 20",
                      fill="red")


class Segment(object):
    """ Сегмент на змията """
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x+SEG_SIZE, y+SEG_SIZE,
                                           fill="green")


class Snake(object):
    """ Клас на змията """
    def __init__(self, segments):
        self.segments = segments
        # Възможни посоки за движение
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # Начална посока
        self.vector = self.mapping["Down"]

    def move(self):
        """ Движи змията в задна посока """
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)

    def add_segment(self):
        """ Добавя сегмент на змията """
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        """ Променя посоката на движение на змията """
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

# Настройка на прозореца
root = Tk()
root.title("Anaconda")

#c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#005500")
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#ffffff")
c.grid()
# установяване на фокус
c.focus_set()
# създаваме сегментите и змията
segments = [Segment(SEG_SIZE, SEG_SIZE),
            Segment(SEG_SIZE*2, SEG_SIZE),
            Segment(SEG_SIZE*3, SEG_SIZE)]
s = Snake(segments)
# Реагираме на натискане на клавиш
c.bind("<KeyPress>", s.change_direction)

# Поставяме първата ябълка в полето
create_block()
# Стартираме играта
main()
root.mainloop()
