from tkinter import messagebox

import mysql.connector

from database import Database

class RegisterMiddleware:

    def __init__(self,reg_id=0, reg_Name="",reg_Address="",reg_Email="",reg_Telephone_No="",reg_Gender="",reg_Password=""):

    # ---------------variable-------------------
    #     self.reg_User_Type = ""
        self.reg_id = reg_id
        self.reg_Name = reg_Name
        self.reg_Address = reg_Address
        self.reg_Email = reg_Email
        self.reg_Telephone_No = reg_Telephone_No
        self.reg_Gender = reg_Gender
        self.reg_Password = reg_Password

        # --------------getter----------------

        # @property
        # def get_regusertype(self):
        #     return self.reg_User_Type

    @property
    def get_regname(self):
        return self.reg_Name

    @property
    def get_regaddress(self):
        return self.reg_Address

    @property
    def get_regemail(self):
        return self.reg_Email

    @property
    def get_regtelephone(self):
        return self.reg_Telephone_No

    @property
    def get_reggender(self):
        return self.reg_Gender

    @property
    def get_regpassword(self):
        return self.reg_Password

    # ------------------------setter--------------------

    # @get_regusertype.setter
    # def set_regusertype(self,regusertype):
    #     self.reg_User_Type = regusertype

    @get_regname.setter
    def set_regname(self,regname):
        self.reg_Name = regname

    @get_regaddress.setter
    def set_regaddress(self,regaddress):
        self.reg_Address = regaddress

    @get_regemail.setter
    def set_regemail(self, regemail):
        self.reg_Email = regemail

    @get_regtelephone.setter
    def set_regtelephone(self, regtelephone):
        self.reg_Telephone_No = regtelephone

    @get_reggender.setter
    def set_reggender(self,reggender):
        self.reg_Gender = reggender

    @get_regpassword.setter
    def set_regpassword(self,regpassword):
        self.reg_Password = regpassword

    def __str__(self):
        return str(self.reg_id) + "," + self.reg_Name + "," + self.reg_Address + "," + self.reg_Email + "," + self.reg_Telephone_No + "," + self.reg_Gender + "," + self.reg_Password


    def insert_data(self):
        db = Database.maindatabse()
        conn = db.databaseConnection()

        if conn:
            cursor = conn.cursor()
            sql = 'INSERT INTO customer(User_Types, Name, Address, Email, Telephone, Gender, Password) values(%s, %s, %s, %s, %s, %s, %s)'
            values = ('Customer', self.get_regname, self.get_regaddress, self.get_regemail, self.get_regtelephone, self.get_reggender, self.get_regpassword)
            try:
                cursor.execute(sql, values)
            except mysql.connector.Error as e:
                messagebox.showerror('Error', e.msg)
            else:
                conn.commit()
                conn.close()
                return True