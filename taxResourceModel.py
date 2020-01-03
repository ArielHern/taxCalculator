# In TaxResource

from taxModel import TaxModel,TaxRange

class TaxResource:

        taxModel_2020_S = TaxModel(2020, 'S', 'Single')
        taxModel_2020_MFJ = TaxModel(2020, 'MFJ', 'Married Filing Jointly')        
        taxModel_2020_MFS = TaxModel(2020, 'MFS', 'Married Filing Separately')
        taxModel_2020_HH = TaxModel(2020, 'HH', 'Head of Household')
        taxModel_2020_QW = TaxModel(2020, 'QW', 'Qualified Widow(er)')
        taxrange = []

        # single
        taxrange.append(TaxRange.from_model(taxModel_2020_S,0, 9700.99, 0.1,"S1"))
        taxrange.append(TaxRange.from_model(taxModel_2020_S, 9701, 39475.99,0.12,'S2'))
        taxrange.append(TaxRange.from_model(taxModel_2020_S, 39476, 84200.99,0.22,'S3'))
        taxrange.append(TaxRange.from_model(taxModel_2020_S, 84201, 160725.99,0.24,'S4'))
        taxrange.append(TaxRange.from_model(taxModel_2020_S, 160726, 204100.99,0.32,'S5'))
        taxrange.append(TaxRange.from_model(taxModel_2020_S, 204101, 510300.99,0.35,'S6'))
        taxrange.append(TaxRange.from_model(taxModel_2020_S, 510301, 9999999.99,0.37,'S6'))


        # Married, filing jointly
        taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 0 ,19400.99 ,.1,'MFJ1'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 19401, 78950.99, .12, 'MFJ2'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 78951 ,168400.99 ,.22,'MFJ3'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 168401,321450.99 ,.24,'MFJ4'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 321451 ,408200.99 ,.32,'MFJ5'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 408201,612350.99 ,.35,'MFJ6'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFJ, 612351 ,9999999.99 ,.37,'MFJ7'))

        # Married, filing separately
        taxrange.append(TaxRange.from_model(taxModel_2020_MFS,0,9700.99,.1,'MFS1'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFS,9701,39475.99,.12,'MFS2'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFS,39476,84200.99,.22,'MFS3'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFS,84201,160725.99,.24,'MFS4'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFS,160726,204100.99,.32,'MFS5'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFS,204101,306175.99,.35,'MFS6'))
        taxrange.append(TaxRange.from_model(taxModel_2020_MFS,306176,9999999.99,.37,'MFS7'))


        #Head of household
        taxrange.append(TaxRange.from_model(taxModel_2020_HH,0, 14100.99,.1,'HH1'))
        taxrange.append(TaxRange.from_model(taxModel_2020_HH,14101,53700.99,.12,'HH2'))
        taxrange.append(TaxRange.from_model(taxModel_2020_HH,53701,85500.99,.22,'HH3'))
        taxrange.append(TaxRange.from_model(taxModel_2020_HH,85501,16300.99,.24,'HH4'))
        taxrange.append(TaxRange.from_model(taxModel_2020_HH,163301,207350.99,.32,'HH5'))
        taxrange.append(TaxRange.from_model(taxModel_2020_HH,207351,518400.99,.35,'HH6'))
        taxrange.append(TaxRange.from_model(taxModel_2020_HH,518401,9999999.99,.37,'HH7'))

        # 'QW', 'Qualified Widow(er)'
        taxrange.append(TaxRange.from_model(taxModel_2020_QW, 0 ,19400.99 ,.1,'QW1'))
        taxrange.append(TaxRange.from_model(taxModel_2020_QW, 19401, 78950.99, .12, 'QW2'))
        taxrange.append(TaxRange.from_model(taxModel_2020_QW, 78951 ,168400.99 ,.22,'QW3'))
        taxrange.append(TaxRange.from_model(taxModel_2020_QW, 168401,321450.99 ,.24,'QW4'))
        taxrange.append(TaxRange.from_model(taxModel_2020_QW, 321451 ,408200.99 ,.32,'QW5'))
        taxrange.append(TaxRange.from_model(taxModel_2020_QW, 408201,612350.99 ,.35,'QW6'))
        taxrange.append(TaxRange.from_model(taxModel_2020_QW, 612351 ,9999999.99 ,.37,'QW7'))


        
        def calculate(self,salary, status,code=False):
                if code is False:
                        try:
                                rv = tuple(x for x in self.taxrange if x.get_endSalary() >= salary and x.get_startSalary() <= salary
                                and x.get_taxCode() ==status)
                                        
                        except:
                                return ('Did you enter $ and correct status?')
                        else:
                                return rv
                else:
                         rv =  list(x.get_code() for x in self.taxrange if x.get_endSalary() >= salary and x.get_startSalary() <= salary
                                and x.get_taxCode() ==status)
                         return rv
               
       

        
                
        

 
