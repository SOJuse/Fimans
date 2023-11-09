# Импортируем библиотеки
import sys
import datetime as dt
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
# Импортируем UI классы
from UIFiles.LoginWindow import Ui_Login_Window
from UIFiles.RegistrationWindow import Ui_Registration_Window
from UIFiles.MenuWindow import Ui_MenuWindow
from UIFiles.HistoryWindow import Ui_HistoryWindow
from UIFiles.AddPayment_form import Ui_AddPayment_form
from UIFiles.PaymentsWindow import Ui_PaymentsWindow
from UIFiles.AddPayments_form import Ui_AddPayments_form
from UIFiles.SettingsWindow import Ui_SettingsWindow
from UIFiles.ChangePassword_form import Ui_ChangePassword_form
from UIFiles.ChangeLogin_form import Ui_ChangeLogin_form
from UIFiles.BudgetsWindow import Ui_BudgetsWindow
from UIFiles.Graphics_form import Ui_GraphicsFrom
# Импортируем функции из других кодов
from Graphics_matpotlib import *
from CRUD import *


# Окно логина
class MyWidget(QMainWindow, Ui_Login_Window):
    def __init__(self):
        super().__init__()
        self.menu = None
        self.values = None
        self.flag = None
        self.setupUi(self)
        self.Button_to_RegistrationForm.clicked.connect(self.To_Registration)
        self.Button_SignIn_1.clicked.connect(self.Authorization)
        self.ShowPassword_radioButton.toggled.connect(self.ShowPassword_switch)
        self.registration = RegistrationWindow(self)
        self.menu = MenuWindow(self)
        self.id = None

    def To_Menu(self):
        self.menu.show()
        self.hide()

    def To_Registration(self):
        self.Clear_Input()
        self.registration.show()
        self.hide()

    def ShowPassword_switch(self):
        if self.ShowPassword_radioButton.isChecked():
            self.Input_password_autorization.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.Input_password_autorization.setEchoMode(QtWidgets.QLineEdit.Password)

    def Clear_Input(self):
        self.Input_mail_autorization.clear()
        self.Input_password_autorization.clear()
        self.Exception_WrongDataLogin.setVisible(False)

    def Authorization(self):
        self.flag = False
        mail = self.Input_mail_autorization.text()
        password = self.Input_password_autorization.text()
        data = Read_Login_db()
        for row in data:
            if mail == str(row[1]) and password == str(row[2]):
                self.flag = True
                self.values = row
                self.menu.Start_work(self.values)
                self.id = row[0]
                break
        if self.flag:
            self.Clear_Input()
            self.To_Menu()
        else:
            self.Exception_WrongDataLogin.setVisible(True)

    def SendValues(self):
        return self.values


# Окно регистрации
class RegistrationWindow(QMainWindow, Ui_Registration_Window):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.Button_to_AutorizationForm.clicked.connect(self.To_Login)
        self.Button_SignUp_1.clicked.connect(self.Registration)

    def Registration(self):
        self.Exception_WrongPasswordConfirm.setVisible(False)
        local_mail = self.Input_mail_registration.text()
        local_password = self.Input_password_registration.text()
        local_password_confirm = self.Input_password_registration_2.text()
        data = Read_Login_db()
        if any(local_mail == row[1] for row in data):
            self.Exception_WrongPasswordConfirm.setText('Аккаунт с таким email уже зарегистрирован')
            self.Exception_WrongPasswordConfirm.setVisible(True)
        elif local_password == local_password_confirm:
            Write_Login_db(local_mail, local_password)
            self.Exception_WrongPasswordConfirm.setText('Регистрация прошла успешно')
            self.Exception_WrongPasswordConfirm.setVisible(True)
        else:
            self.Exception_WrongPasswordConfirm.setText('Пароли не совпадают')
            self.Exception_WrongPasswordConfirm.setVisible(True)

    def To_Login(self):
        self.Clear_Input()
        self.parent.show()
        self.hide()

    def Clear_Input(self):
        self.Input_mail_registration.clear()
        self.Input_password_registration.clear()
        self.Input_password_registration_2.clear()
        self.Exception_WrongPasswordConfirm.setVisible(False)


