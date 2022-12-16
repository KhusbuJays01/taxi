from tkinter import *
from tkinter import ttk


class AdminDashboard(Tk):

    def __init__(self):
        super().__init__()
        self.title("Driver dasboard")
        self.geometry('1350x1024')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()
        self.configure(background="#707FA6")

        # ------------------set frame---------------------------
        Frame_AdminDashboard = Frame(bg="#2A556C", width=1275, height=650)
        Frame_AdminDashboard.place(x=40, y=40)

        # --------------------Title----------------------------------
        head = Label(text="Admin Dashboard ", bg="#2A556C", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=650, y=95)

        label_AdminDashboard = Label(bg="white", width=40, height=35)
        label_AdminDashboard.place(x=80, y=120)

        # ----------------------title 2nd-----------------------------
        head1 = Label(text="Dashboard ", bg="White", font=("", 25, "bold"), fg="Green")
        head1.place(x=140, y=150)

        # -----------------button----------------------------
        lbl1 = Button(label_AdminDashboard, border=0, text="Customer", bg="white", font=("", 20), fg="Black")
        lbl1.place(x=50, y=130)

        lbl2 = Button(label_AdminDashboard, border=0, text="Taxi Driver", bg="white", font=("", 20), fg="Black")
        lbl2.place(x=50, y=180)

        lbl3 = Button(label_AdminDashboard, border=0, text="Assign to Driver", bg="white", font=("", 20), fg="Black")
        lbl3.place(x=50, y=230)

        lbl4 = Button(label_AdminDashboard, border=0, text="Payment", bg="white", font=("", 20), fg="Black")
        lbl4.place(x=50, y=280)

        lbl5 = Button(label_AdminDashboard, border=0, text="Log Out", bg="white", font=("", 20,"bold"), fg="Red")
        lbl5.place(x=50, y=430)

        label_AdminDashboard = Label(bg="white", width=35, height=10)
        label_AdminDashboard.place(x=420, y=170)

        lbl = Label(label_AdminDashboard, text="Total Rider ", bg="white", font=("", 20, "bold"), fg="#FB791B")
        lbl.place(x=50, y=40)

        label_AdminDashboard = Label(bg="white", width=35, height=10)
        label_AdminDashboard.place(x=705, y=170)

        lbl = Label(label_AdminDashboard, text="Total Customer ", bg="white", font=("", 20, "bold"), fg="Black")
        lbl.place(x=25, y=40)

        label_AdminDashboard = Label(bg="white", width=35, height=10)
        label_AdminDashboard.place(x=1000, y=170)

        lbl = Label(label_AdminDashboard, text="Available Rider ", bg="white", font=("", 20, "bold"), fg="#BB0D95")
        lbl.place(x=25, y=40)

        label_AdminDashboard = Label(bg="white", width=35, height=10)
        label_AdminDashboard.place(x=1000, y=360)



        label_AdminDashboard = Label(bg="white", width=35, height=10)
        label_AdminDashboard.place(x=705, y=360)

        label_AdminDashboard = Label(bg="white", width=35, height=10)
        label_AdminDashboard.place(x=420, y=360)

        label_AdminDashboard = Label(bg="white", width=35, height=8)
        label_AdminDashboard.place(x=420, y=550)

        label_AdminDashboard = Label(bg="white", width=35, height=8)
        label_AdminDashboard.place(x=700, y=550)

        label_AdminDashboard = Label(bg="white", width=35, height=8)
        label_AdminDashboard.place(x=1000, y=550)



        self.mainloop()
if __name__ == '__main__':
        login = AdminDashboard ()



