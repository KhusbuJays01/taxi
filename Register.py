import re
from tkinter import *
from tkinter import ttk, messagebox

import mysql.connector

from login1 import Login1


# from PIL import ImageTk
# set window
class Register(Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration")
        self.geometry('1360x710')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()
        # self.wm_state("zoomed")

        # variable
        self.reg_id = IntVar()
        self.reg_User_Type = StringVar()
        self.reg_Name = StringVar()
        self.reg_Address = StringVar()
        self.reg_Licesnse = StringVar()
        self.reg_Email = StringVar()
        self.reg_Telephone_No = StringVar()
        self.reg_Gender = StringVar()
        self.reg_Password = StringVar()

        # set background color
        self.configure(background="#707FA6")
        self.geometry('990x660+50+50')

        # next  window
        label_Resister = Label(bg="#2A556C", width=123, height=40)
        label_Resister.place(x=50, y=25)

        # Title
        head = Label(text="Registration System", bg="#2A556C", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=300, y=50)

        lbl1 = Label(label_Resister, text="User_Type:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl1.place(x=200, y=100)

        combo = ttk.Combobox(label_Resister, textvariable=self.reg_User_Type, values=["Admin", "Customer", "Driver"])
        combo.place(width=300, x=350, y=110)

        lbl2 = Label(label_Resister, text="Full_Name:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl2.place(x=200, y=150)

        self.ent2 = Entry(label_Resister, textvariable=self.reg_Name, width=50)
        self.ent2.place(x=350, y=150)

        lbl3 = Label(label_Resister, text="Email:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl3.place(x=200, y=200)

        self.ent3 = Entry(label_Resister, textvariable=self.reg_Email, width=50)
        self.ent3.place(x=350, y=200)

        lbl4 = Label(label_Resister, text="Address:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl4.place(x=200, y=250)

        self.ent4 = Entry(label_Resister, textvariable=self.reg_Address, width=50)
        self.ent4.place(x=350, y=250)

        lbl5 = Label(label_Resister, text="Phone_No.:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl5.place(x=200, y=300)

        self.ent5 = Entry(label_Resister, textvariable=self.reg_Telephone_No, width=50)
        self.ent5.place(x=350, y=300)

        lbl6 = Label(label_Resister, text="Gender:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl6.place(x=200, y=350)

        combo = ttk.Combobox(label_Resister, textvariable=self.reg_Gender, values=["Male", "Female", "Other"])
        combo.place(width=300, x=350, y=350)

        lbl7 = Label(label_Resister, text="Password:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl7.place(x=200, y=400)

        self.ent7 = Entry(label_Resister, textvariable=self.reg_Password, width=50)
        self.ent7.place(x=350, y=400)

        lbl11 = Label(label_Resister, text="license:", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        lbl11.place(x=200, y=450)

        self.ent11 = Entry(label_Resister, textvariable=self.reg_Licesnse, width=50)
        self.ent11.place(x=350, y=450)

        lbl8 = Button(label_Resister, text="Create", bg="#ED5843", font=("", 15, "bold"), fg="Black",
                      command=self.reg_db)
        lbl8.place(width=200, height=30, x=350, y=500)

        lbl9 = Label(label_Resister, text="Already have an account!!", bg="#2A556C", font=("", 10, "bold"),
                     fg="#A90000")
        lbl9.place(x=250, y=550)

        lbl10 = Button(label_Resister, border=0, text="Sign_in", bg="#2A556C", font=("", 10, "bold"), fg="#72E73C",
                       command= lambda *a: self.open_login1())

        lbl10.place(x=500, y=560)
        self.mainloop()
        # lbl10.bind("<Button>",self.open_login1)

    def open_login1(self):
        self.destroy()
        Login1()

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
                return True
            else:
                messagebox.showerror("Error", "Enter number only")
                return False
        else:
            messagebox.showerror("Error", "short Telephone number length")




    # Database connection

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

        elif self.reg_Licesnse.get() == '':
            messagebox.showerror("Error","Enter your License")

        elif self.reg_Email.get() != None or self.reg_Telephone_No != None:
            self.em = self.email(self.reg_Email.get())
            self.em1 = self.number(self.reg_Telephone_No.get())


        # if (self.em==True and self.em1==True):
        #     try:
        #
        #         con = mysql.connector.connect(host='localhost', user='root', password='', database='khusbu')
        #         cur = con.cursor()
        #         query = ('Select * from Registration where email = %s')
        #         values = (self.reg_Email.get(),)
        #         cur.execute(query, values)
        #         row = cur.fetchone()
        #         if row != None:
        #             messagebox.showerror("Error", "no user found")
        #         else:
        #             cur.execute('insert into Registration values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
        #                 self.reg_id.get(),
        #                 self.reg_User_Type.get(),
        #                 self.reg_Name.get(),
        #                 self.reg_Address.get(),
        #                 self.reg_Licesnse.get(),
        #                 self.reg_Email.get(),
        #                 self.reg_Telephone_No.get(),
        #                 self.reg_Gender.get(),
        #                 self.reg_Password.get(),
        #             ))
        #             con.commit()
        #             con.close()
        #             messagebox.showinfo("Ok", "Saved")
        #     except Exception as ex:
        #         print(ex)
        #         messagebox.showerror("Error", "Error")



if __name__ == '__main__':
    login = Register()
