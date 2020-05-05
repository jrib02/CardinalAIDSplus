# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(341, 481)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("CardinalAIDS-icofile.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("QWidget {\n"
"    background: red;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 341, 481))
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 341, 481))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget{\n"
"    /*font: 10pt \"Segoe UI\";*/\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 10px solid yellow;\n"
"    position: absolute;\n"
"}\n"
"QTabWidget>QWidget>QWidget{background: white;}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: red;\n"
"    font:10pt \"Segoe UI\" ; \n"
"}\n"
"QTabWidget::tab-bar {\n"
"    alignment: right;\n"
"    border: 2px solid red;\n"
"    border-bottom-color: yellow; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 10px;\n"
"    padding: 10px;\n"
"}\n"
"QTabBar::tab:hover {\n"
"    background: red;\n"
"    font: black;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background: yellow;\n"
"    color: black;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    background: red;\n"
"    color: white;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.loginTab = QtWidgets.QWidget()
        self.loginTab.setObjectName("loginTab")
        self.loginBtn = QtWidgets.QPushButton(self.loginTab)
        self.loginBtn.setGeometry(QtCore.QRect(50, 370, 261, 31))
        self.loginBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    border: 1px solid white;\n"
"    border-radius: 15px;\n"
"    background-color: red;\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    text-decoration: underline;\n"
"    border: 1px solid white;\n"
"    border-radius: 15px;\n"
"    background-color: red;\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: red;\n"
"    font: Bold 10pt \"Segoe UI\";\n"
"    border: 1px solid red;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton::focus{\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    text-decoration: underline;\n"
"    border: 1px solid white;\n"
"    border-radius: 15px;\n"
"    background-color: red;\n"
"    min-width: 80px;\n"
"}")
        self.loginBtn.setCheckable(False)
        self.loginBtn.setAutoDefault(True)
        self.loginBtn.setObjectName("loginBtn")
        self.logo = QtWidgets.QLabel(self.loginTab)
        self.logo.setGeometry(QtCore.QRect(35, 10, 281, 271))
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.RichText)
        self.logo.setPixmap(QtGui.QPixmap("CardinalAIDS-full.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.userText = QtWidgets.QLineEdit(self.loginTab)
        self.userText.setGeometry(QtCore.QRect(50, 290, 261, 31))
        self.userText.setStyleSheet("QLineEdit{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.userText.setObjectName("userText")
        self.passText = QtWidgets.QLineEdit(self.loginTab)
        self.passText.setGeometry(QtCore.QRect(50, 330, 261, 31))
        self.passText.setStyleSheet("QLineEdit{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.passText.setObjectName("passText")
        self.incorrrectLbl = QtWidgets.QLabel(self.loginTab)
        self.incorrrectLbl.setGeometry(QtCore.QRect(50, 400, 261, 16))
        self.incorrrectLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    color: red;\n"
"}")
        self.incorrrectLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.incorrrectLbl.setObjectName("incorrrectLbl")
        self.tabWidget.addTab(self.loginTab, "")
        self.adminTab = QtWidgets.QWidget()
        self.adminTab.setObjectName("adminTab")
        self.loginAdBtn = QtWidgets.QPushButton(self.adminTab)
        self.loginAdBtn.setGeometry(QtCore.QRect(50, 370, 261, 31))
        self.loginAdBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    border: 1px solid white;\n"
"    border-radius: 15px;\n"
"    background-color: red;\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    text-decoration: underline;\n"
"    border: 1px solid white;\n"
"    border-radius: 15px;\n"
"    background-color: red;\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:pressed {\n"
"    color: red;\n"
"    font: Bold 10pt \"Segoe UI\";\n"
"    border: 1px solid red;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton::focus{\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    text-decoration: underline;\n"
"    border: 1px solid white;\n"
"    border-radius: 15px;\n"
"    background-color: red;\n"
"    min-width: 80px;\n"
"}")
        self.loginAdBtn.setCheckable(False)
        self.loginAdBtn.setAutoDefault(True)
        self.loginAdBtn.setObjectName("loginAdBtn")
        self.logoAdmin = QtWidgets.QLabel(self.adminTab)
        self.logoAdmin.setGeometry(QtCore.QRect(35, 10, 281, 271))
        self.logoAdmin.setText("")
        self.logoAdmin.setTextFormat(QtCore.Qt.RichText)
        self.logoAdmin.setPixmap(QtGui.QPixmap("CardinalAIDS-full.jpg"))
        self.logoAdmin.setScaledContents(True)
        self.logoAdmin.setObjectName("logoAdmin")
        self.userAdText = QtWidgets.QLineEdit(self.adminTab)
        self.userAdText.setGeometry(QtCore.QRect(50, 290, 261, 31))
        self.userAdText.setStyleSheet("QLineEdit{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.userAdText.setObjectName("userAdText")
        self.passAdText = QtWidgets.QLineEdit(self.adminTab)
        self.passAdText.setGeometry(QtCore.QRect(50, 330, 261, 31))
        self.passAdText.setStyleSheet("QLineEdit{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.passAdText.setObjectName("passAdText")
        self.incorrrecAdmLbl = QtWidgets.QLabel(self.adminTab)
        self.incorrrecAdmLbl.setGeometry(QtCore.QRect(50, 400, 261, 16))
        self.incorrrecAdmLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    color: red;\n"
"}")
        self.incorrrecAdmLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.incorrrecAdmLbl.setObjectName("incorrrecAdmLbl")
        self.tabWidget.addTab(self.adminTab, "")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.logo_3 = QtWidgets.QLabel(self.aboutTab)
        self.logo_3.setGeometry(QtCore.QRect(90, 80, 161, 171))
        self.logo_3.setText("")
        self.logo_3.setTextFormat(QtCore.Qt.RichText)
        self.logo_3.setPixmap(QtGui.QPixmap("CardinalAIDS-full.jpg"))
        self.logo_3.setScaledContents(True)
        self.logo_3.setObjectName("logo_3")
        self.oldPW = QtWidgets.QLabel(self.aboutTab)
        self.oldPW.setGeometry(QtCore.QRect(60, 280, 221, 91))
        self.oldPW.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font: 8pt \"Segoe UI\";\n"
"    background:white;\n"
"}")
        self.oldPW.setAlignment(QtCore.Qt.AlignCenter)
        self.oldPW.setObjectName("oldPW")
        self.tabWidget.addTab(self.aboutTab, "")

        self.retranslateUi(LoginWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        LoginWindow.setTabOrder(self.userText, self.passText)
        LoginWindow.setTabOrder(self.passText, self.loginBtn)
        LoginWindow.setTabOrder(self.loginBtn, self.userAdText)
        LoginWindow.setTabOrder(self.userAdText, self.passAdText)
        LoginWindow.setTabOrder(self.passAdText, self.loginAdBtn)
        LoginWindow.setTabOrder(self.loginAdBtn, self.tabWidget)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Cardinal Login"))
        self.loginBtn.setText(_translate("LoginWindow", "LOGIN"))
        self.userText.setPlaceholderText(_translate("LoginWindow", "Username"))
        self.passText.setPlaceholderText(_translate("LoginWindow", "Password"))
        self.incorrrectLbl.setText(_translate("LoginWindow", "Incorrect username or password."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.loginTab), _translate("LoginWindow", "STUDENT"))
        self.loginAdBtn.setText(_translate("LoginWindow", "LOGIN"))
        self.userAdText.setPlaceholderText(_translate("LoginWindow", "Admin Username"))
        self.passAdText.setPlaceholderText(_translate("LoginWindow", "Admin Password"))
        self.incorrrecAdmLbl.setText(_translate("LoginWindow", "Incorrect username or password."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adminTab), _translate("LoginWindow", "ADMIN"))
        self.oldPW.setText(_translate("LoginWindow", "CardinalAIDS+ is a student information\n"
"chat bot designed for Mapúa.\n"
"\n"
"Project Collaborators:\n"
"CPE-106L B1 Group09\n"
"CPE-106L B2 Group04"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("LoginWindow", "ABOUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QDialog()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

