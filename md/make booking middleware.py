class makebookingmiddleware:
    def __init__(self):

        # --------------variable-----------------
        self.Pick_Up_Address = ""
        self.Pick_Up_Time = ""
        self.Pick_Up_Date = ""
        self.Drop_Address = ""
        self.Drop_Time = ""
        self.Drop_Date = ""

        # ----------------getter-----------
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


        # --------setter----------
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


#         self.mainloop()
# if __name__ == '__main__':
#         login = makebookingmiddleware
