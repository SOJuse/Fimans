# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaymentsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PaymentsWindow(object):
    def setupUi(self, PaymentsWindow):
        PaymentsWindow.setObjectName("PaymentsWindow")
        PaymentsWindow.resize(838, 200)
        self.centralwidget = QtWidgets.QWidget(PaymentsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_Mail = QtWidgets.QLabel(self.centralwidget)
        self.Label_Mail.setGeometry(QtCore.QRect(510, 10, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_Mail.setFont(font)
        self.Label_Mail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_Mail.setObjectName("Label_Mail")
        self.NullPayments_label = QtWidgets.QLabel(self.centralwidget)
        self.NullPayments_label.setGeometry(QtCore.QRect(40, 90, 771, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NullPayments_label.setFont(font)
        self.NullPayments_label.setObjectName("NullPayments_label")
        self.AddPayments_button = QtWidgets.QPushButton(self.centralwidget)
        self.AddPayments_button.setGeometry(QtCore.QRect(650, 50, 151, 23))
        self.AddPayments_button.setObjectName("AddPayments_button")
        self.Name_Window_PaymentsWindow = QtWidgets.QLabel(self.centralwidget)
        self.Name_Window_PaymentsWindow.setEnabled(True)
        self.Name_Window_PaymentsWindow.setGeometry(QtCore.QRect(30, 10, 231, 70))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(40)
        self.Name_Window_PaymentsWindow.setFont(font)
        self.Name_Window_PaymentsWindow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Name_Window_PaymentsWindow.setObjectName("Name_Window_PaymentsWindow")
        self.Back_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_button.setGeometry(QtCore.QRect(740, 10, 75, 23))
        self.Back_button.setObjectName("Back_button")
        PaymentsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PaymentsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menubar.setObjectName("menubar")
        PaymentsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PaymentsWindow)
        self.statusbar.setObjectName("statusbar")
        PaymentsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PaymentsWindow)
        QtCore.QMetaObject.connectSlotsByName(PaymentsWindow)

    def retranslateUi(self, PaymentsWindow):
        _translate = QtCore.QCoreApplication.translate
        PaymentsWindow.setWindowTitle(_translate("PaymentsWindow", "MainWindow"))
        self.Label_Mail.setText(_translate("PaymentsWindow", "Example@mail.ru"))
        self.NullPayments_label.setText(_translate("PaymentsWindow", "У Вас еще нет запланированных платежей"))
        self.AddPayments_button.setText(_translate("PaymentsWindow", "Добавить платеж"))
        self.Name_Window_PaymentsWindow.setText(_translate("PaymentsWindow", "Payments"))
        self.Back_button.setText(_translate("PaymentsWindow", "Назад"))