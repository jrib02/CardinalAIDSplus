# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, StdWindow):
        StdWindow.setObjectName("StdWindow")
        StdWindow.resize(540, 499)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StdWindow.sizePolicy().hasHeightForWidth())
        StdWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("CardinalAIDSicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StdWindow.setWindowIcon(icon)
        StdWindow.setStyleSheet("QWidget {\n"
"    background: red;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(StdWindow)
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
        self.chatTab = QtWidgets.QWidget()
        self.chatTab.setObjectName("chatTab")
        self.sendBtn = QtWidgets.QPushButton(self.chatTab)
        self.sendBtn.setGeometry(QtCore.QRect(330, 415, 91, 31))
        self.sendBtn.setStyleSheet("QPushButton {\n"
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
        self.sendBtn.setCheckable(False)
        self.sendBtn.setAutoDefault(True)
        self.sendBtn.setObjectName("sendBtn")
        self.invalidBtn = QtWidgets.QPushButton(self.chatTab)
        self.invalidBtn.setGeometry(QtCore.QRect(430, 415, 101, 31))
        self.invalidBtn.setStyleSheet("QPushButton {\n"
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
        self.invalidBtn.setCheckable(False)
        self.invalidBtn.setAutoDefault(True)
        self.invalidBtn.setObjectName("invalidBtn")
        self.line = QtWidgets.QFrame(self.chatTab)
        self.line.setGeometry(QtCore.QRect(0, 400, 541, 8))
        self.line.setStyleSheet("Line{background:yellow;}")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.questionText = QtWidgets.QLineEdit(self.chatTab)
        self.questionText.setGeometry(QtCore.QRect(10, 415, 311, 31))
        self.questionText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.questionText.setObjectName("questionText")
        self.listWidget = QtWidgets.QListWidget(self.chatTab)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 541, 401))
        self.listWidget.setStyleSheet("QListWidget{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"    border: 0px;\n"
"    text-align: right;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.chatTab, "")
        self.historyTab = QtWidgets.QWidget()
        self.historyTab.setObjectName("historyTab")
        self.historyTable = QtWidgets.QTableWidget(self.historyTab)
        self.historyTable.setEnabled(True)
        self.historyTable.setGeometry(QtCore.QRect(20, 10, 501, 431))
        self.historyTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.historyTable.setAutoFillBackground(False)
        self.historyTable.setStyleSheet("QTableView{\n"
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
        self.historyTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.historyTable.setShowGrid(True)
        self.historyTable.setRowCount(0)
        self.historyTable.setColumnCount(2)
        self.historyTable.setObjectName("historyTable")
        self.historyTable.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.historyTab, "")
        self.askedTab = QtWidgets.QWidget()
        self.askedTab.setObjectName("askedTab")
        self.askedTable = QtWidgets.QTableWidget(self.askedTab)
        self.askedTable.setEnabled(True)
        self.askedTable.setGeometry(QtCore.QRect(20, 5, 501, 401))
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
        self.askedTable.verticalHeader().setVisible(False)
        self.deleteAskedBtn = QtWidgets.QPushButton(self.askedTab)
        self.deleteAskedBtn.setGeometry(QtCore.QRect(140, 410, 261, 31))
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
        self.invalidTable.setGeometry(QtCore.QRect(20, 5, 501, 401))
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
        self.deleteInvalidBtn.setGeometry(QtCore.QRect(140, 410, 261, 31))
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
        self.updateMIddleLbl = QtWidgets.QLabel(self.updateTab)
        self.updateMIddleLbl.setGeometry(QtCore.QRect(40, 175, 141, 16))
        self.updateMIddleLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"}")
        self.updateMIddleLbl.setObjectName("updateMIddleLbl")
        self.updateMessage = QtWidgets.QLabel(self.updateTab)
        self.updateMessage.setGeometry(QtCore.QRect(40, 330, 461, 16))
        self.updateMessage.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    color: red;\n"
"}")
        self.updateMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.updateMessage.setObjectName("updateMessage")
        self.updateFeeLbl = QtWidgets.QLabel(self.updateTab)
        self.updateFeeLbl.setGeometry(QtCore.QRect(40, 265, 131, 41))
        self.updateFeeLbl.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";\n"
"    background:white;\n"
"}")
        self.updateFeeLbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.updateFeeLbl.setObjectName("updateFeeLbl")
        self.updateLastLbl = QtWidgets.QLabel(self.updateTab)
        self.updateLastLbl.setGeometry(QtCore.QRect(40, 225, 141, 16))
        self.updateLastLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"}")
        self.updateLastLbl.setObjectName("updateLastLbl")
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
        self.updateFirstLbl = QtWidgets.QLabel(self.updateTab)
        self.updateFirstLbl.setGeometry(QtCore.QRect(40, 125, 111, 16))
        self.updateFirstLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"}")
        self.updateFirstLbl.setObjectName("updateFirstLbl")
        self.updatePassLbl = QtWidgets.QLabel(self.updateTab)
        self.updatePassLbl.setGeometry(QtCore.QRect(40, 80, 111, 16))
        self.updatePassLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"}")
        self.updatePassLbl.setObjectName("updatePassLbl")
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
        self.updateUserLbl = QtWidgets.QLabel(self.updateTab)
        self.updateUserLbl.setGeometry(QtCore.QRect(40, 35, 101, 16))
        self.updateUserLbl.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    font: 14pt \"Segoe UI\";\n"
