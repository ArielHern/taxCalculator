# In app.py

from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from taxrateGUI import Ui_MainWindow
from taxResourceModel import TaxResource



class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calculateTaxes)

    def calculateTaxes(self):
        calculator = TaxResource()
        salary = int(self.ui.txtSalary.text())
        status = self.get_status()
        
        
        # return the code
        rv = calculator.calculate(salary, status,True)        
        code = rv 
        
        # print((code[0]))
        self.set_color(code)
        
        

    def set_color(self,code):
        labels = self.findChildren(QtWidgets.QFrame)
        for label in labels:
             if code[0]==label.objectName():
                 label.setStyleSheet('background:#A9A9A9')
            
        

    def all_label(self):
        children = self.findChildren(QtWidgets.QFrame)
        for child in children:
            print(child.objectName())
        
        


    def get_status(self):
        if  self.ui.rbSingle.isChecked()==True:
            return 'S'
        elif self.ui.rbMarriedFilingJointly.isChecked()==True:
            return 'MFJ'
        elif self.ui.rbMarriedFillingSingle.isChecked()==True:
            return 'MFS'
        elif self.ui.rbQualifiedWindow.isChecked()==True:
            return 'QW'
        elif self.ui.rbHeadofHouseHold.isChecked()==True:
            return 'HH'





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QMainWindow()
    ui = myApp()
    ui.show()
    sys.exit(app.exec_())