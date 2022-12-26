from tkinter import *
from tkinter import ttk


class AssignToDRiver(Tk):
    def __init__(self):
        super().__init__()
        self.title("Assign To Driver")
        self.geometry('1360x710')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()

        # set background color
        self.configure(background="#2A556C", width=900, height=550)
        self.geometry('990x660+50+50')


        # Title
        head = Label(text=" Assign To Driver", width=50, height=2, bg="Black", font=("", 25, "bold"),
                     fg="#FFFAFA")
        head.place(x=0, y=0)

        # -------------------name-----------------------
        customername = Label( text="Customer Name :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        customername.place(x=80, y=150)

        customername = Entry(width=25)
        customername.place(x=260, y=155)

        drivername = Label(text="Driver Name :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        drivername.place(x=450, y=150)

        drivername = Entry(width=25)
        drivername.place(x=600, y=155)

        btnassign = Button(text="Assigned",bg="green",font=("",15,"bold"),fg="white")
        btnassign.place(width=100,height=30,x=200,y=250)

        btnedit = Button(text="edit",bg="black", font=("",15, "bold"),fg="white")
        btnedit.place(width=100,height=30,x=350,y=250)

        btnclear = Button(text="Clear",bg="black",font=("",15,"bold"),fg="white")
        btnclear.place(width=100,height=30,x=500,y=250)

        btndelete = Button(text="Delete", bg="red", font=("", 15, "bold"), fg="white")
        btndelete.place(width=100, height=30, x=650, y=250)



        frame_AssignToDriver = Label(bg="white", width=65, height=22)
        frame_AssignToDriver.place(x=30, y=300)

        label_AssignToDriver = Label(bg="green", width=65, height=2)
        label_AssignToDriver.place(x=30, y=300)


        confirm = Label(label_AssignToDriver,text="Confirmed list", bg="green", font=("", 15, "bold"), fg="Black")
        confirm.place(x=150, y=5)

        frame_AssignToDriver = Label(bg="white", width=65, height=22)
        frame_AssignToDriver.place(x=510, y=300)

        label_AssignToDriver = Label(bg="red", width=65, height=2)
        label_AssignToDriver.place(x=510, y=300)

        unconfirm = Label(label_AssignToDriver, text="UnConfirm list", bg="red", font=("", 15, "bold"), fg="Black")
        unconfirm.place(x=150, y=5)




        self.mainloop()
if __name__ == '__main__':
        login = AssignToDRiver ()