"}")
        self.updateUserLbl.setObjectName("updateUserLbl")
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
        self.tabWidget.addTab(self.updateTab, "")
        self.accTab = QtWidgets.QWidget()
        self.accTab.setObjectName("accTab")
        self.logoutBtn = QtWidgets.QPushButton(self.accTab)
        self.logoutBtn.setGeometry(QtCore.QRect(140, 350, 261, 31))
        self.logoutBtn.setStyleSheet("QPushButton {\n"
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
        self.logoutBtn.setCheckable(False)
        self.logoutBtn.setAutoDefault(True)
        self.logoutBtn.setObjectName("logoutBtn")
        self.oldPW = QtWidgets.QLabel(self.accTab)
        self.oldPW.setGeometry(QtCore.QRect(50, 60, 161, 21))
        self.oldPW.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";\n"
"    background:white;\n"
"}")
        self.oldPW.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.oldPW.setObjectName("oldPW")
        self.newPW = QtWidgets.QLabel(self.accTab)
        self.newPW.setGeometry(QtCore.QRect(50, 120, 131, 21))
        self.newPW.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";\n"
"    background:white;\n"
"}")
        self.newPW.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.newPW.setObjectName("newPW")
        self.confirmPW = QtWidgets.QLabel(self.accTab)
        self.confirmPW.setGeometry(QtCore.QRect(50, 170, 131, 41))
        self.confirmPW.setStyleSheet("QLabel{\n"
"    color: black;\n"
"    font: 12pt \"Segoe UI\";\n"
"    background:white;\n"
"}")
        self.confirmPW.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.confirmPW.setObjectName("confirmPW")
        self.changePW = QtWidgets.QPushButton(self.accTab)
        self.changePW.setGeometry(QtCore.QRect(140, 230, 261, 31))
        self.changePW.setStyleSheet("QPushButton {\n"
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
        self.changePW.setCheckable(False)
        self.changePW.setAutoDefault(True)
        self.changePW.setObjectName("changePW")
        self.oldPWText = QtWidgets.QLineEdit(self.accTab)
        self.oldPWText.setGeometry(QtCore.QRect(220, 55, 301, 31))
        self.oldPWText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.oldPWText.setObjectName("oldPWText")
        self.newPWText = QtWidgets.QLineEdit(self.accTab)
        self.newPWText.setGeometry(QtCore.QRect(220, 115, 301, 31))
        self.newPWText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.newPWText.setObjectName("newPWText")
        self.confirmPWText = QtWidgets.QLineEdit(self.accTab)
        self.confirmPWText.setGeometry(QtCore.QRect(220, 170, 301, 31))
        self.confirmPWText.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 15px;\n"
"    border: 1px solid black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    background-color: white;\n"
"}")
        self.confirmPWText.setObjectName("confirmPWText")
        self.matchPassword = QtWidgets.QLabel(self.accTab)
        self.matchPassword.setGeometry(QtCore.QRect(240, 150, 261, 16))
        self.matchPassword.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    color: red;\n"