# Окно главного меню
class MenuWindow(QMainWindow, Ui_MenuWindow):
    def __init__(self, parent):
        super().__init__()
        self.labels = None
        self.paymentsData = None
        self.id = None
        self.mail = None
        self.password = None
        self.parent = parent
        self.setupUi(self)
        self.LogOut_button.clicked.connect(self.To_Login)
        self.history = HistoryWindow(self)
        self.payments = PaymentsWindow(self)
        self.settings = SettingsWindow(self)
        self.budgets = BudgetsWindow(self)
        self.History_button.clicked.connect(self.To_History)
        self.Payments_button.clicked.connect(self.To_Payments)
        self.Settings_button.clicked.connect(self.To_Settings)
        self.Budget_button.clicked.connect(self.To_Budgets)

    def To_History(self):
        self.history.Start_work([self.id, self.mail, self.password])
        self.history.show()
        self.hide()

    def To_Settings(self):
        self.settings.Start_work([self.id, self.mail, self.password])
        self.settings.show()
        self.hide()

    def To_Budgets(self):
        self.budgets.Start_work([self.id, self.mail, self.password])
        self.budgets.show()
        self.hide()

    def To_Login(self):
        self.parent.show()
        self.hide()

    def To_Payments(self):
        self.payments.Start_work([self.id, self.mail, self.password])
        self.payments.show()
        self.hide()

    def Start_work(self, values):
        self.id, self.mail, self.password = values
        self.Label_Mail.setText(self.mail)
        self.paymentsData = Read_Payments_db(self.id)
        self.paymentsData = sorted(self.paymentsData, key=lambda x: dt.datetime.strptime(x[1], '%d.%m.%Y'),
                                   reverse=True)
        self.labels = {}
        font = QtGui.QFont()
        font.setPointSize(14)
        if len(self.paymentsData) != 0:
            self.resize(841, 300 + 40 * (len(self.paymentsData) - 1))
            self.NullRemind_label.setText(
                f'{self.paymentsData[0][1]}  {self.paymentsData[0][2]}  {self.paymentsData[0][3]}₽')
            for i in range(1, len(self.paymentsData)):
                self.labels["label" + str(i)] = QtWidgets.QLabel(self.centralwidget)
                self.labels["label" + str(i)].setGeometry(QtCore.QRect(40, 220 + 40 * i, 771, 31))
                self.labels["label" + str(i)].setFont(font)
                self.labels["label" + str(i)].setText(
                    f'{self.paymentsData[i][1]}  {self.paymentsData[i][2]}  {self.paymentsData[i][3]}₽')
        print(self.paymentsData)
        print(values)


# Окно истории платежей
class HistoryWindow(QMainWindow, Ui_HistoryWindow):
    def __init__(self, parent):
        super().__init__()
        self.labels = None
        self.historyData = None
        self.addPayment = None
        self.id = None
        self.mail = None
        self.password = None
        self.parent = parent
        self.setupUi(self)
        self.Back_button.clicked.connect(self.To_Menu)
        self.AddPayments_button.clicked.connect(self.Open_AddPayment)

    def To_Menu(self):
        self.parent.show()
        self.hide()
        self.Clear()

    def Start_work(self, values):
        self.id, self.mail, self.password = values
        self.Label_Mail.setText(self.mail)
        self.historyData = Read_History_db(self.id)
        self.historyData = sorted(self.historyData, key=lambda x: dt.datetime.strptime(x[1], '%d.%m.%Y'), reverse=True)
        self.labels = {}
        font = QtGui.QFont()
        font.setPointSize(14)
        if len(self.historyData) != 0:
            self.resize(832, 200 + 40 * (len(self.historyData) - 1))
            self.NullHistory_label.setText(
                f'{self.historyData[0][1]}  {self.historyData[0][2]}  {self.historyData[0][3]}₽')
            for i in range(1, len(self.historyData)):
                self.labels["label" + str(i)] = QtWidgets.QLabel(self.centralwidget)
                self.labels["label" + str(i)].setGeometry(QtCore.QRect(40, 90 + 40 * i, 771, 31))
                self.labels["label" + str(i)].setFont(font)
                self.labels["label" + str(i)].setText(
                    f'{self.historyData[i][1]}  {self.historyData[i][2]}  {self.historyData[i][3]}₽')
        print(self.historyData)
        print(values)

    def Open_AddPayment(self):
        self.addPayment = AddPaymentForm(self, self.id)
        self.addPayment.show()

    def Clear(self):
        for i in self.labels.keys():
            self.labels[i].setVisible(False)


