# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangePassword_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePassword_form(object):
    def setupUi(self, ChangePassword_form):
        ChangePassword_form.setObjectName("ChangePassword_form")
        ChangePassword_form.setEnabled(True)
        ChangePassword_form.resize(400, 317)
        self.Name_Form_AddPaymentForm = QtWidgets.QLabel(ChangePassword_form)
        self.Name_Form_AddPaymentForm.setGeometry(QtCore.QRect(10, 10, 381, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Name_Form_AddPaymentForm.setFont(font)
        self.Name_Form_AddPaymentForm.setAlignment(QtCore.Qt.AlignCenter)
        self.Name_Form_AddPaymentForm.setObjectName("Name_Form_AddPaymentForm")
        self.Add_button = QtWidgets.QPushButton(ChangePassword_form)
        self.Add_button.setGeometry(QtCore.QRect(270, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Add_button.setFont(font)
        self.Add_button.setObjectName("Add_button")
        self.label_2 = QtWidgets.QLabel(ChangePassword_form)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Succsess_label = QtWidgets.QLabel(ChangePassword_form)
        self.Succsess_label.setEnabled(False)
        self.Succsess_label.setGeometry(QtCore.QRect(10, 45, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Succsess_label.setFont(font)
        self.Succsess_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Succsess_label.setObjectName("Succsess_label")
        self.Input_password_change = QtWidgets.QLineEdit(ChangePassword_form)
        self.Input_password_change.setGeometry(QtCore.QRect(70, 110, 251, 20))
        self.Input_password_change.setObjectName("Input_password_change")
        self.Input_password_change_2 = QtWidgets.QLineEdit(ChangePassword_form)
        self.Input_password_change_2.setGeometry(QtCore.QRect(70, 170, 251, 20))
        self.Input_password_change_2.setObjectName("Input_password_change_2")
        self.label_3 = QtWidgets.QLabel(ChangePassword_form)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Input_password_change_3 = QtWidgets.QLineEdit(ChangePassword_form)
        self.Input_password_change_3.setGeometry(QtCore.QRect(70, 230, 251, 20))
        self.Input_password_change_3.setObjectName("Input_password_change_3")
        self.label_4 = QtWidgets.QLabel(ChangePassword_form)
        self.label_4.setGeometry(QtCore.QRect(70, 200, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(ChangePassword_form)
        QtCore.QMetaObject.connectSlotsByName(ChangePassword_form)

    def retranslateUi(self, ChangePassword_form):
        _translate = QtCore.QCoreApplication.translate
        ChangePassword_form.setWindowTitle(_translate("ChangePassword_form", "Form"))
        self.Name_Form_AddPaymentForm.setText(_translate("ChangePassword_form", "Сменить пароль"))
        self.Add_button.setText(_translate("ChangePassword_form", "подтвердить"))
        self.label_2.setText(_translate("ChangePassword_form", "Новый пароль:"))
        self.Succsess_label.setText(_translate("ChangePassword_form", "Пароль успешно изменен"))
        self.label_3.setText(_translate("ChangePassword_form", "Повторите новый пароль:"))
        self.label_4.setText(_translate("ChangePassword_form", "Прошлый пароль:"))
