import PyQt5
import random
from PyQt5 import QtWidgets, uic, QtCore, QtGui, QtSql
from login import Ui_LoginWindow
from student import Ui_StdWindow
from admin import Ui_AdminWindow
from bot import AIchat
import sqlite3

conn = sqlite3.connect('CardinalAIDS.db')
c = conn.cursor()

class info(): #proxy; passes variable between classes
    def __init__(self):
        self.user = ''
        print ('just to check')

class StudentWindow(QtWidgets.QMainWindow, Ui_StdWindow):
    logoutStd = QtCore.pyqtSignal()

    conn = sqlite3.connect('CardinalAIDS.db')
    c = conn.cursor()
    #user = info.user    #doesn't work here apparently but works in line 102    
    bot = AIchat("jriborreta")

    def __init__(self, parent=None):
        super(StudentWindow, self).__init__(parent)
        self.setupUi(self)
        self.logoutBtn.clicked.connect(self.logout)
        self.oldPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.listWidget.setWordWrap(True)
        self.sendBtn.clicked.connect(self.chat)
        self.changePW.clicked.connect(self.change)
        header = self.historyTable.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.historyTable.setHorizontalHeaderLabels(["QUESTIONS", "ANSWERS"])
        self.load_stdData() #loads data from database
        self.randomGreeting()

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

    def followUp(self):
        followUpReplies = ["Do you have more questions? ",
                           "Do you still have questions? ",
                           "Would you like to repeat it? "]
        self.flag = random.choice(followUpReplies)
        self.listWidget.addItem("CardinalAIDS+: "+ random.choice(followUpReplies))
        replies = self.listWidget.findItems("CardinalAIDS+:", QtCore.Qt.MatchStartsWith)
        self.colorReply(replies)

    def load_stdData(self):
        self.c.execute('''SELECT * FROM history ''')
        rows = self.c.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.historyTable.insertRow(inx)
            self.historyTable.setColumnCount(2)
            self.historyTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.historyTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[1]))

    @QtCore.pyqtSlot()
    def chat(self):
        self.question = self.questionText.text()
        self.listWidget.addItem("You: "+self.question)
        self.bot = AIchat(info.user)                 #hardcoded for AIchat to receive username, should be info.user but no work man
        self.answer = self.bot.getQues(self.question)
        self.listWidget.addItem("CardinalAIDS: "+self.answer)
        #self.followUp()
        replies = self.listWidget.findItems("CardinalAIDS:", QtCore.Qt.MatchStartsWith)
        self.colorReply(replies)
        numRows = self.historyTable.rowCount()
        self.historyTable.insertRow(numRows)
        self.historyTable.setItem(numRows, 0, QtWidgets.QTableWidgetItem(self.question)) #directly add to table than use load_data again and again
        self.historyTable.setItem(numRows, 1, QtWidgets.QTableWidgetItem(self.answer))
        self.historyTable.resizeRowsToContents()
        self.c.execute("INSERT INTO history (questions, answers) VALUES (?,?)", (self.question, self.answer))
        conn.commit()
        self.questionText.clear()

    @QtCore.pyqtSlot()
    def invalid(self):
        self.c.execute("INSERT INTO history (questions, answers, validity) VALUES (?,?,'invalid')", (self.question, self.answer))
        conn.commit()

    @QtCore.pyqtSlot()
    def change(self):
        new = self.newPWText.text()
        data = list(c.execute("SELECT password FROM students WHERE username == ?", (info.user,))) #info.user works here idk why
        if data:
            if self.newPWText.text() == self.confirmPWText.text():
                new = self.newPWText.text()
                self.c.execute("UPDATE students SET password=? WHERE username == ?", (new, info.user))
                self.conn.commit()
                self.oldPWText.clear()
                self.newPWText.clear()
                self.confirmPWText.clear()
            else:
                self.confirmPWText.clear()
        else:
            self.oldPWText.clear()

    @QtCore.pyqtSlot()
    def logout(self):
        self.listWidget.clear()
        self.randomGreeting()
        self.tabWidget.setCurrentIndex(0)
        self.historyTable.clear()   #clear table first
        self.load_stdData()         #then repopulate with load data before exit
        conn.commit()
        self.logoutStd.emit()
        self.close()