# Окно формы для добавления платежей
class AddPaymentForm(QMainWindow, Ui_AddPayment_form):
    def __init__(self, parent, id):
        super().__init__()
        self.price = None
        self.category = None
        self.date = None
        self.id = id
        self.setupUi(self)
        self.parent = parent
        self.Categoty_box.addItem('Зарплата и выплаты сотрудникам')
        self.Categoty_box.addItem('Аренда и коммунальные услуги')
        self.Categoty_box.addItem('Поставщики и закупки')
        self.Categoty_box.addItem('Налоги и сборы')
        self.Categoty_box.addItem('Финансовые услуги')
        self.Categoty_box.addItem('Транспорт и доставка')
        self.Categoty_box.addItem('Обслуживание и ремонт')
        self.Categoty_box.addItem('Информационные технологии')
        self.Categoty_box.addItem('Страхование')
        self.Add_button.clicked.connect(self.add)
        self.Wrong_label.setVisible(False)

    def add(self):
        self.date = self.date_dateEdit.date().toPyDate()
        self.category = self.Categoty_box.currentText()
        self.price = self.Price_Box.value()
        Write_History_db(self.id, self.date.strftime('%d.%m.%Y'), self.category, self.price)
        self.Wrong_label.setVisible(True)


# Окно предстоящих платежей
class PaymentsWindow(QMainWindow, Ui_PaymentsWindow):
    def __init__(self, parent):
        super().__init__()
        self.labels = None
        self.paymentsData = None
        self.addPayments = None
        self.id = None
        self.mail = None
        self.password = None
        self.parent = parent
        self.setupUi(self)
        self.Back_button.clicked.connect(self.To_Menu)
        self.AddPayments_button.clicked.connect(self.Open_AddPayment)

    def Open_AddPayment(self):
        self.addPayments = AddPaymentsForm(self, self.id)
        self.addPayments.show()

    def Clear(self):
        for i in self.labels.keys():
            self.labels[i].setVisible(False)

    def To_Menu(self):
        self.parent.show()
        self.hide()
        self.Clear()

    def Start_work(self, values):
        self.id, self.mail, self.password = values
        self.Label_Mail.setText(self.mail)
        self.paymentsData = Read_Payments_db(self.id)
        self.paymentsData = sorted(self.paymentsData, key=lambda x: dt.datetime.strptime(x[1], '%d.%m.%Y'),
                                   reverse=True)
        self.labels = {}
        font = QtGui.QFont()
        font.setPointSize(14)
        if len(self.paymentsData) != 0:
            self.resize(832, 200 + 40 * (len(self.paymentsData) - 1))
            self.NullPayments_label.setText(
                f'{self.paymentsData[0][1]}  {self.paymentsData[0][2]}  {self.paymentsData[0][3]}₽')
            for i in range(1, len(self.paymentsData)):
                self.labels["label" + str(i)] = QtWidgets.QLabel(self.centralwidget)
                self.labels["label" + str(i)].setGeometry(QtCore.QRect(40, 90 + 40 * i, 771, 31))
                self.labels["label" + str(i)].setFont(font)
                self.labels["label" + str(i)].setText(
                    f'{self.paymentsData[i][1]}  {self.paymentsData[i][2]}  {self.paymentsData[i][3]}₽')
        print(self.paymentsData)
        print(values)


