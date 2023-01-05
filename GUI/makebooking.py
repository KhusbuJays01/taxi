import re
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

from Middleware import make_booking_middleware
from Middleware.make_booking_middleware import makebookingmiddleware
from database import Database

class makebooking(Tk):
        # print("Hello")

    #     #-------------------- validation --------------------
    #
    #     # def pickupaddress(self, pickupaddresschecking):
    #     #     if len(pickupaddresschecking)>8:
    #     #         if re.match(r'\b[A-Za-z0-9_.]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', emailchecking):
    #     #             return True
    #     #         else:
    #     #             messagebox.showerror("Error", "Enter valid email")
    #     #             return False
    #     #     else:
    #     #         messagebox.showerror("Error", "short email length")
    #     # save
    #     # display confirm message


    def __init__(self):
        super().__init__()
        self.title("Make Booking")
        self.geometry('1360x710')
        self.frame = Frame(self)
        self.resizable(False, False)
        self.frame.pack()

        # -----------variable-------
        self.bokingstatus = IntVar()
        self.pickup_address = StringVar()
        self.pickup_date = StringVar()
        self.pickup_time = StringVar()
        self.drop_address = StringVar()
        self.drop_date = StringVar()
        self.drop_time = StringVar()

        # set background color
        self.configure(background="#707FA6")
        self.geometry('990x660+50+50')

        # next  window
        Frame_makebooking = Frame(bg="#2A556C", width=900, height=550)
        Frame_makebooking.place(x=50, y=40)

        # # Title
        head = Label(text="Make Booking", bg="#2A556C", font=("", 25, "bold"), fg="#FFFAFA")
        head.place(x=370, y=80)

        #------------------------------- sencond head--------------------
        head = Label(text="Pick Up--------------------------", bg="#2A556C", font=("", 20, "bold"), fg="#FFFAFA")
        head.place(x=100, y=150)

        picAddress = Label(Frame_makebooking, text="Address :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        picAddress.place(x=50, y=170)

        self.pickup_address = Entry(Frame_makebooking, width=35,textvariable=self.pickup_address)
        self.pickup_address.place(x=153, y=175)

        picTime = Label(Frame_makebooking, text="Time :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        picTime.place(x=50, y=220)

        self.picTime = Entry(Frame_makebooking, width=35,textvariable=self.pickup_time)
        self.picTime.place(x=153, y=225)

        picDate = Label(Frame_makebooking, text="Date :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        picDate.place(x=50, y=255)

        self.picDate = DateEntry(Frame_makebooking,width=18,font=('Time New Roman',16),textvariable=self.pickup_date)
        self.picDate.place(x=150,y=260)

        head = Label(text="Drop-------------------------------", bg="#2A556C", font=("", 20, "bold"), fg="#FFFAFA")
        head.place(x=540, y=150)

        dropAddress = Label(Frame_makebooking, text="Address :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        dropAddress.place(x=490, y=170)

        self.dropAddress = Entry(Frame_makebooking, width=35,textvariable=self.drop_address)
        self.dropAddress.place(x=600, y=175)
        print(self.dropAddress.get())

        dropTime = Label(Frame_makebooking, text="Time :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        dropTime.place(x=490, y=220)

        self.dropTime = Entry(Frame_makebooking, width=35,textvariable=self.drop_time)
        self.dropTime.place(x=600, y=225)

        dropDate = Label(Frame_makebooking, text="Date :", bg="#2A556C", font=("", 15, "bold"), fg="#FFFAFA")
        dropDate.place(x=490, y=255)

        self.dropDate = DateEntry(Frame_makebooking,width=18,font=('Time New Roman',16),textvariable=self.drop_date)
        self.dropDate.place(x=600, y=260)

        # -------------------------------------------button---------------------------------------------

        btnConfirm = Button(Frame_makebooking, text="Confirm", bg="Green", font=("", 15, "bold"), fg="Black",command=self.confirmbooking) # command=function name to perform
        btnConfirm.place(x=90, y=300, width=90)

        btnEdit = Button(Frame_makebooking, text="Edit", bg="gray", font=("", 15, "bold"), fg="Black")
        btnEdit.place(x=250, y=300, width=90)

        btnClear = Button(Frame_makebooking, text="Clear", bg="blue", font=("", 15, "bold"), fg="Black")
        btnClear.place(x=400, y=300, width=90)

        btnView = Button(Frame_makebooking, text="Delete", bg="orange", font=("", 15, "bold"), fg="Black")
        btnView.place(x=550, y=300, width=90)

        btnDelete = Button(Frame_makebooking, text="LogOut", bg="red", font=("", 15, "bold"), fg="Black")
        btnDelete.place(x=700, y=300, width=90)

        # label_makebooking = Label(bg="white", width=120, height=12)
        # label_makebooking.place(x=80, y=390)

        ##constructing table
        column = ('Booking_id', 'pickup_address', 'picTime', 'picDate', 'dropAddress', 'dropTime','dropDate',
            'booking_status')
        self.table = ttk.Treeview(Frame_makebooking, columns=column, show='headings')
        #------------------------defining heading-----------------------------------
        self.table.heading('Booking_id', text='Booking ID')
        self.table.heading('pickup_address', text='pickup_address')
        self.table.heading('picTime', text='Pickup-Time')
        self.table.heading('picDate', text='Pickup_date')
        self.table.heading('dropAddress', text='Drop_Address')
        self.table.heading('dropTime', text='Drop_time')
        self.table.heading('dropDate', text='Drop_Date')
        self.table.heading('booking_status', text='booking_staus')


        #----------------------------Add  style-----------------------------
        style = ttk.Style()
        #---------------------------configure  color-------------------------
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=50,
                        font=("", 10))
        #------------------------sizing the table heading in the columns---------
        self.table.column("Booking_id", anchor=CENTER, stretch=NO, width=80, minwidth=67)
        self.table.column("pickup_address", anchor=CENTER, stretch=NO, width=100)
        self.table.column("picTime", anchor=CENTER, stretch=NO, width=90)
        self.table.column("picDate", anchor=CENTER, stretch=NO, width=110)
        self.table.column("dropAddress", anchor=CENTER, stretch=NO, width=110)
        self.table.column("dropTime", anchor=CENTER, stretch=NO, width=110)
        self.table.column("dropDate", anchor=CENTER, stretch=NO, width=110)
        self.table.column("booking_status", anchor=CENTER,stretch=NO,width=170)
        self.get_table_data()

        #--------------constructing vertical scrollbar-------------------------
        scrlbar = ttk.Scrollbar(Frame_makebooking, orient="vertical", command=self.table.yview)
        # placing scrollbar by using place()
        self.table.place(x=0, y=390, height=670, width=1000)
        scrlbar.place(x=882, y=392, height=157)
        self.table.configure(yscrollcommand=scrlbar.set)


        # -------------confirm booking-----------------------------------------------
        def makebookingmiddleware(self):
            obje = make_booking_middleware.makebookingmiddleware()
            obje.set_bookingstatus = self.bookingstatus.get()
            obje.set_pickup_address = self.pickup_address.get()
            obje.set_pickuptime = self.reg_pickuptime.get()
            obje.set_pickupdate = self.pickupdate.get()
            obje.set_dropaddress = self.dropaddress.get()
            obje.set_droptime = self.droptime.get()
            obje.set_dropdate =self.dropDate.get()
            result = obje.insert_data()

        #     ------------edit booking---------------------------------------------
        # def edit(self):
        #     obje = make_booking_middleware.makebookingmiddleware()
        #     obje.set_pickup_address = self.pickup_address.get()
        #     obje.set_pickupdate = self.pickupdate.strftime("%Y-%m-%d")
        #     obje.set_pickup_time = (self.pickup_time.get() + self.combo_time.get())
        #     obje.set_droptime = self.set_droptime.get()
        #     obje.set_dropdate = self.set_dropdate.get()
        #     obje.set_bookingstatu = "Pending"
        #     obje.edit()
        #     self.table_data()
        self.mainloop()

    # ----------------------validation----------------------------------
    def confirmbooking(self):
            # print("date", self.dropDate.get())
            if self.pickup_address.get() == "" and self.pickup_time.get() == "" and self.pickup_date.get()== "" and self.Drop_address.get() == "" and self.Drop_time.get() == "" and self.Drop_date.get() == "":
                messagebox.showerror("Error", "Fill all the requirement")
            elif self.pickup_address.get() == "":
                messagebox.showerror("Error", "Enter pickupaddress")
            elif self.pickup_time.get() == "":
                messagebox.showerror("Error", "Enter pickuptime")
            elif self.pickup_date.get() == "":
                messagebox.showerror("Error", "Enter pickupdate")
            elif self.drop_address.get() == "":
                messagebox.showerror("Error", "Enter dropaddress")
            elif self.drop_time.get() == "":
                messagebox.showerror("Error", "Enter droptime")
            # elif self.Drop_date.get() == "":
            #     messagebox.showerror("Error", "Enter Drop_date")
            else:
                booked = makebookingmiddleware()
                booked.set_pickupaddress = self.pickup_address.get()
                booked.set_pickuptime =self.pickup_time.get()
                booked.set_pickupdate = self.pickup_date.get()
                booked.set_dropdate = self.drop_date.get() # value not present
                print(booked.set_dropdate)
                booked.set_dropaddress = self.drop_address.get()
                booked.set_droptime = self.drop_time.get()
                booked.insert_data()
                messagebox.showinfo("Success", "Successful")
                self.get_table_data()

    def get_table_data(self):
        db = Database.maindatabse()
        data = db.get_booking_table_data()
        count = 0
        for delete_data in self.table.get_children():
            self.table.delete(delete_data)

        try:
            for i in data:
                self.table.insert('', count, text="",
                                  values=(i[0], i[3], i[4], i[2], i[6], i[7], i[5], i[1]))
        except TypeError:
            pass

if __name__ == '__main__':
    makebooking = makebooking()

