import re
from tkinter import *
from tkinter import ttk, messagebox

import mysql.connector
from login1 import Login1
from Middleware import Register_middleware

# ----------------------------GuI design----------------------------
class Register(Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration")
        self.geometry('1360x710')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()
        # self.wm_state("zoomed")

# -----------------------variable-------------------
        self.reg_id = IntVar()
        self.reg_User_Type = StringVar()
        self.reg_Name = StringVar()
        self.reg_Address = StringVar()
        # self.reg_Licesnse = StringVar()
        self.reg_Email = StringVar()
        self.reg_Telephone_No = StringVar()
        self.reg_Gender = StringVar()
        self.reg_Password = StringVar()

# -----------------------set background color---------------------
        self.configure(background="#707FA6")
        self.geometry('990x660+50+50')

# ----------------------------next  window------------------------
        Frame_Register = Frame(bg="#2A556C", width=900, height=550)
        Frame_Register.place(x=50, y=40)

# ------------------------------Title----------------------
        head = Label(text="Registration System", bg="#2A556C", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=300, y=50)


        # -----------------set label--------------------------------------
        # lbl1 = Label(Frame_Register, text="User_Type:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        # lbl1.place(x=200, y=100)


        Full_Name = Label(Frame_Register, text="Full_Name:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        Full_Name.place(x=200, y=150)

        Email = Label(Frame_Register, text="Email:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        Email.place(x=200, y=200)

        Address = Label(Frame_Register, text="Address:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        Address.place(x=200, y=250)

        Phone_No = Label(Frame_Register, text="Phone_No.:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        Phone_No.place(x=200, y=300)

        Gender = Label(Frame_Register, text="Gender:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        Gender.place(x=200, y=350)

        Password = Label(Frame_Register, text="Password:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        Password.place(x=200, y=400)


        # ---------------combo box------------------------------
        # self.combo = ttk.Combobox(Frame_Register, textvariable=self.reg_User_Type, values=["Admin", "Customer", "Driver"])
        # self.combo.place(width=300, x=350, y=110)
        # self. combo.bind("<<ComboboxSelected>>", self.open_Driver)


        # -----------------------entry set-------------------------------

        self.reg_Name = Entry(Frame_Register, textvariable=self.reg_Name, width=50)
        self.reg_Name.place(x=350, y=150)


        self.reg_Email = Entry(Frame_Register, textvariable=self.reg_Email, width=50)
        self.reg_Email.place(x=350, y=200)


        self.reg_Address = Entry(Frame_Register, textvariable=self.reg_Address, width=50)
        self.reg_Address.place(x=350, y=250)



        self.reg_Telephone_No = Entry(Frame_Register, textvariable=self.reg_Telephone_No, width=50)
        self.reg_Telephone_No.place(x=350, y=300)



        self.combo = ttk.Combobox(Frame_Register, textvariable=self.reg_Gender, values=["Male", "Female", "Other"])
        self.combo.place(width=300, x=350, y=350)



        self.reg_Password = Entry(Frame_Register, textvariable=self.reg_Password, width=50)
        self.reg_Password.place(x=350, y=400)

        # lbl11 = Label(label_Resister, text="license:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        # lbl11.place(x=200, y=450)
        #
        # self.ent11 = Entry(label_Resister, textvariable=self.reg_Licesnse, width=50)
        # self.ent11.place(x=350, y=450)



        # lbl11 = Button(label_Resister, text="Back to home", bg="#ED5843", font=("", 15, "bold"), fg="Black")
        # lbl11.place(width=200, height=30, x=500, y=500)

        # ---------------------set text------------------------------
        lbl9 = Label(Frame_Register,text="Already have an account!!", bg="#2A556C", font=("", 10, "bold"),
                     fg="#A90000")
        lbl9.place(x=300, y=500)

# ---------------------------------------------set sign in button-------------------------
        btn_signup = Button(Frame_Register, text="Sign up", bg="#ED5843", font=("", 15, "bold"), fg="Black",
                      command=self.reg_data)
        btn_signup.place(width=200, height=30, x=350, y=450)

        btn_signin = Button(Frame_Register,border=0, text="Sign_in", bg="#2A556C", font=("", 10, "bold"), fg="#72E73C",
                       command= lambda *a: self.open_login1())

        btn_signin.place(x=500, y=500)
        self.mainloop()

    # -----------------------------validation-----------------------------
    # def reg_Email(self, emailchecking):
    #     if len(emailchecking)>8:
    #         if re.match(r'\b[A-Za-z0-9_.]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', emailchecking):
    #             return True
    #         else:
    #             messagebox.showerror("Error", "Enter valid email")
    #             return False
    #     else:
    #         messagebox.showerror("Error", "short email length")
    #
    # def number(self, number_checking):
    #     if len(number_checking) == 10:
    #         if re.match('\d{10}', number_checking):
    #             messagebox.showinfo('Success', 'Validation Successfully !!')
    #             self.open_login1()
    #
    #             return True
    #         else:
    #             messagebox.showerror("Error", "Enter number only")
    #             return False
    #     else:
    #         messagebox.showerror("Error", "short Telephone number length")
    #
        # ---------------------------function---------------------------

    def open_login1(self):
        self.destroy()
        Login1()

    # def open_Driver(self, e):
    #     if self.combo.get()=="Driver":
    #
    #         self.destroy()
    #         Driver()

    # def backtohome(self):
    #     self.destroy()
    #     self.home.deiconify()

    def middleware(self):
        obje = Register_middleware.RegisterMiddleware()
        obje.set_regname = self.reg_Name.get()
        obje.set_regaddress = self.reg_Address.get()
        obje.set_regemail = self.reg_Email.get()
        obje.set_regtelephone = self.reg_Telephone_No.get()
        obje.set_reggender = self.reg_Gender.get()
        obje.set_regpassword = self.reg_Password.get()
        # print(obje.__str__())
        obje.insert_data()

    def reg_data(self):
        if self.reg_Name.get() == "" and self.reg_Email.get() == ""  and self.reg_Address.get() == "" and self.reg_Telephone_No.get() == "" and  self.reg_Password.get() == "":
            messagebox.showerror("Error","Fill all the requirement")

        elif self.reg_Name.get() =="" :
            messagebox.showerror("Error", "Enter your name")

        elif self.reg_Email.get() == "" :
            messagebox.showerror("Error","Enter your Email")

        elif self.reg_Address.get() == "" :
            messagebox.showerror("Error","Enter your Address")

        elif self.reg_Telephone_No.get() == "" :
            messagebox.showerror("Error","Enter your Telephone_No")

        elif self.reg_Password.get() == "" :
            messagebox.showerror("Error", "Enter your password")


        elif self.combo.get() == "" :
            messagebox.showerror("Error","select your gender")


        else :
            messagebox.showinfo("Success","Successful")
            # self.open_login1()

            self.middleware()


if __name__ == '__main__':
    login = Register()