# Окно формы для добавления предстоящих платежей
class AddPaymentsForm(QMainWindow, Ui_AddPayments_form):
    def __init__(self, parent, id):
        super().__init__()
        self.price = None
        self.category = None
        self.date = None
        self.id = id
        self.setupUi(self)
        self.parent = parent
        self.Categoty_box.addItem('Зарплата и выплаты сотрудникам')
        self.Categoty_box.addItem('Аренда и коммунальные услуги')
        self.Categoty_box.addItem('Поставщики и закупки')
        self.Categoty_box.addItem('Налоги и сборы')
        self.Categoty_box.addItem('Финансовые услуги')
        self.Categoty_box.addItem('Транспорт и доставка')
        self.Categoty_box.addItem('Обслуживание и ремонт')
        self.Categoty_box.addItem('Информационные технологии')
        self.Categoty_box.addItem('Страхование')
        self.Add_button.clicked.connect(self.add)
        self.Wrong_label.setVisible(False)

    def add(self):
        self.date = self.date_dateEdit.date().toPyDate()
        self.category = self.Categoty_box.currentText()
        self.price = self.Price_Box.value()
        Write_Payments_db(self.id, self.date.strftime('%d.%m.%Y'), self.category, self.price)
        self.Wrong_label.setVisible(True)


# Окно настроек
class SettingsWindow(QMainWindow, Ui_SettingsWindow):
    def __init__(self, parent):
        super().__init__()
        self.changeLogin = None
        self.changePassword = None
        self.id = None
        self.mail = None
        self.password = None
        self.parent = parent
        self.setupUi(self)
        self.ChangeLogin_button.clicked.connect(self.Open_ChangeLogin)
        self.ChangePassword_button.clicked.connect(self.Open_ChangePassword)
        self.Back_button.clicked.connect(self.To_Menu)

    def Start_work(self, values):
        self.id, self.mail, self.password = values
        self.Label_Mail.setText(self.mail)

    def To_Menu(self):
        self.parent.show()
        self.hide()

    def Open_ChangePassword(self):
        self.changePassword = ChangePasswordForm(self, self.mail, self.password, self.id)
        self.changePassword.show()

    def Open_ChangeLogin(self):
        self.changeLogin = ChangeLoginForm(self, self.mail, self.password, self.id)
        self.changeLogin.show()


# Окно формы для изменения пароля
class ChangePasswordForm(QMainWindow, Ui_ChangePassword_form):
    def __init__(self, parent, mail, password, id):
        super().__init__()
        self.newPassword1 = None
        self.newPassword2 = None
        self.newPassword3 = None
        self.parent = parent
        self.mail = mail
        self.password = password
        self.id = id
        self.setupUi(self)
        self.Add_button.clicked.connect(self.Change)
        self.Succsess_label.setVisible(False)

    def Change(self):
        self.Succsess_label.setVisible(False)
        self.newPassword1 = self.Input_password_change.text()
        self.newPassword2 = self.Input_password_change_2.text()
        self.newPassword3 = self.Input_password_change_3.text()
        if self.newPassword3 != self.password:
            self.Succsess_label.setText('Неверный пароль')
            self.Succsess_label.setVisible(True)
        elif self.newPassword1 == self.newPassword2:
            Change_Login_db(self.id, self.mail, self.newPassword1)
            self.Succsess_label.setText('Пароль успешно изменен')
            self.Succsess_label.setVisible(True)
        elif self.newPassword1 != self.newPassword2:
            self.Succsess_label.setText('Пароли не совпадают')
            self.Succsess_label.setVisible(True)


