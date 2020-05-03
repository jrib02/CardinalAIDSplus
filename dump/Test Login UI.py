# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Erin'sGamingPC\Desktop\Test CAIDS\test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from OtherWindow import Ui_OtherWindow
import sqlite3
import random



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Login Window")
        MainWindow.resize(302, 159)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exitWinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitWinBtn.setGeometry(QtCore.QRect(40, 90, 75, 23))
        self.exitWinBtn.setObjectName("exitWinBtn")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.loginBtn.setObjectName("loginBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.userline = QtWidgets.QLineEdit(self.centralwidget)
        self.userline.setGeometry(QtCore.QRect(70, 10, 211, 20))
        self.userline.setInputMask("")
        self.userline.setObjectName("userline")
        self.passline = QtWidgets.QLineEdit(self.centralwidget)
        self.passline.setGeometry(QtCore.QRect(70, 50, 211, 20))
        self.passline.setObjectName("passline")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 302, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loginBtn.clicked.connect(self.checkLogin)
        self.exitWinBtn.clicked.connect(self.openWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exitWinBtn.setText(_translate("MainWindow", "Exit"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUI(self.window)
        self.window.show()
        
    
    def checkLogin(self):
        c.execute("SELECT * FROM students WHERE username == ?",(usernameInput,))    
        data = c.fetchall()
    
        for entry in data:
            username = entry[0]
            password = entry[1]
            
        
        #msg = QMessageBox()
        if self.userline.text() == username and self.passline.text() == password:
            #msg.setText('Login Successful')
            #msg.exec_()
            print('yeet')
        else:
            #msg.setText('Login Denied')
            #msg.exec_()
            print('yoot')

    def exitWin(self):
        sys.exit(app.exec_())
            
conn = sqlite3.connect('CardinalAIDS.db')
c = conn.cursor()

    
#if passwordInput == password:
#    print("Welcome to CardinalAIDS+! \n")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
