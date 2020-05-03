import sys
import random
sys.path.append("../CardinalAIDSplus")
from PyQt5 import QtWidgets, uic, QtCore, QtGui, QtSql
from UI.mainUi import Ui_MainWindow
from UI.login import Ui_LoginWindow
from DAL.database import *
from bot import AIchat

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, username='', user='', parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(540, 499)
        self.setWindowIcon(QtGui.QIcon('CardinalAIDS-icofile.ico'))
        self.username = username
        self.user = user

        self.logoutBtn.clicked.connect(self.logout)
        self.sendBtn.clicked.connect(self.chat)
        #self.changePW.clicked.connect(self.change)
        """ self.invalidBtn.clicked.connect(self.invalid)
        self.newPWText.textEdited.connect(self.comparePass)
        self.confirmPWText.textEdited.connect(self.comparePass)

        self.addBtn.clicked.connect(self.addStudent)
        self.removeBtn.clicked.connect(self.removeStudent)
        self.updateBtn.clicked.connect(self.updateStudent)
        self.deleteAskedBtn.clicked.connect(self.deleteAskedEntry)
        self.deleteInvalidBtn.clicked.connect(self.deleteInvalidEntry) """

        self.oldPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.listWidget.setWordWrap(True)

        self.matchPassword.setVisible(False)
        self.incorrectChange.setVisible(False)
        self.updateMessage.setVisible(False)

        header = self.historyTable.horizontalHeader()
        self.historyTable.setColumnCount(2)       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.historyTable.setHorizontalHeaderLabels(["QUESTIONS", "ANSWERS"])
        self.randomGreeting()

        self.askedTable.verticalHeader().setVisible(True)
        self.askedTable.setColumnCount(3)
        self.askedTable.resizeColumnsToContents()
        aHeader = self.askedTable.horizontalHeader()       
        aHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.askedTable.setColumnWidth(1, 50)
        aHeader.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        aVertHeader = self.askedTable.verticalHeader()
        aVertHeader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        bHeader = self.invalidTable.horizontalHeader()       
        bHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.askedTable.setColumnWidth(1, 50)
        self.invalidTable.verticalHeader().setVisible(True)
        self.invalidTable.setColumnCount(3)
        bHeader.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        bVertHeader = self.invalidTable.verticalHeader()
        bVertHeader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.invalidTable.setHorizontalHeaderLabels(["USER", "QUESTIONS", "ANSWERS"])
        self.askedTable.setHorizontalHeaderLabels(["USER", "QUESTIONS", "ANSWERS"])

        if self.user == 'student':
            self.askedTab.setEnabled(False)
            self.askedTab.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")
            self.invalidTab.setEnabled(False)
            self.invalidTab.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")
            self.updateTab.setEnabled(False)
            self.updateTab.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")

        self.login = LoginWindow()
        self.login.show()
        #self.login.getStudentInfo()

    def randomGreeting(self):
        greetings = ["Hi, welcome to CardinalAIDS+!",
                     "Hi, I hope you're doing well."]
        self.listWidget.addItem("CardinalAIDS+: "+ random.choice(greetings))
        replies = self.listWidget.findItems("CardinalAIDS+:", QtCore.Qt.MatchStartsWith)
        self.colorReply(replies)

    def colorReply(self, replies):
        if len(replies)>0:
            for reply in replies:
                reply.setForeground(QtGui.QColor("white"))
                reply.setBackground(QtGui.QColor("#cc0000"))

    def load_stdData(self):
        self.historyTable.verticalHeader().setVisible(True)
        rows = loadStudentTableData(self.username)
        for row in rows:
            inx = rows.index(row)
            self.historyTable.insertRow(inx)
            self.historyTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.historyTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[2]))

    def load_askedData(self):
        rows = loadAdminTableData('valid')
        for row in rows:
            inx = rows.index(row)
            self.askedTable.insertRow(inx)
            self.askedTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.askedTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.askedTable.setItem(inx, 2, QtWidgets.QTableWidgetItem(row[2]))

    def load_invalidData(self, userAdm):
        rows = loadAdminTableData('invalid')
        for row in rows:
            inx = rows.index(row)
            self.invalidTable.insertRow(inx)
            self.invalidTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.invalidTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.invalidTable.setItem(inx, 2, QtWidgets.QTableWidgetItem(row[2]))

    @QtCore.pyqtSlot()
    def chat(self):
        self.question = self.questionText.text()
        checkQues = self.login.checkWhiteSpace(self.question)
        if checkQues:
            self.listWidget.addItem("You: "+self.question)
            self.bot = AIchat(self.user)
            self.answer = self.bot.getQues(self.question)
            self.listWidget.addItem("CardinalAIDS: "+self.answer)
            replies = self.listWidget.findItems("CardinalAIDS:", QtCore.Qt.MatchStartsWith)
            self.colorReply(replies)
            numRows = self.historyTable.rowCount()
            self.historyTable.insertRow(numRows)
            self.historyTable.setItem(numRows, 0, QtWidgets.QTableWidgetItem(self.question))
            self.historyTable.setItem(numRows, 1, QtWidgets.QTableWidgetItem(self.answer))
            self.historyTable.resizeRowsToContents()
            addToHistory(self.username)
            self.conn.commit()
            self.questionText.clear()


    @QtCore.pyqtSlot()
    def logout(self):
        self.tabWidget.setCurrentIndex(0)
        self.historyTable.clearContents()
        self.historyTable.setRowCount(0)
        self.askedTable.clearContents()
        self.invalidTable.clearContents()
        self.askedTable.setRowCount(0)
        self.invalidTable.setRowCount(0)
        self.login.show()
        self.close()    


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(341, 481)
        self.loginBtn.clicked.connect(self.authenticateStd)
        self.loginAdBtn.clicked.connect(self.authenticateAdm)
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passAdText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.incorrrectLbl.setVisible(False)
        self.incorrrecAdmLbl.setVisible(False)
        self.userText.returnPressed.connect(self.authenticateStd)
        self.passText.returnPressed.connect(self.authenticateStd)
        self.userAdText.returnPressed.connect(self.authenticateAdm)
        self.passAdText.returnPressed.connect(self.authenticateAdm)
        self.setWindowIcon(QtGui.QIcon('CardinalAIDS-icofile.ico'))
        tabFocus = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Tab), self)
        tabFocus.activated.connect(self.changeFocus)

    @QtCore.pyqtSlot()
    def changeFocus(self):
        self.focusNextChild()

    def clearWindow(self):
        self.incorrrectLbl.setVisible(False)
        self.incorrrecAdmLbl.setVisible(False)
        #self.passText.clear()
        #self.passAdText.clear()

    def checkWhiteSpace(self, word):
        checker = True
        if word.isspace() or word == '':
            checker = False
        else:
            checker = True
        return checker

    def getStudentInfo(self, username, password):
        username = self.userText.text()
        password = self.passText.text()

    def getAdminInfo(self, username, password):
        username = self.userAdText.text()
        password = self.passAdText.text()

    @QtCore.pyqtSlot()
    def authenticateStd(self):
        userStd = self.userText.text()
        passStd = self.passText.text()
        checkUser = self.checkWhiteSpace(userStd)
        checkPass = self.checkWhiteSpace(passStd)
        if checkUser and checkPass:
            if checkPassword(userStd, passStd, 'students'):
                self.clearWindow()
                #self.userAdText.clear()
                self.hide()
            else:
                self.passText.clear()
                self.incorrrectLbl.setVisible(True)
        else:
            self.userText.clear()
            self.passText.clear()
            self.incorrrectLbl.setVisible(True)

    @QtCore.pyqtSlot()
    def authenticateAdm(self):
        userAdm = self.userAdText.text()
        passAdm = self.passAdText.text()
        checkAdmUser = self.checkWhiteSpace(userAdm)
        checkAdmPass = self.checkWhiteSpace(passAdm)
        if checkAdmUser and checkAdmPass:
            a = list(c.execute("SELECT * FROM admins WHERE username=? and password=?", (userAdm, passAdm)))
            if a:
                #self.clearWindow()
                self.userText.clear()
                self.hide()
            else:
                #self.passAdText.clear()    
                self.incorrrecAdmLbl.setVisible(True)
        else:
            self.userAdText.clear()
            self.passAdText.clear()   



def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()