# Окно формы для изменения логина
class ChangeLoginForm(QMainWindow, Ui_ChangeLogin_form):
    def __init__(self, parent, mail, password, id):
        super().__init__()
        self.parent = parent
        self.newLogin1 = None
        self.newLogin2 = None
        self.mail = mail
        self.password = password
        self.id = id
        self.setupUi(self)
        self.Add_button.clicked.connect(self.Change)
        self.Succsess_label.setVisible(False)

    def Change(self):
        self.Succsess_label.setVisible(False)
        self.newLogin1 = self.Input_login_change.text()
        self.newLogin2 = self.Input_login_change_2.text()
        if self.newLogin2 != self.mail:
            self.Succsess_label.setText('Неверный логин')
            self.Succsess_label.setVisible(True)
        else:
            Change_Login_db(self.id, self.newLogin1, self.password)
            self.Succsess_label.setText('Логин успешно изменен')
            self.Succsess_label.setVisible(True)


# Окно бюджетов и графиков
class BudgetsWindow(QMainWindow, Ui_BudgetsWindow):
    def __init__(self, parent):
        super().__init__()
        self.pushButton1 = None
        self.labels = None
        self.buttons = None
        self.pixmap = None
        self.data = None
        self.first_image = None
        self.categories = None
        self.graphics = None
        self.id = None
        self.mail = None
        self.password = None
        self.paths = None
        self.parent = parent
        self.setupUi(self)
        self.Back_button.clicked.connect(self.To_Menu)

    def To_Menu(self):
        self.parent.show()
        self.hide()

    def Open_Graphics(self, index):
        if index:
            index = self.categories.index(index) + 1
        else:
            index = 1
        print(index)
        self.graphics = GraphicsForm(self, self.paths[index])
        # self.graphics.Clear()
        self.graphics.show()

    def Start_work(self, values):
        self.id, self.mail, self.password = values
        self.data = Read_History_db(self.id)
        if len(self.data) > 0:
            self.paths, self.categories = Create_Graphics(self.data)
            Write_paths_graphics(self.paths)
            self.Label_Mail.setText(self.mail)
            self.paths = Read_paths_graphics()
            self.pixmap = QPixmap(self.paths[0])
            self.first_image = QtWidgets.QLabel(self.centralwidget)
            self.first_image.setPixmap(self.pixmap)
            self.first_image.setGeometry(QtCore.QRect(410, 40, 400, 240))
        if len(self.data) > 1:
            self.buttons = {}
            self.labels = {}
            font = QtGui.QFont()
            font.setPointSize(12)
            self.NullRemind_label.setText(self.categories[0])
            self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton1.setGeometry(QtCore.QRect(330, 80, 75, 23))
            self.pushButton1.setObjectName("pushButton1")
            self.pushButton1.setText("График")
            self.pushButton1.clicked.connect(self.Open_Graphics)
            i = 1
            for cat in self.categories[1:]:
                self.labels["label" + str(i)] = QtWidgets.QLabel(self.centralwidget)
                self.labels["label" + str(i)].setGeometry(QtCore.QRect(20, 80 + 40 * i, 391, 31))
                self.labels["label" + str(i)].setFont(font)
                self.labels["label" + str(i)].setText(cat)
                self.buttons["pushButton" + str(i + 1)] = QtWidgets.QPushButton(self.centralwidget)
                self.buttons["pushButton" + str(i + 1)].setGeometry(QtCore.QRect(330, 80 + 40 * i, 75, 23))
                self.buttons["pushButton" + str(i + 1)].setText("График")
                self.buttons["pushButton" + str(i + 1)].clicked.connect(
                    lambda ch, ind=cat: self.Open_Graphics(ind))
                i += 1


# Окно формы для вывода графиков бюджетов
class GraphicsForm(QMainWindow, Ui_GraphicsFrom):
    def __init__(self, parent, path):
        super().__init__()
        self.path = path
        self.parent = parent
        self.setupUi(self)
        print(self.path)
        self.pixmap = QPixmap(path)
        self.first_image = QtWidgets.QLabel(self)
        self.first_image.setPixmap(self.pixmap)
        self.first_image.setGeometry(QtCore.QRect(0, 0, 801, 601))

    def Clear(self):
        pass


def excepthook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
