# In test.py

import unittest
from taxModel import TaxModel, TaxRange


taxModel_2020_S = TaxModel(2020, 'S', 'Single')
taxrange = TaxRange.from_model(taxModel_2020_S,0, 9325.99, 0.1,"S1")


class Mytest(unittest.TestCase):
    def testRepresentation(self):
        self.assertEqual(taxrange.get_year(), 2020)
        self.assertEqual(taxrange.get_taxCode(), 'S')
        self.assertEqual(taxrange.get_description(), 'Single')
        self.assertEqual(taxrange.get_startSalary(), 0)
        self.assertEqual(taxrange.get_endSalary(), 9325.99)
        self.assertEqual(taxrange.get_taxRate(), 0.1)
        self.assertEqual(taxrange.get_code(), 'S1')




if __name__ == "__main__":
    unittest.main()