# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(650, 244)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Name_Window_SettingsWindow = QtWidgets.QLabel(self.centralwidget)
        self.Name_Window_SettingsWindow.setEnabled(True)
        self.Name_Window_SettingsWindow.setGeometry(QtCore.QRect(30, 10, 181, 70))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(40)
        self.Name_Window_SettingsWindow.setFont(font)
        self.Name_Window_SettingsWindow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Name_Window_SettingsWindow.setObjectName("Name_Window_SettingsWindow")
        self.Label_Mail = QtWidgets.QLabel(self.centralwidget)
        self.Label_Mail.setGeometry(QtCore.QRect(330, 20, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_Mail.setFont(font)
        self.Label_Mail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_Mail.setObjectName("Label_Mail")
        self.Back_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_button.setGeometry(QtCore.QRect(560, 20, 75, 23))
        self.Back_button.setObjectName("Back_button")
        self.ChangePassword_button = QtWidgets.QPushButton(self.centralwidget)
        self.ChangePassword_button.setGeometry(QtCore.QRect(30, 90, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ChangePassword_button.setFont(font)
        self.ChangePassword_button.setObjectName("ChangePassword_button")
        self.ChangeLogin_button = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeLogin_button.setGeometry(QtCore.QRect(30, 140, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ChangeLogin_button.setFont(font)
        self.ChangeLogin_button.setObjectName("ChangeLogin_button")
        SettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        SettingsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "MainWindow"))
        self.Name_Window_SettingsWindow.setText(_translate("SettingsWindow", "Settings"))
        self.Label_Mail.setText(_translate("SettingsWindow", "Example@mail.ru"))
        self.Back_button.setText(_translate("SettingsWindow", "Назад"))
        self.ChangePassword_button.setText(_translate("SettingsWindow", "Сменить пароль"))
        self.ChangeLogin_button.setText(_translate("SettingsWindow", "Сменить логин"))
