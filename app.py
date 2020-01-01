from PyQt5 import QtWidgets
# from PyQt5 import QtCore, QtGui, QtWidgets
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
        
        rv = calculator.calculate(salary, status)       
        self.ui.displayTextField.setPlainText(str(rv))
        
        
    def get_status(self):
        if  self.ui.rbSingle.isChecked()==True:
            return 'S'
        elif self.ui.rbMarriedFilingJointly.isChecked()==True:
            return 'MFJ'
        elif self.ui.rbMarriedFillingSingle.isChecked()==True:
            return 'MFS'
        elif self.ui.rbQualifiedWindow.isChecked()==True:
            return 'QF'
        elif self.ui.rbHeadofHouseHold.isChecked()==True:
            return 'HH'





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QMainWindow()
    ui = myApp()
    ui.show()
    sys.exit(app.exec_())