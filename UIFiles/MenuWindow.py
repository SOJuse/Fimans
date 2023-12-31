# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(841, 303)
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_Mail = QtWidgets.QLabel(self.centralwidget)
        self.Label_Mail.setGeometry(QtCore.QRect(520, 10, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_Mail.setFont(font)
        self.Label_Mail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_Mail.setObjectName("Label_Mail")
        self.LogOut_button = QtWidgets.QPushButton(self.centralwidget)
        self.LogOut_button.setGeometry(QtCore.QRect(750, 10, 75, 23))
        self.LogOut_button.setObjectName("LogOut_button")
        self.History_button = QtWidgets.QPushButton(self.centralwidget)
        self.History_button.setGeometry(QtCore.QRect(30, 90, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.History_button.setFont(font)
        self.History_button.setObjectName("History_button")
        self.Budget_button = QtWidgets.QPushButton(self.centralwidget)
        self.Budget_button.setGeometry(QtCore.QRect(230, 90, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Budget_button.setFont(font)
        self.Budget_button.setObjectName("Budget_button")
        self.Settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.Settings_button.setGeometry(QtCore.QRect(630, 90, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Settings_button.setFont(font)
        self.Settings_button.setObjectName("Settings_button")
        self.Remind_label = QtWidgets.QLabel(self.centralwidget)
        self.Remind_label.setGeometry(QtCore.QRect(40, 170, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.Remind_label.setFont(font)
        self.Remind_label.setObjectName("Remind_label")
        self.Payments_button = QtWidgets.QPushButton(self.centralwidget)
        self.Payments_button.setGeometry(QtCore.QRect(430, 90, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Payments_button.setFont(font)
        self.Payments_button.setObjectName("Payments_button")
        self.Name_Window_MenuWindow = QtWidgets.QLabel(self.centralwidget)
        self.Name_Window_MenuWindow.setEnabled(True)
        self.Name_Window_MenuWindow.setGeometry(QtCore.QRect(40, 10, 141, 70))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(40)
        self.Name_Window_MenuWindow.setFont(font)
        self.Name_Window_MenuWindow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Name_Window_MenuWindow.setObjectName("Name_Window_MenuWindow")
        self.NullRemind_label = QtWidgets.QLabel(self.centralwidget)
        self.NullRemind_label.setGeometry(QtCore.QRect(40, 220, 771, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NullRemind_label.setFont(font)
        self.NullRemind_label.setObjectName("NullRemind_label")
        MenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 21))
        self.menubar.setObjectName("menubar")
        MenuWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuWindow)
        self.statusbar.setObjectName("statusbar")
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "MainWindow"))
        self.Label_Mail.setText(_translate("MenuWindow", "Example@mail.ru"))
        self.LogOut_button.setText(_translate("MenuWindow", "Выйти"))
        self.History_button.setText(_translate("MenuWindow", "История операций"))
        self.Budget_button.setText(_translate("MenuWindow", "Бюджеты"))
        self.Settings_button.setText(_translate("MenuWindow", "Настройки"))
        self.Remind_label.setText(_translate("MenuWindow", "Предстоящие платежи:"))
        self.Payments_button.setText(_translate("MenuWindow", "Предстоящие платежи"))
        self.Name_Window_MenuWindow.setText(_translate("MenuWindow", "Menu"))
        self.NullRemind_label.setText(_translate("MenuWindow", "У Вас нет предстоящих платежей"))
