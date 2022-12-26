class forgetmiddleware:

    def __init__(self):
        self.for_User_Type = ""
        self.for_Email = ""
        self.for_New_Password = ""
        self.for_Confirm_Password = ""

        # -----------getter-------------
        @property
        def get_forusertype(self):
            return self.for_User_Type

        @property
        def get_foremail(self):
            return self.for_Email

        @property
        def get_fornewpassword(self):
            return self.for_New_Password

        @property
        def get_forconfirmpassword(self):
            return self.for_Confirm_Password

        # ------------setter---------------
        @get_forusertype.setter
        def set_forusertype(self, forusertype):
            self.for_User_Type = forusertype

        @get_foremail.setter
        def set_foremail(self, foremail):
            self.for_Email = foremail

        @get_fornewpassword.setter
        def set_fornewpassword(self,fornewpassword):
            self.for_New_Password = fornewpassword

        @get_forconfirmpassword.setter
        def set_forconfirmpassword(self, forconfirmpassword):
            self.for_Confirm_Password = forconfirmpassword


#
#         self.mainloop()
# if __name__ == '__main__':
#         login = forgetmiddleware ()



