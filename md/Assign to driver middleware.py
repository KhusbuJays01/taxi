class AssignToDriverMiddleware:
    def __init__(self):

        # --------------variable------------

        self.CustomerName = ""
        self.DriverName = ""


        # ----------getter----------
        @property
        def get_customername(self):
            return self.CustomerName

        @property
        def get_drivername(self):
            return self.DriverName

        # ----------setter----------

        @get_customername.setter
        def self_customername(self, customername):
            self_CustomerName = customername


        @get_drivername.setter
        def self_drivername(self, drivername):
            self_Drivername = drivername