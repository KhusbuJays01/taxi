class DriverregMiddleware:

    def __init__(self):

    # ---------------variable-------------------
        self.Name = ""
        self.Address = ""
        self.Email = ""
        self.Telephone_No = ""
        self.Gender = ""
        self.Password = ""
        self.license = ""


        # --------------getter----------------
        @property
        def get_name(self):
            return self.Name

        @property
        def get_address(self):
            return self.Address

        @property
        def get_email(self):
            return self.Email

        @property
        def get_telephone(self):
            return self.Telephone_No

        @property
        def get_gender(self):
            return self.Gender

        @property
        def get_password(self):
            return self.Password

        @property
        def get_license(self):
            return self.license

        # ------------------------setter--------------------
        @get_name.setter
        def setname(self,name):
            self.Name = name

        @get_address.setter
        def set_address(self,address):
            self.Address = address

        @get_email.setter
        def set_email(self, email):
            self.Email = email

        @get_telephone.setter
        def set_telephone(self, telephone):
            self.Telephone_No = telephone

        @get_gender.setter
        def set_gender(self,gender):
            self.Gender = gender

        @get_password.setter
        def set_password(self,password):
            self.Password = password

        @get_license.setter
        def set_license(self,license):
            self.license = license




        # self.mainloop()
# if __name__ == '__main__':
#         login = DriverregMiddleware ()



