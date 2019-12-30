# In TaxResource

from taxModel import TaxModel,TaxRange



taxModel_2020_S = TaxModel(2020, 'S', 'Single')
taxModel_2020_MFJ = TaxModel(2020, 'MFJ', 'Married Filing Jointly')
taxModel_2020_QW = TaxModel(2020, 'QW', 'Qualified Widow(er)')
taxModel_2020_MFS = TaxModel(2020, 'MFS', 'Married Filing Separately')
taxModel_2020_HH = TaxModel(2020, 'HH', 'Head of Household')

taxrange = []

# single
taxrange.append(TaxRange.from_model(taxModel_2020_S,0, 9700.99, 0.1,"S1"))
taxrange.append(TaxRange.from_model(taxModel_2020_S, 9701, 39475.99,0.15,'S2'))
taxrange.append(TaxRange.from_model(taxModel_2020_S, 39476, 84200.99,0.25,'S3'))
taxrange.append(TaxRange.from_model(taxModel_2020_S, 84201, 160725.99,0.28,'S4'))
taxrange.append(TaxRange.from_model(taxModel_2020_S, 160726, 204100.99,0.33,'S5'))
taxrange.append(TaxRange.from_model(taxModel_2020_S, 204101, 510300.99,0.35,'S6'))
taxrange.append(TaxRange.from_model(taxModel_2020_S, 510301, 9999999.99,0.396,'S6'))


# Married, filing jointly
taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 0 ,19400.99 ,.1,'MFJ1'))
taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 19401, 78950.99, .12, 'MFJ2'))
taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 78951 ,168400.99 ,.22,'MFJ3'))
taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 168401,321450.99 ,.24,'MFJ4'))
taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 321451 ,408200.99 ,.32,'MFJ5'))
taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 408201,612350.99 ,.35,'MFJ6'))
taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 612351 ,9999999.99 ,.1,'MFJ7'))





def taxRage_calculator(salary, status):
        rv = tuple(x for x in taxrange if x.get_endSalary() >= salary and x.get_startSalary() <= salary
                    and x.get_taxCode() ==status)
        
        return rv


 
print(taxRage_calculator(85000,'MFJ'))