class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):
    logoutAdm = QtCore.pyqtSignal()

    conn = sqlite3.connect('CardinalAIDS.db')
    c = conn.cursor()

    def __init__(self, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.setupUi(self)
        self.changeAdBtn.clicked.connect(self.changeAdm)
        self.logoutAdBtn.clicked.connect(self.logout)
        self.oldAdPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newAdPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmAdPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        aHeader = self.askedTable.horizontalHeader()       
        aHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        aHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.askedTable.setHorizontalHeaderLabels(["QUESTIONS", "ANSWERS"])
        bHeader = self.invalidTable.horizontalHeader()       
        bHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        bHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.invalidTable.setHorizontalHeaderLabels(["QUESTIONS", "ANSWERS"])
        self.load_askedData()
        self.load_invalidData()

    def load_askedData(self):
        self.c.execute('''SELECT * FROM history ''')
        rows = self.c.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.askedTable.insertRow(inx)
            self.askedTable.setColumnCount(2)
            self.askedTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.askedTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[1]))
            

    def load_invalidData(self):
        self.c.execute('''SELECT * FROM history WHERE validity='invalid' ''')
        rows = self.c.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.historyTable.insertRow(inx)
            self.historyTable.setColumnCount(2)
            self.historyTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.historyTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[1]))

    @QtCore.pyqtSlot()
    def changeAdm(self):
        new = self.newAdPWText.text()
        data = list(c.execute("SELECT password FROM admins WHERE username == ?", (info.user,)))
        if data:
            if self.newAdPWText.text() == self.confirmAdPWText.text():
                new = self.newAdPWText.text()
                self.c.execute("UPDATE admins SET password=? WHERE username == ?", (new, info.user))
                self.conn.commit()
                self.oldAdPWText.clear()
                self.newAdPWText.clear()
                self.confirmAdPWText.clear()
            else:
                self.confirmAdPWText.clear()
        else:
            self.oldAdPWText.clear()

    @QtCore.pyqtSlot()
    def logout(self):
        conn.commit()
        self.tabWidget.setCurrentIndex(0)
        self.askedTable.clear()
        self.invalidTable.clear()
        self.logoutAdm.emit()
        self.close()

class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    loggedStd = QtCore.pyqtSignal()
    loggedAdm = QtCore.pyqtSignal()

    conn = sqlite3.connect('CardinalAIDS.db')
    c = conn.cursor()

    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.loginBtn.clicked.connect(self.authenticateStd)
        self.loginAdBtn.clicked.connect(self.authenticateAdm)
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passAdText.setEchoMode(QtWidgets.QLineEdit.Password)

    @QtCore.pyqtSlot()
    def authenticateStd(self):
        userStd = self.userText.text()
        passStd = self.passText.text()
        a = list(c.execute("SELECT * FROM students WHERE username=? and password=?", (userStd, passStd)))
        if a:
            info.user = userStd
            self.passText.clear()
            self.loggedStd.emit()
            self.close()
        else:
            self.passText.clear()

    @QtCore.pyqtSlot()
    def authenticateAdm(self):
        userAdm = self.userAdText.text()
        passAdm = self.passAdText.text()
        a = list(c.execute("SELECT * FROM admins WHERE username=? and password=?", (userAdm, passAdm)))
        if a:
            info.user = userAdm
            self.passAdText.clear()
            self.loggedAdm.emit()
            self.close()
        else:
            self.passText.clear()       
            

def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindow()
    std = StudentWindow()
    adm = AdminWindow()
    t = info()

    login.loggedStd.connect(std.show)
    login.loggedAdm.connect(adm.show)

    std.logoutStd.connect(login.show)
    adm.logoutAdm.connect(login.show)

    login.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