"}")
        self.matchPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.matchPassword.setObjectName("matchPassword")
        self.incorrectChange = QtWidgets.QLabel(self.accTab)
        self.incorrectChange.setGeometry(QtCore.QRect(140, 260, 261, 16))
        self.incorrectChange.setStyleSheet("QLabel{\n"
"    background: white;\n"
"    color: red;\n"
"}")
        self.incorrectChange.setAlignment(QtCore.Qt.AlignCenter)
        self.incorrectChange.setObjectName("incorrectChange")
        self.tabWidget.addTab(self.accTab, "")
        StdWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StdWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StdWindow)
        StdWindow.setTabOrder(self.questionText, self.sendBtn)
        StdWindow.setTabOrder(self.sendBtn, self.invalidBtn)
        StdWindow.setTabOrder(self.invalidBtn, self.listWidget)
        StdWindow.setTabOrder(self.listWidget, self.historyTable)
        StdWindow.setTabOrder(self.historyTable, self.oldPWText)
        StdWindow.setTabOrder(self.oldPWText, self.newPWText)
        StdWindow.setTabOrder(self.newPWText, self.confirmPWText)
        StdWindow.setTabOrder(self.confirmPWText, self.changePW)
        StdWindow.setTabOrder(self.changePW, self.logoutBtn)
        StdWindow.setTabOrder(self.logoutBtn, self.tabWidget)

    def retranslateUi(self, StdWindow):
        _translate = QtCore.QCoreApplication.translate
        StdWindow.setWindowTitle(_translate("StdWindow", "CardinalAIDS+"))
        self.sendBtn.setText(_translate("StdWindow", "SEND"))
        self.invalidBtn.setText(_translate("StdWindow", "INVALID"))
        self.questionText.setPlaceholderText(_translate("StdWindow", "Enter question"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chatTab), _translate("StdWindow", "CHAT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.historyTab), _translate("StdWindow", "HISTORY"))
        self.deleteAskedBtn.setText(_translate("StdWindow", "DELETE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.askedTab), _translate("StdWindow", "ASKED QUESTIONS"))
        self.deleteInvalidBtn.setText(_translate("StdWindow", "DELETE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.invalidTab), _translate("StdWindow", "INVALID ANSWERS"))
        self.updateBtn.setText(_translate("StdWindow", "UPDATE"))
        self.removeBtn.setText(_translate("StdWindow", "REMOVE"))
        self.updateMIddleLbl.setText(_translate("StdWindow", "MIDDLE INITIAL"))
        self.updateMessage.setText(_translate("StdWindow", "foo"))
        self.updateFeeLbl.setText(_translate("StdWindow", "UNSETTLED\n"
"FEES"))
        self.updateLastLbl.setText(_translate("StdWindow", "LAST NAME"))
        self.updateFirstLbl.setText(_translate("StdWindow", "FIRST NAME"))
        self.updatePassLbl.setText(_translate("StdWindow", "PASSWORD"))
        self.addBtn.setText(_translate("StdWindow", "ADD"))
        self.updateUserLbl.setText(_translate("StdWindow", "USERNAME"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.updateTab), _translate("StdWindow", "UPDATE STUDENT INFO"))
        self.logoutBtn.setText(_translate("StdWindow", "LOGOUT"))
        self.oldPW.setText(_translate("StdWindow", "CURRENT PASSWORD"))
        self.newPW.setText(_translate("StdWindow", "NEW PASSWORD"))
        self.confirmPW.setText(_translate("StdWindow", "CONFIRM NEW\n"
"PASSWORD"))
        self.changePW.setText(_translate("StdWindow", "CHANGE PASSWORD"))
        self.matchPassword.setText(_translate("StdWindow", "Passwords do not match."))
        self.incorrectChange.setText(_translate("StdWindow", "Current password incorrect."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accTab), _translate("StdWindow", "ACCOUNT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

