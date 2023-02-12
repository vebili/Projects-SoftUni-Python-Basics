class Snake(object):
    def __init__(self, segments):
        self.segments = segments
         
        # списък с допустимите посоки за движение на змията
        self.mapping = {"Down": (0, 1), "Up": (0, -1),
                                "Left": (-1, 0), "Right": (1, 0) }
        # изначално змията се движи надясно
        self.vector = self.mapping["Right"]
     
    def move(self):
         """ Движи змията назад """
          
         # обхождаме всички сегменти без първия
         for index in range(len(self.segments)-1):
              segment = self.segments[index].instance
              x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
              # задаваме на всеки сегмент позицията на сегмента,
  # стоящ след него
              c.coords(segment, x1, y1, x2, y2)
          
         # получаваме координатите на сегмента пред „главата“
         x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
          
         # поставяме „главата“ в посоката, указана във вектора на движение 
         c.coords(self.segments[-1].instance,
                       x1 + self.vector[0]*SEG_SIZE,
                       y1 + self.vector[1]*SEG_SIZE,
                       x2 + self.vector[0]*SEG_SIZE,
                       y2 + self.vector[1]*SEG_SIZE)
     
    def change_direction(self, event):
        """ Променя посоката на движение на змията """
 
        # event предава символа на натиснатия клавиш
        # и ако този клавиш е в допустимите посоки 
        # променяме посоката
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
 
    def add_segment(self):
        """ Добавя сегмент на змията """
 
        # определяме последния сегмент
        last_seg = c.coords(self.segments[0].instance)
         
        # определяме координатите къде да се постави следващият сегмент
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
         
        # добавяме още един сегмент към змията в задните координати
        self.segments.insert(0, Segment(x, y))
