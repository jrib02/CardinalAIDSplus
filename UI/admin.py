# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(540, 499)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AdminWindow.sizePolicy().hasHeightForWidth())
        AdminWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("CardinalAIDSicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdminWindow.setWindowIcon(icon)
        AdminWindow.setStyleSheet("QWidget {\n"
"    background: red;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 541, 501))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 10px solid yellow;\n"
"    position: absolute;\n"
"\n"
"}\n"
"QTabWidget>QWidget>QWidget{background: white;}\n"
"QTabWidget{\n"
"    /*font: 10pt \"Segoe UI\";*/\n"
"    background: rgb(247, 245, 246);\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: red;\n"
"    padding: 8px;\n"
"    font:10pt  white \"Segoe UI\"; \n"
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
        self.askedTab = QtWidgets.QWidget()
        self.askedTab.setObjectName("askedTab")
        self.askedTable = QtWidgets.QTableWidget(self.askedTab)
        self.askedTable.setEnabled(True)
        self.askedTable.setGeometry(QtCore.QRect(20, 10, 501, 401))
        self.askedTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.askedTable.setAutoFillBackground(False)
        self.askedTable.setStyleSheet("QTableView{\n"
"    background: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QTableView::item{\n"
"    selection-background-color: rgb(204,0,0);\n"
"    color: black;\n"
"}\n"
"QHeaderView::section{\n"
"    background-color: rgb(204,0,0);\n"
"    color: white;\n"
"    border: 0px;\n"
"}\n"
"QTableView QTableCornerButton::section {\n"
"    background: rgb(204,0,0);\n"
"    border: red;\n"
"}")
        self.askedTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.askedTable.setShowGrid(True)
        self.askedTable.setRowCount(0)
        self.askedTable.setColumnCount(3)
        self.askedTable.setObjectName("askedTable")
        self.askedTable.verticalHeader().setVisible(True)
        self.deleteAskedBtn = QtWidgets.QPushButton(self.askedTab)
        self.deleteAskedBtn.setGeometry(QtCore.QRect(140, 415, 261, 31))
        self.deleteAskedBtn.setStyleSheet("QPushButton {\n"
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
        self.deleteAskedBtn.setCheckable(False)
        self.deleteAskedBtn.setAutoDefault(True)
        self.deleteAskedBtn.setObjectName("deleteAskedBtn")
        self.tabWidget.addTab(self.askedTab, "")
        self.invalidTab = QtWidgets.QWidget()
        self.invalidTab.setObjectName("invalidTab")
        self.invalidTable = QtWidgets.QTableWidget(self.invalidTab)
        self.invalidTable.setEnabled(True)
        self.invalidTable.setGeometry(QtCore.QRect(20, 10, 501, 401))
        self.invalidTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.invalidTable.setAutoFillBackground(False)
        self.invalidTable.setStyleSheet("QTableView{\n"
"    background: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QTableView::item{\n"
"    selection-background-color: rgb(204,0,0);\n"
"    color: black;\n"
"}\n"
"QHeaderView::section{\n"
"    background-color: rgb(204,0,0);\n"
"    color: white;\n"
"    border: 0px;\n"
"}\n"
"QTableView QTableCornerButton::section {\n"
"    background: rgb(204,0,0);\n"
"    border: red;\n"
"}")
        self.invalidTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.invalidTable.setShowGrid(True)
        self.invalidTable.setRowCount(0)
        self.invalidTable.setColumnCount(3)
        self.invalidTable.setObjectName("invalidTable")
        self.invalidTable.verticalHeader().setVisible(False)
        self.deleteInvalidBtn = QtWidgets.QPushButton(self.invalidTab)
        self.deleteInvalidBtn.setGeometry(QtCore.QRect(140, 415, 261, 31))
        self.deleteInvalidBtn.setStyleSheet("QPushButton {\n"
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
        self.deleteInvalidBtn.setCheckable(False)
        self.deleteInvalidBtn.setAutoDefault(True)
        self.deleteInvalidBtn.setObjectName("deleteInvalidBtn")
        self.tabWidget.addTab(self.invalidTab, "")
        self.updateTab = QtWidgets.QWidget()
        self.updateTab.setObjectName("updateTab")
        self.addBtn = QtWidgets.QPushButton(self.updateTab)
        self.addBtn.setGeometry(QtCore.QRect(80, 370, 91, 31))
        self.addBtn.setStyleSheet("QPushButton {\n"
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
        self.addBtn.setCheckable(False)
        self.addBtn.setAutoDefault(True)
        self.addBtn.setObjectName("addBtn")
        self.updateUserText = QtWidgets.QLineEdit(self.updateTab)
        self.updateUserText.setGeometry(QtCore.QRect(190, 30, 311, 31))
        self.updateUserText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.updateUserText.setPlaceholderText("")
        self.updateUserText.setObjectName("updateUserText")
        self.updateUserLbl = QtWidgets.QLabel(self.updateTab)
        self.updateUserLbl.setGeometry(QtCore.QRect(40, 35, 101, 16))
        self.updateUserLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"}")
        self.updateUserLbl.setObjectName("updateUserLbl")
        self.updateFirstLbl = QtWidgets.QLabel(self.updateTab)
        self.updateFirstLbl.setGeometry(QtCore.QRect(40, 125, 111, 16))
        self.updateFirstLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"}")
        self.updateFirstLbl.setObjectName("updateFirstLbl")
        self.updateFirstText = QtWidgets.QLineEdit(self.updateTab)
        self.updateFirstText.setGeometry(QtCore.QRect(190, 120, 311, 31))
        self.updateFirstText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.updateFirstText.setPlaceholderText("")
        self.updateFirstText.setObjectName("updateFirstText")
        self.updateMiddleText = QtWidgets.QLineEdit(self.updateTab)
        self.updateMiddleText.setGeometry(QtCore.QRect(190, 170, 311, 31))
        self.updateMiddleText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.updateMiddleText.setPlaceholderText("")
        self.updateMiddleText.setObjectName("updateMiddleText")
        self.updateMIddleLbl = QtWidgets.QLabel(self.updateTab)
        self.updateMIddleLbl.setGeometry(QtCore.QRect(40, 175, 141, 16))
        self.updateMIddleLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"}")
        self.updateMIddleLbl.setObjectName("updateMIddleLbl")
        self.updateLastLbl = QtWidgets.QLabel(self.updateTab)
        self.updateLastLbl.setGeometry(QtCore.QRect(40, 225, 141, 16))
        self.updateLastLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"}")
        self.updateLastLbl.setObjectName("updateLastLbl")
        self.updateLastText = QtWidgets.QLineEdit(self.updateTab)
        self.updateLastText.setGeometry(QtCore.QRect(190, 220, 311, 31))
        self.updateLastText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.updateLastText.setPlaceholderText("")
        self.updateLastText.setObjectName("updateLastText")
        self.updateFeesText = QtWidgets.QLineEdit(self.updateTab)
        self.updateFeesText.setGeometry(QtCore.QRect(190, 270, 311, 31))
        self.updateFeesText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.updateFeesText.setPlaceholderText("")
        self.updateFeesText.setObjectName("updateFeesText")
        self.updateFeeLbl = QtWidgets.QLabel(self.updateTab)
        self.updateFeeLbl.setGeometry(QtCore.QRect(40, 265, 131, 41))
        self.updateFeeLbl.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";\n"
"    background:white;\n"
"}")
        self.updateFeeLbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.updateFeeLbl.setObjectName("updateFeeLbl")
        self.removeBtn = QtWidgets.QPushButton(self.updateTab)
        self.removeBtn.setGeometry(QtCore.QRect(220, 370, 91, 31))
        self.removeBtn.setStyleSheet("QPushButton {\n"
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
        self.removeBtn.setCheckable(False)
        self.removeBtn.setAutoDefault(True)
        self.removeBtn.setObjectName("removeBtn")
        self.updateBtn = QtWidgets.QPushButton(self.updateTab)
        self.updateBtn.setGeometry(QtCore.QRect(360, 370, 91, 31))
        self.updateBtn.setStyleSheet("QPushButton {\n"
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
        self.updateBtn.setCheckable(False)
        self.updateBtn.setAutoDefault(True)
        self.updateBtn.setObjectName("updateBtn")
        self.updateMessage = QtWidgets.QLabel(self.updateTab)
        self.updateMessage.setGeometry(QtCore.QRect(40, 330, 461, 16))
        self.updateMessage.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    color: red;\n"
"}")
        self.updateMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.updateMessage.setObjectName("updateMessage")
        self.updatePassText = QtWidgets.QLineEdit(self.updateTab)
        self.updatePassText.setGeometry(QtCore.QRect(190, 75, 311, 31))
        self.updatePassText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.updatePassText.setText("")
        self.updatePassText.setPlaceholderText("")
        self.updatePassText.setObjectName("updatePassText")
        self.updatePassLbl = QtWidgets.QLabel(self.updateTab)
        self.updatePassLbl.setGeometry(QtCore.QRect(40, 80, 111, 16))
        self.updatePassLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"}")
        self.updatePassLbl.setObjectName("updatePassLbl")
        self.tabWidget.addTab(self.updateTab, "")
        self.accAdTab = QtWidgets.QWidget()
        self.accAdTab.setObjectName("accAdTab")
        self.logoutAdBtn = QtWidgets.QPushButton(self.accAdTab)
        self.logoutAdBtn.setGeometry(QtCore.QRect(140, 350, 261, 31))
        self.logoutAdBtn.setStyleSheet("QPushButton {\n"
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
        self.logoutAdBtn.setCheckable(False)
        self.logoutAdBtn.setAutoDefault(True)
        self.logoutAdBtn.setObjectName("logoutAdBtn")
        self.oldAdPW = QtWidgets.QLabel(self.accAdTab)
        self.oldAdPW.setGeometry(QtCore.QRect(50, 60, 131, 21))
        self.oldAdPW.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";\n"
"    background:white;\n"
"}")
        self.oldAdPW.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.oldAdPW.setObjectName("oldAdPW")
        self.newAdPW = QtWidgets.QLabel(self.accAdTab)
        self.newAdPW.setGeometry(QtCore.QRect(50, 120, 131, 21))
        self.newAdPW.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";\n"
