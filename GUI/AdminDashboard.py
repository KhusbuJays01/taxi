from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image


class AdminDashboard(Tk):

    def __init__(self):
        super().__init__()
        self.title("Driver dasboard")
        self.geometry('1350x1024')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()
        # self.configure(background="#707FA6")


        # ------------------set frame---------------------------
        Frame_AdminDashboard = Frame(bg="#2A556C", width=1275, height=650)
        Frame_AdminDashboard.place(x=40, y=40)

        # --------------------Title----------------------------------
        head = Label(text="Admin Dashboard ", bg="#2A556C", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=650, y=95)

        Frame_AdminDashboard = Label(bg="white", width=40, height=35)
        Frame_AdminDashboard.place(x=80, y=120)

        image = Image.open("../image/admin1.jpg").resize((1360, 700))
        bgImage = ImageTk.PhotoImage(image)
        bgLabel = Label(self.frame, image=bgImage, width=1360, height=700, bg='black')
        bgLabel.pack()


        # ----------------------title 2nd-----------------------------
        head1 = Label(text="Admin ", bg="White", font=("", 25, "bold"), fg="Green")
        head1.place(x=155, y=150)

        # -----------------button----------------------------
        Manage = Button(Frame_AdminDashboard, border=0, text="Manage Customer", bg="white", font=("", 20), fg="Black")
        Manage.place(x=20, y=130)

        Add = Button(Frame_AdminDashboard, border=0, text="Add Taxi Driver", bg="white", font=("", 20), fg="Black")
        Add.place(x=20, y=215)

        Assign = Button(Frame_AdminDashboard, border=0, text="Assign to Driver", bg="white", font=("", 20), fg="Black")
        Assign.place(x=20, y=290)

        # lbl4 = Button(Frame_AdminDashboard, border=0, text="Payment", bg="white", font=("", 20), fg="Black")
        # lbl4.place(x=50, y=280)

        LogOut = Button(Frame_AdminDashboard, border=0, text="Log Out", bg="white", font=("", 20,"bold"), fg="Red")
        LogOut.place(x=50, y=430)

        self.mainloop()
if __name__ == '__main__':
        login = AdminDashboard ()



