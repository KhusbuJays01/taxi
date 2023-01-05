from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image


class Driver(Tk):

    def __init__(self):
        super().__init__()
        self.title("Taxi Booking System")
        self.geometry('1350x1024')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()
        self.configure(background="#707FA6")


        # ------------------set frame---------------------------
        Frame_BookingDashboard = Frame(bg="#2A556C", width=1275, height=650)
        Frame_BookingDashboard.place(x=40, y=40)




        # --------------------Title----------------------------------
        head = Label(text="Driver-Dashboard ", bg="#2A556C", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=650, y=95)

        Frame_BookingDashboard = Label(bg="white", width=40, height=35)
        Frame_BookingDashboard.place(x=80, y=120)

        # ----------------------title 2nd-----------------------------
        Dashboardlbl = Label(text="Driver ", bg="White", font=("", 25, "bold"), fg="Green")
        Dashboardlbl.place(x=170, y=190)

        Dashboardlbl = Button(text="View assign ", bg="White", border=0, font=("", 15, "bold"), fg="Black")
        Dashboardlbl.place(x=170, y=300)

        Dashboardlbl = Button(text="LogOut ", bg="White", border=0, font=("", 15, "bold"), fg="red")
        Dashboardlbl.place(x=170, y=500)


        self.mainloop()
if __name__ == '__main__':
        login = Driver ()






