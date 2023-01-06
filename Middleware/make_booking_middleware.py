import sys
from tkinter import messagebox
import mysql
from database import Database
class makebookingmiddleware:
    def __init__(self):
        # --------------variable-----------------
        self.Booking_Status = ""
        self.Pick_Up_Address = ""
        self.Pick_Up_Time = ""
        self.Pick_Up_Date = ""
        self.Drop_Address = ""
        self.Drop_Time = ""
        self.Drop_Date = ""
        self.customer_id = ""
        # ----------------getter-----------
    @property
    def get_bookingstatus(self):
        return self.Booking_Status
    @property
    def get_pickupaddress(self):
        return self.Pick_Up_Address
    @property
    def get_pickuptime(self):
        return self.Pick_Up_Time
    @property
    def get_pickupdate(self):
        return self.Pick_Up_Date
    @property
    def get_dropaddress(self):
        return self.Drop_Address
    @property
    def get_droptime(self):
        return self.Drop_Time
    @property
    def get_dropdate(self):
        return self.Drop_Date
    @property
    def get_customer_id(self):
        return self.customer_id

    # --------setter----------
    @get_bookingstatus.setter
    def set_bookingstatus(self, bookingstatus):
        self.Booking_Status = bookingstatus
    @get_pickupaddress.setter
    def set_pickupaddress(self, pickupaddress):
        self.Pick_Up_Address = pickupaddress

    @get_pickuptime.setter
    def set_pickuptime(self, pickuptime):
        self.Pick_Up_Time = pickuptime

    @get_pickupdate.setter
    def set_pickupdate(self, pickupdate):
        self.Pick_Up_Date = pickupdate

    @get_dropaddress.setter
    def set_dropaddress(self, dropaddress):
        self.Drop_Address = dropaddress

    @get_droptime.setter
    def set_droptime(self, droptime):
        self.Drop_Time = droptime

    @get_dropdate.setter
    def set_dropdate(self, dropdate):
        self.Drop_Date = dropdate

    @get_customer_id.setter
    def set_customer_id(self,customerid):
        self.customer_id = customerid

    def __str__(self):
        return self.get_dropdate+", "+self.get_droptime+", "+self.get_dropaddress

    def insert_data(self):
        db = Database.maindatabse()
        conn = db.databaseConnection()
        if conn:
            cursor = conn.cursor()
            sql = 'INSERT INTO Booking(Booking_status, PickUp_date, PicUP_addess, PickUp_time, Drop_date, Drop_address,Drop_time,CustomerCustomer_id) values(%s, %s, %s, %s, %s, %s,%s,%s)'
            values = (
            'Pending',self.get_pickupdate, self.get_pickupaddress, self.get_pickuptime, self.get_dropdate, self.get_dropaddress,
            self.get_droptime,self.get_customer_id)
            print(values)
            try:
                cursor.execute(sql, values)
            except mysql.connector.Error as e:
                messagebox.showerror('Error', e.msg)
            else:
                conn.commit()
                conn.close()
                return True

    #         ----------edit booking---------------

    def edit(self, values):
        db = Database.maindatabse()
        conn = db.databaseConnection()

        if conn:
            mycursor = conn.cursor()
            sql = 'update booking SET PickUp_date=%s, PicUP_addess=%s, PickUp_time=%s, drop_address=%s,Drop_date=%s, Drop_time=%s WHERE Booking_id = %s'
            mycursor.execute(sql, values)
            conn.commit()
            messagebox.showinfo("TBS", "Booking Updated Successfully")
        else:
            messagebox.showerror("TBS", "Booking Updated Error")

    # #         ---------------------------------delete--------------------------------


    #         messagebox.showinfo("delete", "You are sure to delete data")

