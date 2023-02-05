from tkinter import *
 
class Paint(Frame):
    def __init__(self, parent):
         Frame.__init__(self, parent)
         self.parent = parent
 
 
def main():
    root = Tk()
    root.geometry("800x600+200+200")
    app = Paint(root)
    root.mainloop()
 
if __name__ == "__main__":
    main()
