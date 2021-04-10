from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image  
import tkinter.messagebox

class atm: 
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(110* blank_space + " ATM System")
        self.root.geometry("800x760+280+0")
        self.root.configure(background = 'gainsboro')

        MainFrame = Frame(self.root, bd =20, width = 784, height=700, relief= RIDGE)
        MainFrame.grid()
        
        TopFrame1 = Frame(MainFrame, bd =7, width = 734, height=300, relief= RIDGE)
        TopFrame1.grid(row=1, column=0, padx=12)
        TopFrame2 = Frame(MainFrame, bd =7, width = 734, height=300, relief= RIDGE)
        TopFrame2.grid(row=0, column=0, padx=12)

        TopFrame2Left = Frame(TopFrame2, bd =5, width = 190, height=300, relief= RIDGE)
        TopFrame2Left.grid(row=0, column=0, padx=8)

        TopFrame2Mid = Frame(TopFrame2, bd =5, width = 200, height=300, relief= RIDGE)
        TopFrame2Mid.grid(row=0, column=1, padx=8)

        TopFrame2Right = Frame(TopFrame2, bd =5, width = 190, height=300, relief= RIDGE)
        TopFrame2Right.grid(row=0, column=2, padx=8)

        # ---------------------------Widget-----------------------------
        self.txtReceipt = Text(TopFrame2Mid, height=17, width=42, bd=12, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0, column=0)

        self.img_arrow_Left = ImageTk.PhotoImage(Image.open("lArrow.png"))

        self.btnArrowL1 = Button(TopFrame2Left, width=100, height=60, state=NORMAL,
        image= self.img_arrow_Left).grid(row=0,column=0,padx=2, pady=2)
        self.btnArrowL2 = Button(TopFrame2Left, width=100, height=60, state=NORMAL,
        image= self.img_arrow_Left).grid(row=1,column=0,padx=2, pady=2)
        self.btnArrowL3 = Button(TopFrame2Left, width=100, height=60, state=NORMAL,
        image= self.img_arrow_Left).grid(row=2,column=0,padx=2, pady=2)
        self.btnArrowL4 = Button(TopFrame2Left, width=100, height=60, state=NORMAL,
        image= self.img_arrow_Left).grid(row=3,column=0,padx=2, pady=2)


        self.img_arrow_Right = ImageTk.PhotoImage(Image.open("rArrow.png"))
        
        self.btnArrowL1 = Button(TopFrame2Right, width=100, height=60, state=NORMAL,
        image= self.img_arrow_Right).grid(row=0,column=0,padx=2, pady=2)
        self.btnArrowL2 = Button(TopFrame2Right, width=100, height=60, state=NORMAL,
        image= self.img_arrow_Right).grid(row=1,column=0,padx=2, pady=2)
        self.btnArrowL3 = Button(TopFrame2Right, width=100, height=60, state=NORMAL,
        image= self.img_arrow_Right).grid(row=2,column=0,padx=2, pady=2)
        self.btnArrowL4 = Button(TopFrame2Right, width=100, height=60, state=NORMAL,
        image= self.img_arrow_Right).grid(row=3,column=0,padx=2, pady=2)



if __name__ == '__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()
