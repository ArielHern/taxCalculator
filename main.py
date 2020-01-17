# In app.py

from PyQt5 import QtWidgets

import sys

from utils.taxrateGUI import Ui_MainWindow
from resource.taxResource import TaxResource



class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cal_btn.clicked.connect(self.calculateTaxes)        
        self.ui.close_btn.clicked.connect(self.close_app)
        self.ui.reset_btn.clicked.connect(self.reset_app)

        self.msg = QtWidgets.QErrorMessage()
        self.msg.setWindowTitle('Error')

    def calculateTaxes(self):
        calculator = TaxResource()
        try:
            salary = int(self.ui.txtSalary.text())
        except ValueError:
            self.msg.showMessage('Enter Annual Salary')
        else:
            status = self.get_status()

            if status == 'All':
                stat = ('S', 'MFJ', 'MFS', 'QW', 'HH')
                for st in stat:
                    code = calculator.calculate(salary, st, True)
                    self.set_color(code[0])
            else:
                code = calculator.calculate(salary, status, True)
                self.set_color(code[0])

    def set_color(self, code):
        
        for label in self.get_labels():
            if code == label.objectName():
                label.setStyleSheet('background:#A9A9A9')

    def get_status(self):
        if self.ui.rbSingle.isChecked():
            return 'S'
        elif self.ui.rbMarriedFilingJointly.isChecked():
            return 'MFJ'
        elif self.ui.rbMarriedFillingSingle.isChecked():
            return 'MFS'
        elif self.ui.rbQualifiedWindow.isChecked():
            return 'QW'
        elif self.ui.rbHeadofHouseHold.isChecked():
            return 'HH'
        elif self.ui.rbAll.isChecked():
            return 'All'

    def close_app(self):
        sys.exit()

    def reset_app(self):        
        self.ui.txtSalary.clear()                
        
        for label in self.get_labels():
            if label.styleSheet() == 'background:#A9A9A9':
                label.setStyleSheet('border: 1px solid black')
            
    def get_labels(self):
        labels = self.findChildren(QtWidgets.QFrame)
        for label in labels:
            yield label
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = myApp()
    ui.show()
    sys.exit(app.exec_())
