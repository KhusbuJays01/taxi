class CustomerviewlMiddleware:
    def __init__(self):
        # --------------variable----------
        self.Customer_id = ""
        self.FullName = ""
        self.Address = ""
        self.Email = ""
        self.Phone_No = ""
        self.Password = ""
        self.Gender = ""

        # ----------------getter--------------
        @property
        def get_Customerid(self):
            return self.Customer_id

        @property
        def get_FullName (self):
            return self.FullName

        @property
        def get_address(self):
            return self.Address

        @property
        def get_email(self):
            return self.Email

        @property
        def get_phone(self):
            return self.Phone_No

        @property
        def get_password(self):
            return self.Password

        @property
        def get_gender(self):
            return self.Gender

        # ----------------setter----------------

        @get_Customerid.setter
        def set_customerid(self, customerid):
            self.Customer_id = get_Customerid

        @get_FullName.setter
        def set_FullName(self,FullName):
            self.FullName = FullName

        @get_address.setter
        def self_address(self,address):
            self.Address = address

        @get_email.setter
        def self_email(self,email):
            self_email = email

        @get_phone.setter
        def self_phone(self,phone):
            self_phone = phone

        @get_password.setter
        def self_password(self,password):
            self_password = password

        @get_gender.setter
        def self_gender(self, gender):
            self_gender = gender

#         self.mainloop()
# if __name__ == '__main__':
#         login = DriverDetailMiddleware

