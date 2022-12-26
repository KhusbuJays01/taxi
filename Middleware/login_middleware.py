from database import Database
from tkinter import messagebox

class Login_middleware:
    def __init__(self):
        self.login_id = ''
        self.login_usertype = ''
        self.login_email = ''
        self.login_pass = ''

    @property
    def get_login_id(self):
        return self.login_id

    @property
    def get_login_usertype(self):
        return self.login_usertype

    @property
    def get_login_email(self):
        return self.login_email

    @property
    def get_login_pass(self):
        return self.login_pass


    @get_login_id.setter
    def set_login_id(self, login_id):
        self.login_id = login_id

    @get_login_usertype.setter
    def set_login_usertype(self, login_usertype):
        self.login_usertype = login_usertype

    @get_login_email.setter
    def set_login_email(self, login_email):
        self.login_email = login_email

    @get_login_pass.setter
    def set_login_pass(self, login_pass):
        self.login_pass = login_pass

    def __str__(self):
        return self.get_login_usertype + ' ' + self.get_login_email + ' ' + self.get_login_pass


    def login_database(self):
        db = Database.maindatabse()
        conn = db.databaseConnection()

        if conn:
            cursor = conn.cursor()
            sql = 'SELECT Customer_Id, User_Types, Email, Password FROM customer where Email = %s and Password = %s'
            values = (self.get_login_email, self.get_login_pass)
            try:
                cursor.execute(sql, values)
            except:
               messagebox.showerror('Error', 'Database Error')
            else:
                store = cursor.fetchone()
                return store
