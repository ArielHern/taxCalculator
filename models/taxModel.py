# In taxModel.py

class TaxModel:
   
    def __init__(self, year, tax_code, description):
        self.year = year
        self.tax_code = tax_code
        self.description = description      

    def get_year(self):
        return self.year

    def get_taxCode(self):
        return self.tax_code

    def get_description(self):
        return self.description




