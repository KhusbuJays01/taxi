from tkinter import *
from tkinter import ttk
from Register import Register
from login1 import Login1
from PIL import ImageTk, Image


# -----------------------------GuI desiging-------------------------------
class Home (Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration")
        self.geometry('1360x700')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()

        # -----------------set image-------------------------
        image = Image.open("../image/khusbujais.png").resize((1360, 700))
        bgImage = ImageTk.PhotoImage(image)
        bgLabel = Label(self.frame, image=bgImage, width=1360, height=700, bg='black')
        bgLabel.pack()

        # -------------------head------------------------
        head = Label(text=" Wel-Come To Taxi Booking System",width=70,height=2, bg="Black", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=0, y=0)

        # -------------------login button-----------------
        button = Button(self, text="LogIn", bg="white", font=("", 15, "bold"), fg="Black")
        button.place(x=1120, y=20)
        button.bind("<Button-1>", self.open_login1)

        # -------------------sign up button----------------
        button1 = Button(self, text="Sign_Up", bg="white", font=("", 15, "bold"), fg="Black")
        button1.place(x=1240, y=20)
        button1.bind("<Button-1>", self.open_signup)

        self.mainloop()
    def open_signup(self, e):
        self.destroy()
        Register()


    def open_login1(self, e):
            self.destroy()
            Login1()

if __name__ == '__main__':
        login = Home()