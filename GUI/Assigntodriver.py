from tkinter import *
from tkinter import ttk


class DriverDetail(Tk):
    def __init__(self):
        super().__init__()
        self.title("AssignDiver")
        self.geometry('1360x710')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()

        # set background color
        self.configure(background="#2A556C", width=900, height=550)
        self.geometry('990x660+50+50')


        # Title
        head = Label(text="Assign To Driver ", width=50, height=2, bg="Black", font=("", 25, "bold"),
                     fg="#FFFAFA")
        head.place(x=0, y=0)

        # -------------------name-----------------------
        Customer = Label( text="Customer name :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        Customer.place(x=80, y=150)

        Customer = Entry(width=25)
        Customer.place(x=260, y=155)

        fullname = Label(text="Assign To Driver :", bg="#2A556C", font=("", 15, "bold"), fg="Black")
        fullname.place(x=500, y=150)

        fullname = Entry(width=25)
        fullname.place(x=700, y=155)



        btnsave = Button(text="Save",bg="black",font=("",15,"bold"),fg="white")
        btnsave.place(width=100,height=30,x=350,y=250)

        btnclear = Button(text="Clear",bg="black", font=("",15, "bold"),fg="white")
        btnclear.place(width=100,height=30,x=500,y=250)

        btnedit = Button(text="Edit",bg="black",font=("",15,"bold"),fg="white")
        btnedit.place(width=100,height=30,x=650,y=250)

        btndelete = Button(text="Delete", bg="#ED5843", font=("", 15, "bold"), fg="Black")
        btndelete.place(width=100, height=30, x=800, y=250)


        #
        # label_DriverDetail = Label(bg="white", width=132, height=16)
        # label_DriverDetail.place(x=30, y=390)

        column = ('driverid', 'fullname', 'address', 'email', 'contract', 'combo', 'password','License'
                  )
        self.table = ttk.Treeview(columns=column, show='headings')
        ##defining heading
        self.table.heading('driverid', text='Driver-id')
        self.table.heading('fullname', text='Fullname')
        self.table.heading('address', text='Address')
        self.table.heading('email', text='Email')
        self.table.heading('contract', text='contract')
        self.table.heading('combo', text='Gender')
        # self.table.heading('dropDate', text='Drop_Date')
        self.table.heading('password', text='Password')
        self.table.heading('License',text='License')

        ##Add some style
        style = ttk.Style()
        ##configure our treeview color
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=50,
                        font=("", 10))
        ### sizing the heading in the columns
        self.table.column("driverid", anchor=CENTER, stretch=NO, width=120, minwidth=67)
        self.table.column("fullname", anchor=CENTER, stretch=NO, width=130)
        self.table.column("address", anchor=CENTER, stretch=NO, width=120)
        self.table.column("email", anchor=CENTER, stretch=NO, width=120)
        self.table.column("contract", anchor=CENTER, stretch=NO, width=120)
        self.table.column("combo", anchor=CENTER, stretch=NO, width=120)
        self.table.column("password", anchor=CENTER, stretch=NO, width=120)
        self.table.column("License", anchor=CENTER, stretch=NO, width=120)

        self.get_table_data()

        # constructing vertical scrollbar
        scrlbar = ttk.Scrollbar(orient="vertical", command=self.table.yview)
        # placing scrollbar by using place()
        # placing scrollbar by using place()
        self.table.place(x=0, y=390, height=670, width=1050)
        scrlbar.place(x=972, y=392, height=270)
        self.table.configure(yscrollcommand=scrlbar.set)


        self.mainloop()

    def get_table_data(self):
        pass


if __name__ == '__main__':
        login = DriverDetail ()