"    background:white;\n"
"}")
        self.newAdPW.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.newAdPW.setObjectName("newAdPW")
        self.confirmAdPW = QtWidgets.QLabel(self.accAdTab)
        self.confirmAdPW.setGeometry(QtCore.QRect(50, 170, 131, 41))
        self.confirmAdPW.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";\n"
"    background:white;\n"
"}")
        self.confirmAdPW.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.confirmAdPW.setObjectName("confirmAdPW")
        self.changeAdBtn = QtWidgets.QPushButton(self.accAdTab)
        self.changeAdBtn.setGeometry(QtCore.QRect(140, 230, 261, 31))
        self.changeAdBtn.setStyleSheet("QPushButton {\n"
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
        self.changeAdBtn.setCheckable(False)
        self.changeAdBtn.setAutoDefault(True)
        self.changeAdBtn.setObjectName("changeAdBtn")
        self.newAdPWText = QtWidgets.QLineEdit(self.accAdTab)
        self.newAdPWText.setGeometry(QtCore.QRect(220, 115, 301, 31))
        self.newAdPWText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.newAdPWText.setObjectName("newAdPWText")
        self.confirmAdPWText = QtWidgets.QLineEdit(self.accAdTab)
        self.confirmAdPWText.setGeometry(QtCore.QRect(220, 170, 301, 31))
        self.confirmAdPWText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.confirmAdPWText.setObjectName("confirmAdPWText")
        self.oldAdPWText = QtWidgets.QLineEdit(self.accAdTab)
        self.oldAdPWText.setGeometry(QtCore.QRect(220, 55, 301, 31))
        self.oldAdPWText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.oldAdPWText.setObjectName("oldAdPWText")
        self.matchAdmPassword = QtWidgets.QLabel(self.accAdTab)
        self.matchAdmPassword.setGeometry(QtCore.QRect(240, 150, 261, 16))
        self.matchAdmPassword.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    color: red;\n"
"}")
        self.matchAdmPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.matchAdmPassword.setObjectName("matchAdmPassword")
        self.incorrectAdmChange = QtWidgets.QLabel(self.accAdTab)
        self.incorrectAdmChange.setGeometry(QtCore.QRect(140, 260, 261, 16))
        self.incorrectAdmChange.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    color: red;\n"
