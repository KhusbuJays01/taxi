class loginmiddleware:

    def __init__(self):
        self.log.id = ""
        self.log.User_Type = ""
        self.Log.User_Name = ""
        self.log.Password = ""

        # ----------------getter----------------

        @property
        def get_logid(self):
            return self.logid

        @property
        def get_logusertype(self):
            return self.log_User_Type

        @property
        def get_logusername(self):
            return self.log_User_Name

        @property
        def get_logpassword(self):
            return self.log_Password

        # -----------------setter------------

        @get_logid.setter
        def set_logid(self,logid):
            self.logid = logid

        @get_logusertype.setter
        def set_logusertype(self,logusertype):
            self.log_User_Type = logusertype

        @get_logusername.setter
        def set_logusername(self,logusername):
            self.log_User_Name = logusername

        @get_logpassword.setter
        def set_logpassword(self,logpassword):
            self.log_Password = logpassword

#         self.mainloop()
# if __name__ == '__main__':
#         login = loginmiddleware ()



