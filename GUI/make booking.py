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
        Frame_makebooking = Frame(bg="#2A556C", width=900, height=550)
        Frame_makebooking.place(x=50, y=40)

        # # Title
        head = Label(text="Make Booking", bg="#2A556C", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=370, y=80)

        #------------------------------- sencond head--------------------
        head = Label(text="Pick Up--------------------------", bg="#2A556C", font=("", 20, "bold"), fg="#FFFAFA")
        head.place(x=100, y=150)

        lbl1 = Label(Frame_makebooking, text="Address :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        lbl1.place(x=50, y=170)

        ent2 = Entry(Frame_makebooking, width=35)
        ent2.place(x=153, y=175)

        lbl3 = Label(Frame_makebooking, text="Time :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        lbl3.place(x=50, y=220)

        ent3 = Entry(Frame_makebooking, width=35)
        ent3.place(x=153, y=225)

        lbl4 = Label(Frame_makebooking, text="Date :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        lbl4.place(x=50, y=255)

        ent4 = Entry(Frame_makebooking, width=35)
        ent4.place(x=153, y=265)

        head = Label(text="Drop-------------------------------", bg="#2A556C", font=("", 20, "bold"), fg="#FFFAFA")
        head.place(x=540, y=150)

        lbl5 = Label(Frame_makebooking, text="Address :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        lbl5.place(x=490, y=170)

        ent5 = Entry(Frame_makebooking, width=35)
        ent5.place(x=600, y=175)

        lbl6 = Label(Frame_makebooking, text="Time :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        lbl6.place(x=490, y=220)

        ent6 = Entry(Frame_makebooking, width=35)
        ent6.place(x=600, y=225)

        lbl7 = Label(Frame_makebooking, text="Date :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        lbl7.place(x=490, y=255)

        ent7 = Entry(Frame_makebooking, width=35)
        ent7.place(x=600, y=265)

        lbl4 = Button(Frame_makebooking, text="Confirm", bg="Green", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=90, y=300, width=90)

        lbl4 = Button(Frame_makebooking, text="Edit", bg="gray", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=250, y=300, width=90)

        lbl4 = Button(Frame_makebooking, text="Clear", bg="blue", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=400, y=300, width=90)

        lbl4 = Button(Frame_makebooking, text="View", bg="orange", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=550, y=300, width=90)

        lbl4 = Button(Frame_makebooking, text="Delete", bg="red", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=700, y=300, width=90)

        label_makebooking = Label(bg="white", width=120, height=12)
        label_makebooking.place(x=80, y=390)


        self.mainloop()
if __name__ == '__main__':
        login = makebooking ()

