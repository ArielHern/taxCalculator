# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 597)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.salary = QtWidgets.QLabel(self.centralwidget)
        self.salary.setGeometry(QtCore.QRect(10, 60, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.salary.setFont(font)
        self.salary.setObjectName("salary")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.rbSingle = QtWidgets.QRadioButton(self.centralwidget)
        self.rbSingle.setGeometry(QtCore.QRect(390, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.rbSingle.setFont(font)
        self.rbSingle.setObjectName("rbSingle")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbSingle)
        self.rbMarriedFilingJointly = QtWidgets.QRadioButton(self.centralwidget)
        self.rbMarriedFilingJointly.setGeometry(QtCore.QRect(560, 80, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.rbMarriedFilingJointly.setFont(font)
        self.rbMarriedFilingJointly.setObjectName("rbMarriedFilingJointly")
        self.buttonGroup.addButton(self.rbMarriedFilingJointly)
        self.rbQualifiedWindow = QtWidgets.QRadioButton(self.centralwidget)
        self.rbQualifiedWindow.setGeometry(QtCore.QRect(240, 120, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.rbQualifiedWindow.setFont(font)
        self.rbQualifiedWindow.setObjectName("rbQualifiedWindow")
        self.buttonGroup.addButton(self.rbQualifiedWindow)
        self.rbMarriedFillingSingle = QtWidgets.QRadioButton(self.centralwidget)
        self.rbMarriedFillingSingle.setGeometry(QtCore.QRect(390, 120, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.rbMarriedFillingSingle.setFont(font)
        self.rbMarriedFillingSingle.setObjectName("rbMarriedFillingSingle")
        self.buttonGroup.addButton(self.rbMarriedFillingSingle)
        self.rbHeadofHouseHold = QtWidgets.QRadioButton(self.centralwidget)
        self.rbHeadofHouseHold.setGeometry(QtCore.QRect(560, 120, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.rbHeadofHouseHold.setFont(font)
        self.rbHeadofHouseHold.setObjectName("rbHeadofHouseHold")
        self.buttonGroup.addButton(self.rbHeadofHouseHold)
        self.rbAll = QtWidgets.QRadioButton(self.centralwidget)
        self.rbAll.setEnabled(True)
        self.rbAll.setGeometry(QtCore.QRect(240, 80, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.rbAll.setFont(font)
        self.rbAll.setAutoFillBackground(False)
        self.rbAll.setChecked(True)
        self.rbAll.setObjectName("rbAll")
        self.buttonGroup.addButton(self.rbAll)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.txtSalary = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSalary.setGeometry(QtCore.QRect(60, 60, 113, 20))
        self.txtSalary.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txtSalary.setObjectName("txtSalary")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 170, 861, 351))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setStyleSheet("border: 2px solid black; ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.S1 = QtWidgets.QLabel(self.frame)
        self.S1.setGeometry(QtCore.QRect(0, 0, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.S1.setFont(font)
        self.S1.setStyleSheet("border: 1px solid black; ")
        self.S1.setScaledContents(False)
        self.S1.setWordWrap(True)
        self.S1.setObjectName("S1")
        self.S2 = QtWidgets.QLabel(self.frame)
        self.S2.setGeometry(QtCore.QRect(170, 0, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.S2.setFont(font)
        self.S2.setStyleSheet("border: 1px solid black; ")
        self.S2.setWordWrap(True)
        self.S2.setObjectName("S2")
        self.S3 = QtWidgets.QLabel(self.frame)
        self.S3.setGeometry(QtCore.QRect(350, 0, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.S3.setFont(font)
        self.S3.setStyleSheet("border: 1px solid black; ")
        self.S3.setWordWrap(True)
        self.S3.setObjectName("S3")
        self.S4 = QtWidgets.QLabel(self.frame)
        self.S4.setGeometry(QtCore.QRect(520, 0, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.S4.setFont(font)
        self.S4.setStyleSheet("border: 1px solid black; ")
        self.S4.setWordWrap(True)
        self.S4.setObjectName("S4")
        self.S5 = QtWidgets.QLabel(self.frame)
        self.S5.setGeometry(QtCore.QRect(690, 0, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.S5.setFont(font)
        self.S5.setStyleSheet("border: 1px solid black; ")
        self.S5.setWordWrap(True)
        self.S5.setObjectName("S5")
        self.MFJ1 = QtWidgets.QLabel(self.frame)
        self.MFJ1.setGeometry(QtCore.QRect(350, 50, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFJ1.setFont(font)
        self.MFJ1.setStyleSheet("border: 1px solid black; ")
        self.MFJ1.setWordWrap(True)
        self.MFJ1.setObjectName("MFJ1")
        self.S6 = QtWidgets.QLabel(self.frame)
        self.S6.setGeometry(QtCore.QRect(0, 50, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.S6.setFont(font)
        self.S6.setStyleSheet("border: 1px solid black; ")
        self.S6.setScaledContents(False)
        self.S6.setWordWrap(True)
        self.S6.setObjectName("S6")
        self.MFJ3 = QtWidgets.QLabel(self.frame)
        self.MFJ3.setGeometry(QtCore.QRect(690, 50, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFJ3.setFont(font)
        self.MFJ3.setStyleSheet("border: 1px solid black; ")
        self.MFJ3.setWordWrap(True)
        self.MFJ3.setObjectName("MFJ3")
        self.MFJ2 = QtWidgets.QLabel(self.frame)
        self.MFJ2.setGeometry(QtCore.QRect(520, 50, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFJ2.setFont(font)
        self.MFJ2.setStyleSheet("border: 1px solid black; ")
        self.MFJ2.setWordWrap(True)
        self.MFJ2.setObjectName("MFJ2")
        self.S7 = QtWidgets.QLabel(self.frame)
        self.S7.setGeometry(QtCore.QRect(170, 50, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.S7.setFont(font)
        self.S7.setStyleSheet("border: 1px solid black; ")
        self.S7.setWordWrap(True)
        self.S7.setObjectName("S7")
        self.MFJ5 = QtWidgets.QLabel(self.frame)
        self.MFJ5.setGeometry(QtCore.QRect(170, 100, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFJ5.setFont(font)
        self.MFJ5.setStyleSheet("border: 1px solid black; ")
        self.MFJ5.setWordWrap(True)
        self.MFJ5.setObjectName("MFJ5")
        self.MFJ7 = QtWidgets.QLabel(self.frame)
        self.MFJ7.setGeometry(QtCore.QRect(520, 100, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFJ7.setFont(font)
        self.MFJ7.setStyleSheet("border: 1px solid black; ")
        self.MFJ7.setWordWrap(True)
        self.MFJ7.setObjectName("MFJ7")
        self.MFS1 = QtWidgets.QLabel(self.frame)
        self.MFS1.setGeometry(QtCore.QRect(690, 100, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFS1.setFont(font)
        self.MFS1.setStyleSheet("border: 1px solid black; ")
        self.MFS1.setWordWrap(True)
        self.MFS1.setObjectName("MFS1")
        self.MFJ4 = QtWidgets.QLabel(self.frame)
        self.MFJ4.setGeometry(QtCore.QRect(0, 100, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFJ4.setFont(font)
        self.MFJ4.setStyleSheet("border: 1px solid black; ")
        self.MFJ4.setScaledContents(False)
        self.MFJ4.setWordWrap(True)
        self.MFJ4.setObjectName("MFJ4")
        self.MFJ6 = QtWidgets.QLabel(self.frame)
        self.MFJ6.setGeometry(QtCore.QRect(350, 100, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFJ6.setFont(font)
        self.MFJ6.setStyleSheet("border: 1px solid black; ")
        self.MFJ6.setWordWrap(True)
        self.MFJ6.setObjectName("MFJ6")
        self.MFS3 = QtWidgets.QLabel(self.frame)
        self.MFS3.setGeometry(QtCore.QRect(170, 150, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFS3.setFont(font)
        self.MFS3.setStyleSheet("border: 1px solid black; ")
        self.MFS3.setWordWrap(True)
        self.MFS3.setObjectName("MFS3")
        self.MFS5 = QtWidgets.QLabel(self.frame)
        self.MFS5.setGeometry(QtCore.QRect(520, 150, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFS5.setFont(font)
        self.MFS5.setStyleSheet("border: 1px solid black; ")
        self.MFS5.setWordWrap(True)
        self.MFS5.setObjectName("MFS5")
        self.MFS6 = QtWidgets.QLabel(self.frame)
        self.MFS6.setGeometry(QtCore.QRect(690, 150, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFS6.setFont(font)
        self.MFS6.setStyleSheet("border: 1px solid black; ")
        self.MFS6.setWordWrap(True)
        self.MFS6.setObjectName("MFS6")
        self.MFS4 = QtWidgets.QLabel(self.frame)
        self.MFS4.setGeometry(QtCore.QRect(350, 150, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFS4.setFont(font)
        self.MFS4.setStyleSheet("border: 1px solid black; ")
        self.MFS4.setWordWrap(True)
        self.MFS4.setObjectName("MFS4")
        self.MFS2 = QtWidgets.QLabel(self.frame)
        self.MFS2.setGeometry(QtCore.QRect(0, 150, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFS2.setFont(font)
        self.MFS2.setStyleSheet("border: 1px solid black; ")
        self.MFS2.setScaledContents(False)
        self.MFS2.setWordWrap(True)
        self.MFS2.setObjectName("MFS2")
        self.MFS7 = QtWidgets.QLabel(self.frame)
        self.MFS7.setGeometry(QtCore.QRect(0, 200, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.MFS7.setFont(font)
        self.MFS7.setStyleSheet("border: 1px solid black; ")
        self.MFS7.setScaledContents(False)
        self.MFS7.setWordWrap(True)
        self.MFS7.setObjectName("MFS7")
        self.HH4 = QtWidgets.QLabel(self.frame)
        self.HH4.setGeometry(QtCore.QRect(690, 200, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.HH4.setFont(font)
        self.HH4.setStyleSheet("border: 1px solid black; ")
        self.HH4.setWordWrap(True)
        self.HH4.setObjectName("HH4")
        self.HH3 = QtWidgets.QLabel(self.frame)
        self.HH3.setGeometry(QtCore.QRect(520, 200, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.HH3.setFont(font)
        self.HH3.setStyleSheet("border: 1px solid black; ")
        self.HH3.setWordWrap(True)
        self.HH3.setObjectName("HH3")
        self.HH2 = QtWidgets.QLabel(self.frame)
        self.HH2.setGeometry(QtCore.QRect(350, 200, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.HH2.setFont(font)
        self.HH2.setStyleSheet("border: 1px solid black; ")
        self.HH2.setWordWrap(True)
        self.HH2.setObjectName("HH2")
        self.HH1 = QtWidgets.QLabel(self.frame)
        self.HH1.setGeometry(QtCore.QRect(170, 200, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.HH1.setFont(font)
        self.HH1.setStyleSheet("border: 1px solid black; ")
        self.HH1.setWordWrap(True)
        self.HH1.setObjectName("HH1")
        self.HH5 = QtWidgets.QLabel(self.frame)
        self.HH5.setGeometry(QtCore.QRect(0, 250, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.HH5.setFont(font)
        self.HH5.setStyleSheet("border: 1px solid black; ")
        self.HH5.setScaledContents(False)
        self.HH5.setWordWrap(True)
        self.HH5.setObjectName("HH5")
        self.HH6 = QtWidgets.QLabel(self.frame)
        self.HH6.setGeometry(QtCore.QRect(170, 250, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.HH6.setFont(font)
        self.HH6.setStyleSheet("border: 1px solid black; ")
        self.HH6.setWordWrap(True)
        self.HH6.setObjectName("HH6")
        self.QW1 = QtWidgets.QLabel(self.frame)
        self.QW1.setGeometry(QtCore.QRect(520, 250, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.QW1.setFont(font)
        self.QW1.setStyleSheet("border: 1px solid black; ")
        self.QW1.setWordWrap(True)
        self.QW1.setObjectName("QW1")
        self.HH7 = QtWidgets.QLabel(self.frame)
        self.HH7.setGeometry(QtCore.QRect(350, 250, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.HH7.setFont(font)
        self.HH7.setStyleSheet("border: 1px solid black; ")
        self.HH7.setWordWrap(True)
        self.HH7.setObjectName("HH7")
        self.QW2 = QtWidgets.QLabel(self.frame)
        self.QW2.setGeometry(QtCore.QRect(690, 250, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.QW2.setFont(font)
        self.QW2.setStyleSheet("border: 1px solid black; ")
        self.QW2.setWordWrap(True)
        self.QW2.setObjectName("QW2")
        self.QW6 = QtWidgets.QLabel(self.frame)
        self.QW6.setGeometry(QtCore.QRect(520, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.QW6.setFont(font)
        self.QW6.setStyleSheet("border: 1px solid black; ")
        self.QW6.setWordWrap(True)
        self.QW6.setObjectName("QW6")
        self.QW4 = QtWidgets.QLabel(self.frame)
        self.QW4.setGeometry(QtCore.QRect(170, 300, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.QW4.setFont(font)
        self.QW4.setStyleSheet("border: 1px solid black; ")
        self.QW4.setWordWrap(True)
        self.QW4.setObjectName("QW4")
        self.QW3 = QtWidgets.QLabel(self.frame)
        self.QW3.setGeometry(QtCore.QRect(0, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.QW3.setFont(font)
        self.QW3.setStyleSheet("border: 1px solid black; ")
        self.QW3.setScaledContents(False)
        self.QW3.setWordWrap(True)
        self.QW3.setObjectName("QW3")
        self.QW5 = QtWidgets.QLabel(self.frame)
        self.QW5.setGeometry(QtCore.QRect(350, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.QW5.setFont(font)
        self.QW5.setStyleSheet("border: 1px solid black; ")
        self.QW5.setWordWrap(True)
        self.QW5.setObjectName("QW5")
        self.QW7 = QtWidgets.QLabel(self.frame)
        self.QW7.setGeometry(QtCore.QRect(690, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        self.QW7.setFont(font)
        self.QW7.setStyleSheet("border: 1px solid black; ")
        self.QW7.setWordWrap(True)
        self.QW7.setObjectName("QW7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 0, 81, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/money-bag.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1006, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tax Calculator"))
        self.salary.setText(_translate("MainWindow", "Salary "))
        self.label_2.setText(_translate("MainWindow", "Marginal Tax"))
        self.rbSingle.setText(_translate("MainWindow", "Single"))
        self.rbMarriedFilingJointly.setText(_translate("MainWindow", "Married Filing Jointly"))
        self.rbQualifiedWindow.setText(_translate("MainWindow", "Qualified Widow"))
        self.rbMarriedFillingSingle.setText(_translate("MainWindow", "Married Filing Single"))
        self.rbHeadofHouseHold.setText(_translate("MainWindow", "Head of House Hold"))
        self.rbAll.setText(_translate("MainWindow", "All"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.S1.setText(_translate("MainWindow", "code: S, range: $000.00 - $9,700.99                Rate:10% "))
        self.S2.setText(_translate("MainWindow", "code: S, range: $9,701.00 - $39,475.99               Rate:12%  "))
        self.S3.setText(_translate("MainWindow", "code: S, range: $37,476.00 - $84,200.99              Rate:22%  "))
        self.S4.setText(_translate("MainWindow", "code: S, range: $84,201.00 - $160,725.99        Rate:24% "))
        self.S5.setText(_translate("MainWindow", "code: S, range: $160,726.00 - $204,100.99 Rate:32% "))
        self.MFJ1.setText(_translate("MainWindow", "code: MFJ, range: $000.00 - $19,400.99             Rate:10% "))
        self.S6.setText(_translate("MainWindow", "code: S, range: $204,101.00 - $510,300..99          Rate:35%  "))
        self.MFJ3.setText(_translate("MainWindow", "code: MFJ, range: $78,951.00 - $168,400.99 Rate:22% "))
        self.MFJ2.setText(_translate("MainWindow", "code: MFJ, range: $19,401.00 - $78,950.99        Rate:12%  "))
        self.S7.setText(_translate("MainWindow", "code: S, range: $510,301.00 - $9,999,999.99         Rate:37%  "))
        self.MFJ5.setText(_translate("MainWindow", "code: MFJ, range: $321,451.00 - $408,200.99            Rate:32%  "))
        self.MFJ7.setText(_translate("MainWindow", "code: MFJ, range: $612,351.00 - $9,999,999.99  Rate:37%  "))
        self.MFS1.setText(_translate("MainWindow", "code: MFS, range: $000.00 - $9,700.99        Rate:10%  "))
        self.MFJ4.setText(_translate("MainWindow", "code: MFJ, range: $168,401.00 - $321,450.99  Rate:24%  "))
        self.MFJ6.setText(_translate("MainWindow", "code: MFJ, range: $408,201.00 - $612,350.99 Rate:35%  "))
        self.MFS3.setText(_translate("MainWindow", "code: MFS, range: $39,476.00 - $84,200.99              Rate:22%  "))
        self.MFS5.setText(_translate("MainWindow", "code: MFS, range: $160,726.00 - $204,100.99  Rate:32%  "))
        self.MFS6.setText(_translate("MainWindow", "code: MFS, range: $204,101.00 - $306,175.99   Rate:35%  "))
        self.MFS4.setText(_translate("MainWindow", "code: MFS, range: $84,201.00 - $160,725.99        Rate:24%  "))
        self.MFS2.setText(_translate("MainWindow", "code: MFS, range: $9,701.00 - $39,475.99             Rate:12% "))
        self.MFS7.setText(_translate("MainWindow", "code: MFS, range: $306,176.00 - $9,999,999.99  Rate:37%  "))
        self.HH4.setText(_translate("MainWindow", "code: HH, range: $84,201.00 - $160,700.99        Rate:24%  "))
        self.HH3.setText(_translate("MainWindow", "code: HH, range: $52,851.00 - $84,200.99           Rate:22%  "))
        self.HH2.setText(_translate("MainWindow", "code: HH, range: $13,851.00 - $52,850.99            Rate:12%  "))
        self.HH1.setText(_translate("MainWindow", "code: HH, range: $000.00 - $13,850.99               Rate:10%  "))
        self.HH5.setText(_translate("MainWindow", "code: HH, range: $160,701.00 - $204,100.99          Rate:32%  "))
        self.HH6.setText(_translate("MainWindow", "code: HH, range: $204,101.00 - $510,300.99             Rate:35%  "))
        self.QW1.setText(_translate("MainWindow", "code: QW, range: $000.00 - $19,400.99            Rate:10%  "))
        self.HH7.setText(_translate("MainWindow", "code: HH, range: $510,301.00 - $9,999,999.99      Rate:37%  "))
        self.QW2.setText(_translate("MainWindow", "code: QW, range: $19,401.00 - $78,950.99            Rate:12%  "))
        self.QW6.setText(_translate("MainWindow", "code: QW, range: $408,201.00 - $612,350.99        Rate:35% "))
        self.QW4.setText(_translate("MainWindow", "code: QW, range: $168,401.00 - $321,450.99             Rate:24%  "))
        self.QW3.setText(_translate("MainWindow", "code: QW, range: $78,951.00 - $168,400.99            Rate:22%  "))
        self.QW5.setText(_translate("MainWindow", "code:QW, range: $321,451.00 - $408,200.99           Rate:32% "))
        self.QW7.setText(_translate("MainWindow", "code:QW, range: $612,351.00 - $9,999,999.99     Rate:37%  "))
