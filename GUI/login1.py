from tkinter import *
from tkinter import ttk, messagebox
from unittest import result
from PIL import ImageTk,Image
import booking
from Forgot import Forgot
from GUI.AdminDashboard import AdminDashboard
from GUI.makebooking import makebooking
# from GUI.Register import Register
from GUI import makebooking
from Middleware import login_middleware

# def Resister_page(label_win=None):
#     label_win.destroy()
#     import Register
    

# -------------------GUI-----------------------------
class Login1(Tk):
    # def submitact():
    #     user = self.Email.get()
    #     passw = Password.get()
    #
    #     print(f"The name entered by you is {user} {passw}")
    #
    #     logintodb(email, passw)
    #
    # def logintodb(user, passw):
    #     # If password is enetered by the
    #     # user
    #     if passw:
    #         db = mysql.connector.connect(host="localhost",
    #                                      user=user,
    #                                      password=passw,
    #                                      db="College")
    #         cursor = db.cursor()

    def __init__(self):
        super().__init__()
        self.title("login")
        self.resizable(0,0)
        self.geometry('990x660+50+50')
        self.frame = Frame(self)
        self.frame.pack();
        self.configure(background="#707FA6")
        self.wm_state("zoomed")

        # --------------------------image size-------------------------------
        self.image = Image.open('../image/car.jpg').resize((1500, 800))
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

        self.combo_usertype = ttk.Combobox(self.label_win, values=["Admin", "Customer", "Driver"])
        self.combo_usertype.place(x=90, y=130)

        Email = Label(self.label_win, text="Email", bg="white", font=("", 10, "bold"), fg="Black")
        Email.place(x=90, y=170)

        self.email_ent = Entry(self.label_win)
        self.email_ent.place(x=90, y=200)

        Password = Label(self.label_win, text="Password", bg="white", font=("", 10, "bold"), fg="Black")
        Password.place(x=90, y=250)

        self.pass_ent = Entry(self.label_win,show="*")
        self.pass_ent.place(x=90, y=300)

        # ------------------Hide password function---------------------------------
        def ShowPwd(event):
            password = self.pass_ent.get()
            self.pass_ent.config(show="", text=password)

        def HidePwd(event):
            self.pass_ent.config(show="*")

        cb_val = IntVar()
        lbl4 = Checkbutton(self.label_win, text="Show Password", variable=cb_val, onvalue=1, offvalue="0")
        lbl4.place(width=120, height=20, x=20, y=350)

        # -------------------------Button--------------------------------------
        lbl4.bind('<Button-1>', ShowPwd)
        lbl4.bind('<ButtonRelease-1>', HidePwd)
        # # lbl4.bind('<Button-1>',show_password)

        btn_fg = Button(self.label_win,border=0, text="Forget Password", bg="white", font=("", 10), fg="red")
        btn_fg.place(x=200, y=350)
        btn_fg.bind("<Button-1>",self.open_Forget)

        btn_login = Button(self.label_win, text="Login", bg="green", font=("", 15, "bold"), fg="Black",
                      command=self.log_db)
        btn_login.place(width=70, height=25, x=130, y=400)
        # btn_login.bind("<BUtton-1",self.open_makebooking())

        lbl7 = Label(self.label_win, text="Don't have an account?", bg="white", font=("", 10), fg="black")
        lbl7.place(x=20, y=500)

        lblor = Label(self.label_win, text="------------------------------OR-----------------------------", bg="white", font=("", 10, "bold"), fg="black")
        lblor.place(x=40, y=460)

        Sign_Up = Button(self.label_win, border=0, text="Sign Up", bg="white", font=("", 10), fg="red")
        Sign_Up.place(x=200, y=500)
        # command = lambda *a: self.open_Register()

        # ----------------method------------------------------

        self.mainloop()


    def open_Forget(self, e):
        self.label_win.destroy()
        Forgot()

    def open_makebooking(self):
        self.log_db()
        makebooking.makebooking()

    def log_db(self):
        login_md = login_middleware.Login_middleware()
        login_md.set_login_usertype = self.combo_usertype.get()
        login_md.set_login_email = self.email_ent.get()
        login_md.set_login_pass = self.pass_ent.get()
        values = login_md.login_database()
        #
        # if result:
        #     self.login_makebooking()

        try:
            if len(values) > 0:
                # print(values)
                login_md.set_login_id = values[0]
                login_md.set_login_email = values[1]
                login_md.set_login_pass = values[2]
                messagebox.showinfo('Success', f'Successfully login as a {login_md.get_login_usertype}.')
                self.destroy()
                makebooking.makebooking()


        except TypeError:
            messagebox.showerror('Error', 'Incorrect email and password !!')

            # if object.get_login_usertype == "Customer":
            #     self.destroy()
            #     makebooking.makebooking()
            #     # self.open_makebooking()

                # makebooking.makebooking(object.)

            # elif object.get_usertype == "Admin":
            #     self.login1.destroy()
            #     AdminDashboard.AdminDashboard(object.get_userid)

            # elif object.get_usertype == "Driver":
            #     self.login.destroy()
            #     booking.Booking(object.get_userid)

if __name__ == '__main__':
    login = Login1()