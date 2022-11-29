from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

class Forgot (Tk):
    def __init__(self):
        super().__init__()
        self.title("Forgot Password")
        self.resizable(0, 0)
        self.geometry('400x540+50+50')
        self.config(bg='white')
        self.frame = Frame(self)
        self.frame.pack()

        label_win = Frame(self, bg="white", width=400, height=400)
        label_win.place(x=0, y=150)

        lbl = Label(self, text="Forgot Password System ",bg="white", font=("", 20, "bold"), fg="#AF1515")
        lbl.place(x=40, y=20)

        lbl1 = Label(self, text="User_Type", bg="white", font=("", 10, "bold"), fg="Black")
        lbl1.place(x=140, y=100)

        combo = ttk.Combobox(self, values=["Admin", "Customer", "Driver"])
        combo.place(x=100, y=140)

        lbl2 = Label(self, text="Email", bg="white", font=("", 10, "bold"), fg="Black")
        lbl2.place(x=100, y=190)

        ent1 = Entry(self)
        ent1.place(x=100, y=230)

        lbl2 = Label(self, text="new PAssword", bg="white", font=("", 10, "bold"), fg="Black")
        lbl2.place(x=100, y=290)

        ent1 = Entry(self)
        ent1.place(x=100, y=330)

        lbl2 = Label(self, text="Confirm PAssword", bg="white", font=("", 10, "bold"), fg="Black")
        lbl2.place(x=100, y=390)

        ent1 = Entry(self)
        ent1.place(x=100, y=430)

        lbl6 = Button(self, text="Update", bg="red", font=("", 15, "bold"), fg="Black")
        lbl6.place(width=70, height=25, x=130, y=490)


        self.mainloop()
if __name__ == '__main__':
        login = Forgot()