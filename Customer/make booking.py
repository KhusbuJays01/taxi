from tkinter import *
from tkinter import ttk


class makebooking(Tk):
    def __init__(self):
        super().__init__()
        self.title("Make Bookinng")
        self.geometry('1360x710')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()

        # set background color
        self.configure(background="#707FA6")
        self.geometry('990x660+50+50')

        # next  window
        label_makebooking = Label(bg="#2A556C", width=123, height=37)
        label_makebooking.place(x=50, y=50)

        # Title
        head = Label(text="Make Booking", bg="#2A556C", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=350, y=80)

        lbl1 = Label(label_makebooking, text="PickUp_Address :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl1.place(x=200, y=100)

        ent2 = Entry(label_makebooking, width=50)
        ent2.place(x=390, y=110)

        lbl3 = Label(label_makebooking, text="PickUp_Time :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl3.place(x=200, y=170)

        ent3 = Entry(label_makebooking, width=50)
        ent3.place(x=390, y=180)

        lbl4 = Label(label_makebooking, text="PickUp_Date :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=200, y=250)

        ent4 = Entry(label_makebooking, width=50)
        ent4.place(x=390, y=250)

        lbl4 = Button(label_makebooking, text="Confirm", bg="Green", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=170, y=300, width=90)

        lbl4 = Button(label_makebooking, text="Edit", bg="gray", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=300, y=300, width=90)

        lbl4 = Button(label_makebooking, text="Clear", bg="blue", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=430, y=300, width=90)

        lbl4 = Button(label_makebooking, text="View", bg="orange", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=560, y=300, width=90)

        lbl4 = Button(label_makebooking, text="Delete", bg="red", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=690, y=300, width=90)

        label_makebooking = Label(bg="white", width=115, height=12)
        label_makebooking.place(x=80, y=410)





        self.mainloop()
if __name__ == '__main__':
        login = makebooking ()