"}")
        self.incorrectAdmChange.setAlignment(QtCore.Qt.AlignCenter)
        self.incorrectAdmChange.setObjectName("incorrectAdmChange")
        self.tabWidget.addTab(self.accAdTab, "")
        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)
        AdminWindow.setTabOrder(self.askedTable, self.tabWidget)
        AdminWindow.setTabOrder(self.tabWidget, self.invalidTable)
        AdminWindow.setTabOrder(self.invalidTable, self.updateUserText)
        AdminWindow.setTabOrder(self.updateUserText, self.updatePassText)
        AdminWindow.setTabOrder(self.updatePassText, self.updateFirstText)
        AdminWindow.setTabOrder(self.updateFirstText, self.updateMiddleText)
        AdminWindow.setTabOrder(self.updateMiddleText, self.updateLastText)
        AdminWindow.setTabOrder(self.updateLastText, self.updateFeesText)
        AdminWindow.setTabOrder(self.updateFeesText, self.addBtn)
        AdminWindow.setTabOrder(self.addBtn, self.removeBtn)
        AdminWindow.setTabOrder(self.removeBtn, self.updateBtn)
        AdminWindow.setTabOrder(self.updateBtn, self.oldAdPWText)
        AdminWindow.setTabOrder(self.oldAdPWText, self.newAdPWText)
        AdminWindow.setTabOrder(self.newAdPWText, self.confirmAdPWText)
        AdminWindow.setTabOrder(self.confirmAdPWText, self.changeAdBtn)
        AdminWindow.setTabOrder(self.changeAdBtn, self.logoutAdBtn)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "CardinalAIDS+ ADMIN"))
        self.deleteAskedBtn.setText(_translate("AdminWindow", "DELETE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.askedTab), _translate("AdminWindow", "ASKED QUESTIONS"))
        self.deleteInvalidBtn.setText(_translate("AdminWindow", "DELETE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.invalidTab), _translate("AdminWindow", "INVALID ANSWERS"))
        self.addBtn.setText(_translate("AdminWindow", "ADD"))
        self.updateUserLbl.setText(_translate("AdminWindow", "USERNAME"))
        self.updateFirstLbl.setText(_translate("AdminWindow", "FIRST NAME"))
        self.updateMIddleLbl.setText(_translate("AdminWindow", "MIDDLE INITIAL"))
        self.updateLastLbl.setText(_translate("AdminWindow", "LAST NAME"))
        self.updateFeeLbl.setText(_translate("AdminWindow", "UNSETTLED\n"
"FEES"))
        self.removeBtn.setText(_translate("AdminWindow", "REMOVE"))
        self.updateBtn.setText(_translate("AdminWindow", "UPDATE"))
        self.updateMessage.setText(_translate("AdminWindow", "foo"))
        self.updatePassLbl.setText(_translate("AdminWindow", "PASSWORD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.updateTab), _translate("AdminWindow", "UPDATE STUDENT INFO"))
        self.logoutAdBtn.setText(_translate("AdminWindow", "LOGOUT"))
        self.oldAdPW.setText(_translate("AdminWindow", "OLD PASSWORD"))
        self.newAdPW.setText(_translate("AdminWindow", "NEW PASSWORD"))
        self.confirmAdPW.setText(_translate("AdminWindow", "CONFIRM NEW\n"
"PASSWORD"))
        self.changeAdBtn.setText(_translate("AdminWindow", "CHANGE PASSWORD"))
        self.matchAdmPassword.setText(_translate("AdminWindow", "Passwords do not match."))
        self.incorrectAdmChange.setText(_translate("AdminWindow", "Current password incorrect."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accAdTab), _translate("AdminWindow", "ACCOUNT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminWindow()
    ui.setupUi(AdminWindow)
    AdminWindow.show()
    sys.exit(app.exec_())

