from tkinter import *
from PIL import ImageTk, Image

class DriverDashboard (Tk):
    def __init__(self):
        super().__init__()
        self.title("DriverDashboard")
        self.resizable(False, False)
        self.frame = Frame(self)
        self.frame.pack()
        self.configure(background="#707FA6")
        self.geometry('990x660+50+50')

        # -------------------------set Frame-----------------------------------------
        Frame_Driver = Frame(bg="#2A556C", width=900, height=550)
        Frame_Driver.place(x=50, y=40)

        # ------------------------Title-------------------------------------------------
        head = Label(text="Driver Dashboard", bg="#2A556C", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=350, y=80)

        label_DriverDashboard = Label(bg="White", width=55, height=20)
        label_DriverDashboard.place(x=80, y=160)

        head = Label(text="New Trip List", bg="white", font=("", 25, "bold"), fg="Black")
        head.place(x=140, y=180)

        label_DriverDashboard = Label(bg="white", width=55, height=20)
        label_DriverDashboard.place(x=520, y=160)

        head = Label(text="Old Trip List", bg="white", font=("", 25, "bold"), fg="Black")
        head.place(x=600, y=180)

        lbl10 = Button(Frame_Driver, text="Complete Trip", bg="Green", font=("", 15, "bold"), fg="Black")
        lbl10.place(width=150, height=35, x=380, y=470)



        self.mainloop()
if __name__ == '__main__':
    login = DriverDashboard()



