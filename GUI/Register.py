import re
from tkinter import *
from tkinter import ttk, messagebox

import mysql.connector

from Driver import Driver
from login1 import Login1

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
        lbl1 = Label(Frame_Register, text="User_Type:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl1.place(x=200, y=100)


        lbl2 = Label(Frame_Register, text="Full_Name:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl2.place(x=200, y=150)

        lbl3 = Label(Frame_Register, text="Email:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl3.place(x=200, y=200)

        lbl4 = Label(Frame_Register, text="Address:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=200, y=250)

        lbl5 = Label(Frame_Register, text="Phone_No.:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl5.place(x=200, y=300)

        lbl6 = Label(Frame_Register, text="Gender:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl6.place(x=200, y=350)

        lbl7 = Label(Frame_Register, text="Password:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl7.place(x=200, y=400)


        # ---------------combo box------------------------------
        self.combo = ttk.Combobox(Frame_Register, textvariable=self.reg_User_Type, values=["Admin", "Customer", "Driver"])
        self.combo.place(width=300, x=350, y=110)
        self. combo.bind("<<ComboboxSelected>>", self.open_Driver)


        # -----------------------entry set-------------------------------

        self.ent2 = Entry(Frame_Register, textvariable=self.reg_Name, width=50)
        self.ent2.place(x=350, y=150)


        self.ent3 = Entry(Frame_Register, textvariable=self.reg_Email, width=50)
        self.ent3.place(x=350, y=200)


        self.ent4 = Entry(Frame_Register, textvariable=self.reg_Address, width=50)
        self.ent4.place(x=350, y=250)



        self.ent5 = Entry(Frame_Register, textvariable=self.reg_Telephone_No, width=50)
        self.ent5.place(x=350, y=300)



        combo = ttk.Combobox(Frame_Register, textvariable=self.reg_Gender, values=["Male", "Female", "Other"])
        combo.place(width=300, x=350, y=350)



        self.ent7 = Entry(Frame_Register, textvariable=self.reg_Password, width=50)
        self.ent7.place(x=350, y=400)

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
        lbl9.place(x=150, y=500)

# ---------------------------------------------set sign in button-------------------------
        lbl8 = Button(Frame_Register, text="Create", bg="#ED5843", font=("", 15, "bold"), fg="Black",
                      command=self.reg_db)
        lbl8.place(width=200, height=30, x=350, y=500)

        lbl10 = Button(Frame_Register,border=0, text="Sign_in", bg="#2A556C", font=("", 10, "bold"), fg="#72E73C",
                       command= lambda *a: self.open_login1())

        lbl10.place(x=600, y=500)
        self.mainloop()

    # -----------------------------validation-----------------------------
    def email(self, emailchecking):
        if len(emailchecking)>8:
            if re.match(r'\b[A-Za-z0-9_.]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', emailchecking):
                return True
            else:
                messagebox.showerror("Error", "Enter valid email")
                return False
        else:
            messagebox.showerror("Error", "short email length")

    def number(self, number_checking):
        if len(number_checking) == 10:
            if re.match('\d{10}', number_checking):
                messagebox.showinfo('Success', 'Validation Successfully !!')
                self.open_login1()

                return True
            else:
                messagebox.showerror("Error", "Enter number only")
                return False
        else:
            messagebox.showerror("Error", "short Telephone number length")

        # ---------------------------function---------------------------

    def open_login1(self):
        self.destroy()
        Login1()

    def open_Driver(self, e):
        if self.combo.get()=="Driver":

            self.destroy()
            Driver()

    # def backtohome(self):
    #     self.destroy()
    #     self.home.deiconify()


    #------------------------------------------ Database connection

    def reg_db(self):
      # if self.reg_Name.get() == '':
        # #         messagebox.showerror("ERROR", "Choose your user type")

        if self.reg_Name.get() == '':
            messagebox.showerror("Error","Enter your Full_Name")

        elif self.reg_Email.get() == '':
            messagebox.showerror("Error", "Enter your Email address")

        elif self.reg_Address.get() == '':
            messagebox.showerror("Error","Enter your Address")

        elif self.reg_Telephone_No.get() == '':
            messagebox.showerror("Error","Enter your Telephone_NO.")

        elif self.reg_Gender.get() == '':
            messagebox.showerror("Error","Enter your Gender")

        elif self.reg_Password.get() == '':
            messagebox.showerror("Error","Enter your Password")

        # elif self.reg_Licesnse.get() == '':
        #     messagebox.showerror("Error","Enter your License")

        elif self.reg_Email.get() != None or self.reg_Telephone_No != None:
            self.em = self.email(self.reg_Email.get())
            self.em1 = self.number(self.reg_Telephone_No.get())




if __name__ == '__main__':
    login = Register()
