from tkinter import *
from tkinter import ttk


class Driver(Tk):
    def __init__(self):
        super().__init__()
        self.title("Driver dasboard")
        self.geometry('1360x710')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()

        # set background color
        self.configure(background="#707FA6")
        self.geometry('990x660+50+50')

        # next  window
        label_Driver = Label(bg="#2A556C", width=123, height=37)
        label_Driver.place(x=50, y=50)

        # Title
        head = Label(text="Driver Register", bg="#2A556C", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=350, y=80)

        lbl1 = Label(label_Driver, text="Full name :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl1.place(x=200, y=100)

        ent2 = Entry(label_Driver, width=50)
        ent2.place(x=390, y=110)

        lbl3 = Label(label_Driver, text="Email :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl3.place(x=200, y=150)

        ent3 = Entry(label_Driver, width=50)
        ent3.place(x=390, y=150)

        lbl4 = Label(label_Driver, text="Address :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=200, y=200)

        ent4 = Entry(label_Driver, width=50)
        ent4.place(x=390, y=200)

        lbl5 = Label(label_Driver, text="Phone number :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl5.place(x=200, y=250)

        ent5 = Entry(label_Driver, width=50)
        ent5.place(x=390, y=250)

        lbl6 = Label(label_Driver, text="Gender :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl6.place(x=200, y=300)

        ent6 = Entry(label_Driver, width=50)
        ent6.place(x=390, y=300)

        lbl7 = Label(label_Driver, text="Password :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl7.place(x=200, y=350)

        ent7 = Entry(label_Driver, width=50)
        ent7.place(x=390, y=350)

        lbl8 = Label(label_Driver, text="Licences :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl8.place(x=200, y=400)

        ent9 = Entry(label_Driver, width=50)
        ent9.place(x=390, y=400)

        lbl10 = Button(label_Driver, text="Back", bg="black", font=("", 15, "bold"), fg="white")
        lbl10.place(width=150, height=30, x=250, y=500)

        lbl10 = Button(label_Driver, text="Create", bg="#ED5843", font=("", 15, "bold"), fg="Black")
        lbl10.place(width=150, height=30, x=500, y=500)






        self.mainloop()
if __name__ == '__main__':
        login = Driver ()