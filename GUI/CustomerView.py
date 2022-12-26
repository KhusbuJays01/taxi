from tkinter import *
from tkinter import ttk


class CustomerView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Customer Detail")
        self.geometry('1360x710')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()

        # set background color
        self.configure(background="#2A556C", width=900, height=550)
        self.geometry('990x660+50+50')


        # Title
        head = Label(text=" Customer Detail", width=50, height=2, bg="Black", font=("", 25, "bold"),
                     fg="#FFFAFA")
        head.place(x=0, y=0)

        Searchcustomer = Label(text="Search Customer  :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        Searchcustomer.place(x=270, y=105)

        customerid = Entry(width=25)
        customerid.place(x=450, y=110)



        # -------------------name-----------------------
        customerid = Label( text="Customer Id :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        customerid.place(x=80, y=150)

        customerid = Entry(width=25)
        customerid.place(x=260, y=155)

        fullname = Label(text="FullName :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        fullname.place(x=450, y=150)

        fullname = Entry(width=25)
        fullname.place(x=600, y=155)

        address = Label(text="Address :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        address.place(x=80, y=200)

        address = Entry(width=25)
        address.place(x=260, y=200)

        email = Label(text="Email :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        email.place(x=450, y=200)

        ent5 = Entry(width=25)
        ent5.place(x=600, y=200)

        Contract = Label(text="Contract No. :", bg="#2A556C", font=("", 15, "bold"), fg="black")
        Contract.place(x=80, y=250)

        contract = Entry(width=25)
        contract.place(x=260, y=250)

        gender = Label(text="Gender :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        gender.place(x=80, y=300)

        self.combo = ttk.Combobox(values=["Male", "Female", "Other"])
        self.combo.place(x=260, y=300)

        password = Label(text="Password :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        password.place(x=450, y=250)

        password = Entry(width=25)
        password.place(x=600, y=250)

        save = Button(text="Save",bg="black",font=("",15,"bold"),fg="white")
        save.place(width=100,height=30,x=350,y=350)

        clear = Button(text="Clear",bg="black", font=("",15, "bold"),fg="white")
        clear.place(width=100,height=30,x=500,y=350)

        edit = Button(text="Edit",bg="black",font=("",15,"bold"),fg="white")
        edit.place(width=100,height=30,x=650,y=350)

        delete = Button(text="Delete", bg="#ED5843", font=("", 15, "bold"), fg="Black")
        delete.place(width=100, height=30, x=800, y=350)



        label_CustomerView = Label(bg="white", width=132, height=16)
        label_CustomerView.place(x=30, y=390)


        self.mainloop()
if __name__ == '__main__':
        login = CustomerView ()