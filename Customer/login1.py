from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from Forgot import Forgot



# -------------------GUI-----------------------------
class Login1(Tk):

    def __init__(self):
        super().__init__()
        self.title("login")
        self.resizable(0,0)
        self.geometry('990x660+50+50')
        self.frame = Frame(self)
        self.frame.pack();
        self.configure(background="#707FA6")
        self.wm_state("zoomed")
        #
        # # ------------------variable----------------------
        # self.log.id = IntVar()
        # self.log.User_Type.StringVar()
        # self.Log.User_Name.StringVar()
        # self.log.Password.StringVar()

        # --------------------------image size-------------------------------
        self.image = Image.open('image/car.jpg').resize((1500, 800))
        self.bgImage=ImageTk.PhotoImage(self.image)

        bgLabel=Label(self.frame, image=self.bgImage)
        bgLabel.pack()

        # -------------------------------------set head------------------------
        head = Label(text="Online Taxi  Booking  System", bg="black", font=("", 25, "bold"),fg="#FFFAFA")
        head.place(x=-5, y=-5,height=60, width=1500)

        # --------------------------------------next Frame---------------------
        self.label_win = Frame(bgLabel, bg="white", width=360, height=1000)
        self.label_win.place(x=0, y=150)

        # ------------------------ set the title of login and username---------------------
        lbl = Label(self.label_win, text="Login System ", bg="white", font=("", 20, "bold"), fg="Black")
        lbl.place(x=90, y=30)

        lbl1 = Label(self.label_win, text="User_Type", bg="white", font=("", 10, "bold"), fg="Black")
        lbl1.place(x=120, y=100)

        self.combo = ttk.Combobox(self.label_win, values=["Admin", "Customer", "Driver"])
        self.combo.place(x=90, y=130)

        lbl2 = Label(self.label_win, text="User_Name", bg="white", font=("", 10, "bold"), fg="Black")
        lbl2.place(x=90, y=170)

        self.ent1 = Entry(self.label_win)
        self.ent1.place(x=90, y=200)

        lbl3 = Label(self.label_win, text="Password", bg="white", font=("", 10, "bold"), fg="Black")
        lbl3.place(x=90, y=250)

        self.ent2 = Entry(self.label_win,show="*")
        self.ent2.place(x=90, y=300)

        # ------------------Hide password function---------------------------------
        def ShowPwd(event):
            password = self.ent2.get()
            self.ent2.config(show="", text=password)

        def HidePwd(event):
            self.ent2.config(show="*")

        cb_val = IntVar()
        lbl4 = Checkbutton(self.label_win, text="Show Password", variable=cb_val, onvalue=1, offvalue="0")
        lbl4.place(width=120, height=20, x=20, y=350)

        # -------------------------Button--------------------------------------
        lbl4.bind('<Button-1>', ShowPwd)
        lbl4.bind('<ButtonRelease-1>', HidePwd)
        # # lbl4.bind('<Button-1>',show_password)

        lbl5 = Button(self.label_win,border=0, text="Forget Password", bg="white", font=("", 10), fg="red")
        lbl5.place(x=200, y=350)
        lbl5.bind("<Button-1>",self.open_Forget)

        lbl6 = Button(self.label_win, text="Login", bg="green", font=("", 15, "bold"), fg="Black",
                      command=self.log_db)

        lbl6.place(width=70, height=25, x=130, y=400)

        lbl7 = Label(self.label_win, text="Don't have an account?", bg="white", font=("", 10), fg="black")
        lbl7.place(x=20, y=500)

        lbl8 = Label(self.label_win, text="------------------------------OR-----------------------------", bg="white", font=("", 10, "bold"), fg="black")
        lbl8.place(x=40, y=460)

        lbl9 = Button(self.label_win, border=0, text="Sign Up", bg="white", font=("", 10), fg="red")
        lbl9.place(x=200, y=500)


        # end nex window

        # -----------------------validation------------------------



        # ----------------method------------------------------

        self.mainloop()
    def open_Forget(self, e):
        self.label_win.destroy()
        Forgot()

    def log_db(self):
        User_Name=self.ent1.get()
        Password=self.ent2.get()


if __name__ == '__main__':
    login = Login1()

