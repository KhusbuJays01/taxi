from tkinter import *
from tkinter import ttk


class Bill(Tk):
    def __init__(self):
        super().__init__()
        self.title("Bill")
        self.geometry('1360x710')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()

        # set background color
        self.configure(background="#2A556C", width=900, height=550)
        self.geometry('990x660+50+50')


        # Title
        head = Label(text=" Customer Bill", width=50, height=2, bg="Black", font=("", 25, "bold"),
                     fg="#FFFAFA")
        head.place(x=0, y=0)

        # -------------------name-----------------------
        customer_name = Label( text="Customer Name :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        customer_name.place(x=80, y=150)

        customer_name = Entry(width=25)
        customer_name.place(x=260, y=155)

        rate = Label(text="Rate :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        rate.place(x=80, y=200)

        rate = Entry(width=25)
        rate.place(x=260, y=200)

        vat = Label(text="VAT :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        vat.place(x=80, y=250)

        vat = Entry(width=25)
        vat.place(x=260, y=250)

        Kilometer = Label(text="Kilometer :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        Kilometer.place(x=80, y=300)

        kilometer = Entry(width=25)
        kilometer.place(x=260, y=305)

        btntotal = Button(text="Total",bg="green",font=("",15,"bold"),fg="white")
        btntotal.place(width=70,height=30,x=70,y=380)

        btnGenerate = Button(text="Generate",bg="black", font=("",15, "bold"),fg="white")
        btnGenerate.place(width=100,height=30,x=200,y=380)

        btnPrint = Button(text="Print",bg="black",font=("",15,"bold"),fg="white")
        btnPrint.place(width=100,height=30,x=350,y=380)

        btnedit = Button(text="Edit", bg="red", font=("", 15, "bold"), fg="white")
        btnedit.place(width=70, height=30, x=70, y=450)

        btnclear = Button(text="Clear", bg="red", font=("", 15, "bold"), fg="white")
        btnclear.place(width=100, height=30, x=200, y=450)

        btndelete = Button(text="Delete", bg="red", font=("", 15, "bold"), fg="white")
        btndelete.place(width=100, height=30, x=350, y=450)

        # -------------------------set frame-------------------------
        frame_Bill = Label(bg="white", width=65, height=35)
        frame_Bill.place(x=500, y=100)

        label_Bill = Label(bg="red", width=65, height=3)
        label_Bill.place(x=500, y=100)


        Bill = Label(label_Bill,text="Bill", bg="Red", font=("", 15, "bold"), fg="Black")
        Bill.place(x=200, y=6)






        self.mainloop()
if __name__ == '__main__':
        login = Bill ()