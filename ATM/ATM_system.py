from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image  
import tkinter.messagebox

class atm: 
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(110* blank_space + " ATM System")
        self.root.geometry("800x660+280+0")
        self.root.configure(background = 'gainsboro')

        MainFrame = Frame(self.root, bd =20, width = 784, height=700, relief= RIDGE)
        MainFrame.grid()
        
        TopFrame1 = Frame(MainFrame, bd =7, width = 734, height=300, relief= RIDGE)
        TopFrame1.grid(row=1, column=0, padx=12)
        TopFrame2 = Frame(MainFrame, bd =7, width = 734, height=300, relief= RIDGE)
        TopFrame2.grid(row=0, column=0, padx=12)

        TopFrame2Left = Frame(TopFrame2, bd =5, width = 190, height=300, relief= RIDGE)
        TopFrame2Left.grid(row=0, column=0, padx=3)

        TopFrame2Mid = Frame(TopFrame2, bd =5, width = 200, height=300, relief= RIDGE)
        TopFrame2Mid.grid(row=0, column=1, padx=3)

        TopFrame2Right = Frame(TopFrame2, bd =5, width = 190, height=300, relief= RIDGE)
        TopFrame2Right.grid(row=0, column=2, padx=3)

        # ---------------------------Widget-----------------------------
        self.txtReceipt = Text(TopFrame2Mid, height=17, width=42, bd=12, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0, column=0)

        self.img_arrow_Left = ImageTk.PhotoImage(Image.open("lArrow.png"))

        self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,
        image= self.img_arrow_Left).grid(row=0,column=0,padx=2, pady=2)
        self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,
        image= self.img_arrow_Left).grid(row=1,column=0,padx=2, pady=2)
        self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,
        image= self.img_arrow_Left).grid(row=2,column=0,padx=2, pady=2)
        self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,
        image= self.img_arrow_Left).grid(row=3,column=0,padx=2, pady=2)


        self.img_arrow_Right = ImageTk.PhotoImage(Image.open("rArrow.png"))
        
        self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,
        image= self.img_arrow_Right).grid(row=0,column=0,padx=2, pady=2)
        self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,
        image= self.img_arrow_Right).grid(row=1,column=0,padx=2, pady=2)
        self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,
        image= self.img_arrow_Right).grid(row=2,column=0,padx=2, pady=2)
        self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,
        image= self.img_arrow_Right).grid(row=3,column=0,padx=2, pady=2)

        self.img1 = ImageTk.PhotoImage(Image.open("one.png"))
        self.btn1 = Button(TopFrame1, width=160, height=60,
        image= self.img1).grid(row=2,column=0,padx=6, pady=4)

        self.img2 = ImageTk.PhotoImage(Image.open("two.png"))
        self.btn2 = Button(TopFrame1, width=160, height=60,
        image= self.img2).grid(row=2,column=1,padx=6, pady=4)

        self.img3 = ImageTk.PhotoImage(Image.open("three.png"))
        self.btn3 = Button(TopFrame1, width=160, height=60,
        image= self.img3).grid(row=2,column=2,padx=6, pady=4)

        self.imgcancel = ImageTk.PhotoImage(Image.open("cancel.png"))
        self.btncancel = Button(TopFrame1, width=160, height=60,
        image= self.imgcancel).grid(row=2,column=3,padx=6, pady=4)

        self.img4 = ImageTk.PhotoImage(Image.open("four.png"))
        self.btn4 = Button(TopFrame1, width=160, height=60,
        image= self.img4).grid(row=3,column=0,padx=6, pady=4)    

        self.img5 = ImageTk.PhotoImage(Image.open("five.png"))
        self.btn2 = Button(TopFrame1, width=160, height=60,
        image= self.img5).grid(row=3,column=1,padx=6, pady=4)

        self.img6 = ImageTk.PhotoImage(Image.open("six.png"))
        self.btn3 = Button(TopFrame1, width=160, height=60,
        image= self.img6).grid(row=3,column=2,padx=6, pady=4)

        self.imgclear = ImageTk.PhotoImage(Image.open("clear.png"))
        self.btnclear = Button(TopFrame1, width=160, height=60,
        image= self.imgclear).grid(row=3,column=3,padx=6, pady=4)

        self.img7 = ImageTk.PhotoImage(Image.open("seven.png"))
        self.btn4 = Button(TopFrame1, width=160, height=60,
        image= self.img7).grid(row=4,column=0,padx=6, pady=4)    

        self.img8 = ImageTk.PhotoImage(Image.open("eight.png"))
        self.btn2 = Button(TopFrame1, width=160, height=60,
        image= self.img8).grid(row=4,column=1,padx=6, pady=4)

        self.img9 = ImageTk.PhotoImage(Image.open("nine.png"))
        self.btn3 = Button(TopFrame1, width=160, height=60,
        image= self.img9).grid(row=4,column=2,padx=6, pady=4)

        self.imgenter = ImageTk.PhotoImage(Image.open("enter.png"))
        self.btnenter = Button(TopFrame1, width=160, height=60,
        image= self.imgenter).grid(row=4,column=3,padx=6, pady=4) 

        self.imgspace1 = ImageTk.PhotoImage(Image.open("empty.png"))
        self.btnspace1 = Button(TopFrame1, width=160, height=60,
        image= self.imgspace1).grid(row=5,column=0,padx=6, pady=4)    

        self.img0 = ImageTk.PhotoImage(Image.open("zero.png"))
        self.btn0 = Button(TopFrame1, width=160, height=60,
        image= self.img0).grid(row=5,column=1,padx=6, pady=4)

        self.imgspace2 = ImageTk.PhotoImage(Image.open("empty.png"))
        self.btnspace2 = Button(TopFrame1, width=160, height=60,
        image= self.imgspace2).grid(row=5,column=2,padx=6, pady=4)

        self.imgspace3 = ImageTk.PhotoImage(Image.open("empty.png"))
        self.btnspace3 = Button(TopFrame1, width=160, height=60,
        image= self.imgspace3).grid(row=5,column=3,padx=6, pady=4)   
if __name__ == '__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()
