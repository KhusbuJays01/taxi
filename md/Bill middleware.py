class Billmiddleware:
    def __init__(self):

        # --------------variable-----------

        self.Customer_Name =""
        self.Rate = ""
        self.VAT = ""
        self.Kilometer = ""


        # ----------------getter-------------
        @property
        def get_customername(self):
            return self.Customer_Name

        @property
        def get_rate(self):
            return self.Rate

        @property
        def get_vat(self):
            return self.VAT

        @property
        def get_kilometer(self):
            return self.Kilometer


        # --------------setter--------------

        @get_customername.setter
        def self_customername(self, customername):
            self_Customer_Name = customername

        @get_rate.setter
        def self_rate(self,rate):
            self_Rate = rate

        @get_vat.setter
        def self_vat(self,vat):
            self_VAT = vat

        @get_kilometer.setter
        def self_kilometer(self, kilometer):
            self_kilometer = kilometer
