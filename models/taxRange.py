# In taxRange.py

from models.taxModel import TaxModel



class TaxRange(TaxModel):
    def __init__(self,year, tax_code, description,start_salary, end_salary, tax_rate, code):
        super().__init__(year, tax_code,description)        
        self.start_salary = start_salary
        self.end_salary = end_salary
        self.tax_rate = tax_rate
        self.code = code 
    
    @classmethod
    def from_model(cls, model, start_salary, end_salary, tax_rate, code):
        return cls(model.year, model.tax_code, model.description, start_salary, end_salary, tax_rate, code)


    def __repr__(self):
        return (
                f'Code : {self.get_code()},\n'
                f'Tax Rate : {self.get_taxRate()},\n' 
                f'Start Salary: {self.get_startSalary()},\n' 
                f'End Salary: {self.get_endSalary()},\n'  
                f'Status: {self.get_taxCode()},\n' 
                f'Description: {self.get_description()}')           
    

    def get_startSalary(self):
        return self.start_salary
    
    def get_endSalary(self):
        return self.end_salary

    def get_taxRate(self):
        return self.tax_rate
    
    def get_code(self):
        return self.code


