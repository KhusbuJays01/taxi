class DriverDetailMiddleware:
    def __init__(self):
        # --------------variable----------
        self.Drivr_id = ""
        self.FullName = ""
        self.Address = ""
        self.Email = ""
        self.Phone_No = ""
        self.Password = ""
        self.Gender = ""
        self.license = ""

        # ----------------getter--------------
        @property
        def get_drievrid(self):
            return self.Driver_id

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

        @property
        def get_license(self):
            return self.license

        # ----------------setter----------------

        @get_drievrid.setter
        def set_driverid(self, driverid):
            self.Driver_id = driverid

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

        @get_license.setter
        def self_license(self,license):
            self_license = license




#         self.mainloop()
# if __name__ == '__main__':
#         login = DriverDetailMiddleware

