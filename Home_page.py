from tkinter import *
from tkinter import ttk
from Register import Register
from login1 import Login1
from PIL import ImageTk, Image


class Home (Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration")
        self.geometry('1360x700')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()

        image = Image.open("khusbujais.png").resize((1360, 700))
        bgImage = ImageTk.PhotoImage(image)
        bgLabel = Label(self.frame, image=bgImage, width=1360, height=700, bg='black')
        bgLabel.pack()

        head = Label(text=" Wel-Come To Online Taxi Booking System",width=70,height=2, bg="Black", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=0, y=0)

        lbl5 = Button(self, text="LogIn", bg="white", font=("", 15, "bold"), fg="Black")
        lbl5.place(x=1120, y=20)
        lbl5.bind("<Button-1>", self.open_login1)

        lbl4 = Button(self, text="Sign_Up", bg="white", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=1240, y=20)
        lbl4.bind("<Button-1>", self.open_signup)


        self.mainloop()
    def open_signup(self, e):
        self.destroy()
        Register()


    def open_login1(self, e):
            self.destroy()
            Login1()

if __name__ == '__main__':
        login = Home()