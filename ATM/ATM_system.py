from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image  
import tkinter.messagebox
import HandDetect
import threading

class atm: 
    def __init__(self, root):
        balance = 0
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
        
        def enter_Pin():
            pinNo=self.txtReceipt.get("1.0", "end-1c")
            if(pinNo == str("1234")):
                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.insert(END, '\t\t ATM' + "\n\n\n")
                self.txtReceipt.insert(END, 'Withdraw Cash \t\t\t Loan' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Cash with Receipt \t\t\t Deposit ' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Balance \t\t\t Request New Pin' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Mini Statement \t\t\t Print Statement' + "\n\n\n\n")

                self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=loan,
                image= self.img_arrow_Right).grid(row=0,column=0,padx=2, pady=2)
                self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=deposit,
                image= self.img_arrow_Right).grid(row=1,column=0,padx=2, pady=2)
                self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=request_new_pin,
                image= self.img_arrow_Right).grid(row=2,column=0,padx=2, pady=2)
                self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=statement,
                image= self.img_arrow_Right).grid(row=3,column=0,padx=2, pady=2)


                self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=NORMAL,command=withdrawcash,
                image= self.img_arrow_Left).grid(row=0,column=0,padx=2, pady=2)
                self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=NORMAL,command=withdrawcash,
                image= self.img_arrow_Left).grid(row=1,column=0,padx=2, pady=2)
                self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=NORMAL,command=balance,
                image= self.img_arrow_Left).grid(row=2,column=0,padx=2, pady=2)
                self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=NORMAL,command=statement,
                image= self.img_arrow_Left).grid(row=3,column=0,padx=2, pady=2)
            else:
                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.insert(END, 'Invalid Pin Number' + "\n\n")
    ############################################################################################################
        def enter():
                self.txtReceipt.delete("1.0", END)
                self.txtReceipt.insert(END, '\t\t ATM' + "\n\n\n")
                self.txtReceipt.insert(END, 'Withdraw Cash \t\t\t Loan' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Cash with Receipt \t\t\t Deposit ' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Balance \t\t\t Request New Pin' + "\n\n\n\n")
                self.txtReceipt.insert(END, 'Mini Statement \t\t\t Print Statement' + "\n\n\n\n")

                self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=loan,
                image= self.img_arrow_Right).grid(row=0,column=0,padx=2, pady=2)
                self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=deposit,
                image= self.img_arrow_Right).grid(row=1,column=0,padx=2, pady=2)
                self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=request_new_pin,
                image= self.img_arrow_Right).grid(row=2,column=0,padx=2, pady=2)
                self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=NORMAL,command=statement,
                image= self.img_arrow_Right).grid(row=3,column=0,padx=2, pady=2)


                self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=NORMAL,command=withdrawcash,
                image= self.img_arrow_Left).grid(row=0,column=0,padx=2, pady=2)
                self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=NORMAL,command=withdrawcash,
                image= self.img_arrow_Left).grid(row=1,column=0,padx=2, pady=2)
                self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=NORMAL,command=balance,
                image= self.img_arrow_Left).grid(row=2,column=0,padx=2, pady=2)
                self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=NORMAL,command=statement,
                image= self.img_arrow_Left).grid(row=3,column=0,padx=2, pady=2)
            
        def clear():
            self.txtReceipt.delete("1.0", END)

            self.txtReceipt = Text(TopFrame2Mid, height=17, width=42, bd=12, font=('arial', 9, 'bold'))
            self.txtReceipt.grid(row=0, column=0)

            self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,
            image= self.img_arrow_Left).grid(row=0,column=0,padx=2, pady=2)
            self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,
            image= self.img_arrow_Left).grid(row=1,column=0,padx=2, pady=2)
            self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,
            image= self.img_arrow_Left).grid(row=2,column=0,padx=2, pady=2)
            self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,
            image= self.img_arrow_Left).grid(row=3,column=0,padx=2, pady=2)

            self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,
            image= self.img_arrow_Right).grid(row=0,column=0,padx=2, pady=2)
            self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,
            image= self.img_arrow_Right).grid(row=1,column=0,padx=2, pady=2)
            self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,
            image= self.img_arrow_Right).grid(row=2,column=0,padx=2, pady=2)
            self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,
            image= self.img_arrow_Right).grid(row=3,column=0,padx=2, pady=2)

        def insert0():
            value0 = 0
            self.txtReceipt.insert(END, value0)

        def insert1():
            value1 = 1
            self.txtReceipt.insert(END, value1)

        def insert2():
            value2 = 2
            self.txtReceipt.insert(END, value2)

        def insert3():
            value3 = 3
            self.txtReceipt.insert(END, value3)

        def insert4():
            value4 = 4
            self.txtReceipt.insert(END, value4)

        def insert5():
            value5 = 5
            self.txtReceipt.insert(END, value5)

        def insert6():
            value6 = 6
            self.txtReceipt.insert(END, value6)
        
        def insert7():
            value7 = 7
            self.txtReceipt.insert(END, value7)

        def insert8():
            value8 = 8
            self.txtReceipt.insert(END, value8)

        def insert9():
            value9 = 9
            self.txtReceipt.insert(END, value9)
        def cancel():
            Cancel = tkinter.messagebox.askyesno("ATM", "Confirm if you want to cancel")
            if Cancel>0:
                self.root.destroy()
                return
        def withdrawcash(): 
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END , "Withdraw amount: ")
            # self.txtReceipt.delete("1.0", END)
            self.txtReceipt.focus_set()
        def loan(): 
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, 'Loan $')
            self.txtReceipt.focus_set()
        def deposit(): 
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END , "Enter amount to be deposited: \n")
            self.txtReceipt.focus_set()
        def request_new_pin():
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END , "Enter new Pin: ")
        def balance():
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, "Balance is 10000763\n\n")
        def statement():
            enter_Pin()
            self.txtReceipt.delete("1.0", END)
            self.txtReceipt.insert(END, "Balance is 10000763\n\n")

            # ---------------------------Widget-----------------------------
        self.txtReceipt = Text(TopFrame2Mid, height=17, width=42, bd=12, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0, column=0)

        self.img_arrow_Left = ImageTk.PhotoImage(Image.open("lArrow.png"))

        self.btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command = withdrawcash,
        image= self.img_arrow_Left).grid(row=0,column=0,padx=2, pady=2)
        self.btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,command=withdrawcash,
        image= self.img_arrow_Left).grid(row=1,column=0,padx=2, pady=2)
        self.btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,command = balance,
        image= self.img_arrow_Left).grid(row=2,column=0,padx=2, pady=2)
        self.btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=DISABLED,command=statement,
        image= self.img_arrow_Left).grid(row=3,column=0,padx=2, pady=2)

    #####################################################################################################################
        self.img_arrow_Right = ImageTk.PhotoImage(Image.open("rArrow.png"))
        
        self.btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command = loan,
        image= self.img_arrow_Right).grid(row=0,column=0,padx=2, pady=2)
        self.btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,command=deposit,
        image= self.img_arrow_Right).grid(row=1,column=0,padx=2, pady=2)
        self.btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,command=request_new_pin,
        image= self.img_arrow_Right).grid(row=2,column=0,padx=2, pady=2)
        self.btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=DISABLED,command=statement,
        image= self.img_arrow_Right).grid(row=3,column=0,padx=2, pady=2)

        self.img1 = ImageTk.PhotoImage(Image.open("one.png"))
        self.btn1 = Button(TopFrame1, width=160, height=60, command=insert1,
        image= self.img1).grid(row=2,column=0,padx=6, pady=4)

        self.img2 = ImageTk.PhotoImage(Image.open("two.png"))
        self.btn2 = Button(TopFrame1, width=160, height=60, command=insert2,
        image= self.img2).grid(row=2,column=1,padx=6, pady=4)

        self.img3 = ImageTk.PhotoImage(Image.open("three.png"))
        self.btn3 = Button(TopFrame1, width=160, height=60,command=insert3,
        image= self.img3).grid(row=2,column=2,padx=6, pady=4)

        self.imgcancel = ImageTk.PhotoImage(Image.open("cancel.png"))
        self.btncancel = Button(TopFrame1, width=160, height=60,command=cancel,
        image= self.imgcancel).grid(row=2,column=3,padx=6, pady=4)
    #############################################################################
        self.img4 = ImageTk.PhotoImage(Image.open("four.png"))
        self.btn4 = Button(TopFrame1, width=160, height=60,command=insert4,
        image= self.img4).grid(row=3,column=0,padx=6, pady=4)    

        self.img5 = ImageTk.PhotoImage(Image.open("five.png"))
        self.btn2 = Button(TopFrame1, width=160, height=60,command=insert5,
        image= self.img5).grid(row=3,column=1,padx=6, pady=4)

        self.img6 = ImageTk.PhotoImage(Image.open("six.png"))
        self.btn3 = Button(TopFrame1, width=160, height=60,command=insert6,
        image= self.img6).grid(row=3,column=2,padx=6, pady=4)

        self.imgclear = ImageTk.PhotoImage(Image.open("clear.png"))
        self.btnclear = Button(TopFrame1, width=160, height=60, command=clear,
        image= self.imgclear).grid(row=3,column=3,padx=6, pady=4)

        self.img7 = ImageTk.PhotoImage(Image.open("seven.png"))
        self.btn4 = Button(TopFrame1, width=160, height=60,command=insert7,
        image= self.img7).grid(row=4,column=0,padx=6, pady=4)    

        self.img8 = ImageTk.PhotoImage(Image.open("eight.png"))
        self.btn2 = Button(TopFrame1, width=160, height=60,command=insert8,
        image= self.img8).grid(row=4,column=1,padx=6, pady=4)

        self.img9 = ImageTk.PhotoImage(Image.open("nine.png"))
        self.btn3 = Button(TopFrame1, width=160, height=60,command=insert9,
        image= self.img9).grid(row=4,column=2,padx=6, pady=4)

        self.imgenter = ImageTk.PhotoImage(Image.open("enter.png"))
        self.btnenter = Button(TopFrame1, width=160, height=60, command=enter,
        image= self.imgenter).grid(row=4,column=3,padx=6, pady=4) 

        self.imgspace1 = ImageTk.PhotoImage(Image.open("empty.png"))
        self.btnspace1 = Button(TopFrame1, width=160, height=60,
        image= self.imgspace1).grid(row=5,column=0,padx=6, pady=4)    

        self.img0 = ImageTk.PhotoImage(Image.open("zero.png"))
        self.btn0 = Button(TopFrame1, width=160, height=60, command=insert0,
        image= self.img0).grid(row=5,column=1,padx=6, pady=4)

        self.imgspace2 = ImageTk.PhotoImage(Image.open("empty.png"))
        self.btnspace2 = Button(TopFrame1, width=160, height=60,
        image= self.imgspace2).grid(row=5,column=2,padx=6, pady=4)

        self.imgspace3 = ImageTk.PhotoImage(Image.open("empty.png"))
        self.btnspace3 = Button(TopFrame1, width=160, height=60,
        image= self.imgspace3).grid(row=5,column=3,padx=6, pady=4)   
        

def ATM():
    root = Tk()
    application = atm(root)
    root.mainloop()


if __name__ == '__main__':
    p1 = threading.Thread(target=ATM)
    p2 = threading.Thread(target=HandDetect.detector)
    p1.start()
    p2.start()