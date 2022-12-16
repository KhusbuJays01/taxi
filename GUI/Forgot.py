from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

class Forgot (Tk):
    def __init__(self):
        super().__init__()
        self.title("Forgot Password")
        self.resizable(0, 0)
        self.geometry('400x580+50+50')
        self.config(bg='white')
        self.configure(background="#707FA6")
        self.frame = Frame(self)
        self.frame.pack()

        label_win = Frame(self, bg="#2A556C", width=370, height=520)
        label_win.place(x=15, y=30)

        lbl = Label(self, text="Forget Password System ",bg="#2A556C", font=("", 20, "bold"), fg="white")
        lbl.place(x=40, y=60)

        lbl1 = Label(self, text="User_Type", bg="#2A556C", font=("", 10, "bold"), fg="Black")
        lbl1.place(x=170, y=140)

        combo = ttk.Combobox(self, values=["Admin", "Customer", "Driver"])
        combo.place(x=140, y=165)

        lbl2 = Label(self, text="Email", bg="#2A556C", font=("", 10, "bold"), fg="Black")
        lbl2.place(x=170, y=220)

        ent1 = Entry(self)
        ent1.place(x=140, y=245)

        lbl2 = Label(self, text="new PAssword", bg="#2A556C", font=("", 10, "bold"), fg="Black")
        lbl2.place(x=160, y=290)

        ent1 = Entry(self)
        ent1.place(x=140, y=320)

        lbl2 = Label(self, text="Confirm PAssword", bg="#2A556C", font=("", 10, "bold"), fg="Black")
        lbl2.place(x=145, y=370)

        ent1 = Entry(self)
        ent1.place(x=140, y=400)

        lbl6 = Button(self, text="Update", bg="red", font=("", 15, "bold"), fg="Black")
        lbl6.place(width=70, height=25, x=170, y=470)


        self.mainloop()
if __name__ == '__main__':
        login = Forgot()