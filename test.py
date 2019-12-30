# In test.py

import unittest
from taxModel import TaxModel, TaxRange
# from taxResourceModel import TaxResource

# taxtest = TaxResource()

taxModel_2020_S = TaxModel(2020, 'S', 'Single')
taxrange = TaxRange.from_model(taxModel_2020_S,0, 9325.99, 0.1,"S1")


class TaxModelTest(unittest.TestCase):
    def test_get_year(self):
        self.assertEqual(taxrange.get_year(), 2020)

    def test_get_taxCode(self):
        self.assertEqual(taxrange.get_taxCode(), 'S')

    def test_get_description(self):
        self.assertEqual(taxrange.get_description(), 'Single')
    
    def test_get_startSalary(self):        
        self.assertEqual(taxrange.get_startSalary(), 0)
    
    def test_get_endSalary(self):
        self.assertEqual(taxrange.get_endSalary(), 9325.99)
    
    def test_get_taxRate(self):
        self.assertEqual(taxrange.get_taxRate(), 0.1)

    def test_get_code(self):
        self.assertEqual(taxrange.get_code(), 'S1')

           


if __name__ == "__main__":
    unittest.main()