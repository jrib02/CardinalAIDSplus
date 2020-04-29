import PyQt5
import random
from PyQt5 import QtWidgets, uic, QtCore, QtGui, QtSql
from UI.login import Ui_LoginWindow
from UI.student import Ui_StdWindow
from UI.admin import Ui_AdminWindow
from UI.mainUi import Ui_MainWindow
from DAL.database import *
from bot import AIchat
import sqlite3
import ctypes

myappid = u'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class StudentWindow(QtWidgets.QMainWindow, Ui_StdWindow):
    checkMatch = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(StudentWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(540, 499)
        self.logoutBtn.clicked.connect(self.logout)
        self.questionText.setFocus()
        self.oldPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.listWidget.setWordWrap(True)
        self.sendBtn.clicked.connect(self.chat)
        self.changePW.clicked.connect(self.change)
        self.invalidBtn.clicked.connect(self.invalid)
        self.matchPassword.setVisible(False)
        self.incorrectChange.setVisible(False)
        self.newPWText.textEdited.connect(self.comparePass)
        self.confirmPWText.textEdited.connect(self.comparePass)
        header = self.historyTable.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.historyTable.setHorizontalHeaderLabels(["QUESTIONS", "ANSWERS"])
        self.randomGreeting()
        self.parentLoginStd = parent

    def randomGreeting(self):
        greetings = ["Hi, welcome to CardinalAIDS+!",
                     "Hi, I hope you're doing well."]
        self.listWidget.addItem("CardinalAIDS+: "+ random.choice(greetings))
        replies = self.listWidget.findItems("CardinalAIDS+:", QtCore.Qt.MatchStartsWith)
        self.colorReply(replies)

    def comparePass(self):
        if self.newPWText.text() == '' and self.confirmPWText.text() == '':
            self.matchPassword.setVisible(False)
            return
        if self.newPWText.text() == self.confirmPWText.text():
            self.matchPassword.setText('Passwords match.')
            self.matchPassword.setStyleSheet('color: green; background: white')
            self.matchPassword.setVisible(True)
            return
        else:
            self.matchPassword.setText('Passwords do not match.')
            self.matchPassword.setStyleSheet('color: red; background: white')
            self.matchPassword.setVisible(True)

    def colorReply(self, replies):
        if len(replies)>0:
            for reply in replies:
                reply.setForeground(QtGui.QColor("white"))
                reply.setBackground(QtGui.QColor("#cc0000"))
        
    def load_stdData(self, userStd):
        self.historyTable.verticalHeader().setVisible(True)
        self.user = userStd
        self.c.execute("SELECT * FROM history WHERE user=?", (self.user,))
        rows = self.c.fetchall()
        for row in rows:
            inx = rows.index(row)
            self.historyTable.insertRow(inx)
            self.historyTable.setColumnCount(2)
            self.historyTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.historyTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[2]))

    @QtCore.pyqtSlot()
    def chat(self):
        self.question = self.questionText.text()
        checkQues = self.parentLoginStd.checkWhiteSpace(self.question)
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
            self.c.execute("INSERT INTO history (user, questions, answers, validity) VALUES (?,?,?,?)", (self.user, self.question, self.answer, 'valid'))
            self.conn.commit()
            self.questionText.clear()

    @QtCore.pyqtSlot()
    def invalid(self):
        row = self.listWidget.count()
        if row > 2:
            question = self.listWidget.item(row - 2).text().replace('You: ', '')
            answer = self.listWidget.item(row-1).text().replace('CardinalAIDS: ', '')
            self.c.execute("UPDATE history SET validity=(?) WHERE user=? AND questions=? AND answers=?", ('invalid', self.user, question, answer))
            self.conn.commit()

    @QtCore.pyqtSlot()
    def change(self):
        new = self.newPWText.text()
        self.c.execute("SELECT password FROM students WHERE username == ?", (self.user,))
        data = str(self.c.fetchall())
        oldPass = data.translate(str.maketrans({',': '', '(': '', '[': '', ')': '', ']' : '', "'": ''}))
        if self.oldPWText.text() == oldPass:
            if self.newPWText.text() != '' or self.confirmPWText.text() != '':
                if self.newPWText.text() == self.confirmPWText.text():
                    new = self.newPWText.text()
                    self.c.execute("UPDATE students SET password=? WHERE username == ?", (new, self.user))
                    self.conn.commit()
                    self.oldPWText.clear()
                    self.newPWText.clear()
                    self.confirmPWText.clear()
                    self.incorrectChange.setVisible(False)
                    self.matchPassword.setVisible(False)
                else:
                    self.confirmPWText.clear()
            else:
                self.matchPassword.setText('Empty password field(s).')
                self.matchPassword.setStyleSheet('color: red')
                self.matchPassword.setVisible(True)
        else:
            self.oldPWText.clear()
            self.incorrectChange.setVisible(True)

    @QtCore.pyqtSlot()
    def logout(self):
        self.listWidget.clear()
        self.randomGreeting()
        self.tabWidget.setCurrentIndex(0)
        self.historyTable.clearContents()
        self.historyTable.setRowCount(0)
        self.conn.commit()
        self.parentLoginStd.show()
        self.close()

class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):

    conn = sqlite3.connect('CardinalAIDS.db')
    c = conn.cursor()

    def __init__(self, parent=None):
        super(AdminWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(540, 499)
        self.setWindowIcon(QtGui.QIcon('cardinalaidsicon_TZT_icon.ico'))
        self.changeAdBtn.clicked.connect(self.changeAdm)
        self.logoutAdBtn.clicked.connect(self.logout)
        self.addBtn.clicked.connect(self.addStudent)
        self.removeBtn.clicked.connect(self.removeStudent)
        self.updateBtn.clicked.connect(self.updateStudent)
        self.deleteAskedBtn.clicked.connect(self.deleteAskedEntry)
        self.deleteInvalidBtn.clicked.connect(self.deleteInvalidEntry)
        self.oldAdPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newAdPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmAdPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        aHeader = self.askedTable.horizontalHeader()       
        aHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.askedTable.setColumnWidth(1, 50)
        aHeader.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        aVertHeader = self.askedTable.verticalHeader()
        aVertHeader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.askedTable.setHorizontalHeaderLabels(["USER", "QUESTIONS", "ANSWERS"])
        bHeader = self.invalidTable.horizontalHeader()       
        bHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.askedTable.setColumnWidth(1, 50)
        bHeader.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        bVertHeader = self.invalidTable.verticalHeader()
        bVertHeader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.matchAdmPassword.setVisible(False)
        self.incorrectAdmChange.setVisible(False)
        self.updateMessage.setVisible(False)
        self.newAdPWText.textEdited.connect(self.compareAdmPass)
        self.confirmAdPWText.textEdited.connect(self.compareAdmPass)
        self.invalidTable.setHorizontalHeaderLabels(["USER", "QUESTIONS", "ANSWERS"])
        self.parentLoginAdm = parent

    def compareAdmPass(self):
        if self.newAdPWText.text() == '' and self.confirmAdPWText.text() == '':
            self.matchAdmPassword.setVisible(False)
            return
        if self.newAdPWText.text() == self.confirmAdPWText.text():
            self.matchAdmPassword.setText('Passwords match.')
            self.matchAdmPassword.setStyleSheet('color: green; background: white')
            self.matchAdmPassword.setVisible(True)
            return
        else:
            self.matchAdmPassword.setText('Passwords do not match.')
            self.matchAdmPassword.setStyleSheet('color: red; background: white')
            self.matchAdmPassword.setVisible(True)

    def load_askedData(self, userAdm):
        self.askedTable.verticalHeader().setVisible(True)
        self.askedTable.resizeColumnsToContents()
        self.user = userAdm
        self.c.execute("SELECT * FROM history WHERE validity='valid'")
        rows = self.c.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.askedTable.insertRow(inx)
            self.askedTable.setColumnCount(3)
            self.askedTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.askedTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.askedTable.setItem(inx, 2, QtWidgets.QTableWidgetItem(row[2]))

    def load_invalidData(self, userAdm):
        self.invalidTable.verticalHeader().setVisible(True)
        self.user = userAdm
        self.c.execute("SELECT * FROM history WHERE validity='invalid'")
        rows = self.c.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.invalidTable.insertRow(inx)
            self.invalidTable.setColumnCount(3)
            self.invalidTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.invalidTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.invalidTable.setItem(inx, 2, QtWidgets.QTableWidgetItem(row[2]))

    def getInfo(self):
        self.usernameStd = self.updateUserText.text()
        self.passwordStd = self.updatePassText.text()
        self.firstStd = self.updateFirstText.text()
        self.middleStd = self.updateMiddleText.text()
        self.lastStd = self.updateLastText.text()
        self.feesStd = self.updateFeesText.text()
        self.canUpdate = False
        if self.passwordStd != '' or self.firstStd != '' or self.middleStd != '' or self.lastStd != '' or self.feesStd != '':
            self.canUpdate = True
        
        self.updateList = []
        if self.passwordStd != '':
            self.updateList.append('password')
            self.updateList.append(self.passwordStd)
        if self.firstStd != '':
            self.updateList.append('firstName')
            self.updateList.append(self.firstStd)
        if self.middleStd != '':
            self.updateList.append('middleInitial')
            self.updateList.append(self.middleStd)
        if self.lastStd != '':
            self.updateList.append('lastName')
            self.updateList.append(self.lastStd)
        if self.feesStd != '':
            self.updateList.append('unsettled')
            self.updateList.append(self.feesStd)

    def clearInfo(self):
        self.updateUserText.clear()
        self.updatePassText.clear()
        self.updateFirstText.clear()
        self.updateMiddleText.clear()
        self.updateLastText.clear()
        self.updateFeesText.clear()
        self.updateList.clear()

    @QtCore.pyqtSlot()
    def addStudent(self):
        self.getInfo()
        if self.usernameStd == '' or self.passwordStd == '' or self.firstStd == '' or self.middleStd == '' or self.lastStd == '' or self.feesStd == '':
            self.updateMessage.setText('Required field(s) empty.')
            self.updateMessage.setStyleSheet('color: red; background: white')
            self.updateMessage.setVisible(True)
        else:
            self.c.execute("SELECT * FROM students WHERE username=?", (self.usernameStd,))
            data = list(self.c.fetchall())
            if data:
                self.updateMessage.setText('Username already exists.')
                self.updateMessage.setStyleSheet('color: red; background: white')
                self.updateMessage.setVisible(True)
                self.updateUserText.setFocus()
            else:
                self.c.execute("INSERT INTO students (username, password, firstName, middleInitial, lastName, unsettled) VALUES (?,?,?,?,?,?)", (self.usernameStd, self.passwordStd, self.firstStd, self.middleStd, self.lastStd, self.feesStd))
                self.conn.commit()
                self.clearInfo()
                self.updateUserText.setFocus()
                self.updateMessage.setText('Added student info to database.')
                self.updateMessage.setStyleSheet('color: green; background: white')
                self.undoBtn.setEnabled(True)

    @QtCore.pyqtSlot()
    def removeStudent(self):
        self.getInfo()
        if self.usernameStd == '':
            self.updateMessage.setText('Requires username to remove student from database.')
            self.updateMessage.setStyleSheet('color: red; background: white')
            self.updateMessage.setVisible(True)
        else:
            self.c.execute("SELECT * FROM students WHERE username=?", (self.usernameStd,))
            data = list(self.c.fetchall())
            if data:
                self.c.execute("DELETE FROM students WHERE username=?", (self.usernameStd,))
                self.conn.commit()
                self.clearInfo()
                self.updateUserText.setFocus()
                self.updateMessage.setText('Removed student info from database.')
                self.updateMessage.setStyleSheet('color: green; background: white')
                self.updateMessage.setVisible(True)
                self.undoBtn.setEnabled(True)
            else:
                self.updateMessage.setText('Username/Student does not exist.')
                self.updateMessage.setStyleSheet('color: red; background: white')
                self.updateMessage.setVisible(True)
                self.updateUserText.setFocus()

    @QtCore.pyqtSlot()
    def updateStudent(self):
        self.getInfo()
        if self.usernameStd == '' or not self.canUpdate:
            print(self.usernameStd)
            print(self.canUpdate)
            self.updateMessage.setText('Requires username and another entry to update student info in database.')
            self.updateMessage.setStyleSheet('color: red; background: white')
            self.updateMessage.setVisible(True)
        else:
            self.c.execute("SELECT * FROM students WHERE username=?", (self.usernameStd,))
            data = list(self.c.fetchall())
            if data:
                query = 'UPDATE students SET '
                counter = 0
                while counter < len(self.updateList):
                    query = query + str(self.updateList[counter]) + '=? WHERE username=?'
                    self.c.execute(query, (self.updateList[counter+1], self.usernameStd))
                    conn.commit()
                    query = 'UPDATE students SET '
                    counter = counter + 2          
                self.conn.commit()
                self.clearInfo()
                self.updateUserText.setFocus()
                self.updateMessage.setText('Updated student info from database.')
                self.updateMessage.setStyleSheet('color: green; background: white')
                self.updateMessage.setVisible(True)
                self.undoBtn.setEnabled(True)
            else:
                self.updateMessage.setText('Username/Student does not exist.')
                self.updateMessage.setStyleSheet('color: red; background: white')
                self.updateMessage.setVisible(True)
                self.updateUserText.setFocus()

    @QtCore.pyqtSlot()
    def deleteAskedEntry(self):
        indexList = []
        indexes = self.askedTable.selectionModel().selectedRows()

        for index in sorted(indexes):
            user = index.sibling(index.row(),index.column()).data()
            question = index.sibling(index.row(),index.column() + 1).data()
            answer = index.sibling(index.row(),index.column() + 2).data()
            row = QtCore.QPersistentModelIndex(index)         
            indexList.append(row)   
            self.c.execute('DELETE FROM history WHERE user=? and questions=? and answers=?', (user, question, answer))
            self.conn.commit()

        for rowIndex in indexList:                                      
            self.askedTable.removeRow(rowIndex.row())

    @QtCore.pyqtSlot()
    def deleteInvalidEntry(self):
        indexList = []
        indexes = self.invalidTable.selectionModel().selectedRows()
        
        for index in sorted(indexes):
            user = index.sibling(index.row(),index.column()).data()
            question = index.sibling(index.row(),index.column() + 1).data()
            answer = index.sibling(index.row(),index.column() + 2).data()
            row = QtCore.QPersistentModelIndex(index)         
            indexList.append(row)   
            self.c.execute('DELETE FROM history WHERE user=? and questions=? and answers=?', (user, question, answer))
            self.conn.commit()

        for rowIndex in indexList:                                      
            self.invalidTable.removeRow(rowIndex.row())

    @QtCore.pyqtSlot()
    def changeAdm(self):
        new = self.newAdPWText.text()
        self.c.execute("SELECT password FROM admins WHERE username == ?", (self.user,))
        data = str(self.c.fetchall())
        oldPass = data.translate(str.maketrans({',': '', '(': '', '[': '', ')': '', ']' : '', "'": ''}))
        if self.oldAdPWText.text() == oldPass:
            if self.newAdPWText.text() != '' or self.confirmAdPWText.text() != '':
                if self.newAdPWText.text() == self.confirmAdPWText.text():
                    new = self.newAdPWText.text()
                    self.c.execute("UPDATE admins SET password=? WHERE username == ?", (new, self.user))
                    self.conn.commit()
                    self.oldAdPWText.clear()
                    self.newAdPWText.clear()
                    self.confirmAdPWText.clear()
                    self.incorrectAdmChange.setVisible(False)
                    self.matchAdmPassword.setVisible(False)
                else:
                    self.confirmAdPWText.clear()
            else:
                self.matchAdmPassword.setText('Empty password field(s).')
                self.matchAdmPassword.setStyleSheet('color: red')
                self.matchAdmPassword.setVisible(True)
        else:
            self.oldAdPWText.clear()
            self.incorrectAdmChange.setVisible(True)

    @QtCore.pyqtSlot()
    def logout(self):
        conn.commit()
        self.tabWidget.setCurrentIndex(0)
        self.askedTable.clearContents()
        self.invalidTable.clearContents()
        self.askedTable.setRowCount(0)
        self.invalidTable.setRowCount(0)
        self.parentLoginAdm.show()
        self.close()

class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):

    conn = sqlite3.connect('CardinalAIDS.db')
    c = conn.cursor()

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
        self.setWindowIcon(QtGui.QIcon('cardinalaidsicon_TZT_icon.ico'))
        tabFocus = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Tab), self)
        tabFocus.activated.connect(self.changeFocus)

    @QtCore.pyqtSlot()
    def changeFocus(self):
        self.focusNextChild()

    def clearWindow(self):
        self.incorrrectLbl.setVisible(False)
        self.incorrrecAdmLbl.setVisible(False)
        self.passText.clear()
        self.passAdText.clear()

    def checkWhiteSpace(self, word):
        checker = True
        if word.isspace() or word == '':
            checker = False
        else:
            checker = True
        return checker

    @QtCore.pyqtSlot()
    def authenticateStd(self):
        userStd = self.userText.text()
        passStd = self.passText.text()
        checkUser = self.checkWhiteSpace(userStd)
        checkPass = self.checkWhiteSpace(passStd)
        if checkUser and checkPass:
            a = list(c.execute("SELECT * FROM students WHERE username=? and password=?", (userStd, passStd)))
            if a:
                self.clearWindow()
                self.userAdText.clear()
                self.student = StudentWindow(self)
                self.student.load_stdData(userStd)
                self.student.historyTable.resizeRowsToContents()            
                self.student.show()
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
                self.clearWindow()
                self.userText.clear()
                self.admin = AdminWindow(self)
                self.admin.load_askedData(userAdm)
                self.admin.load_invalidData(userAdm)
                self.admin.askedTable.resizeRowsToContents()         
                self.admin.invalidTable.resizeRowsToContents()
                self.admin.show()
                self.hide()
            else:
                self.passAdText.clear()    
                self.incorrrecAdmLbl.setVisible(True)
        else:
            self.userAdText.clear()
            self.passAdText.clear()   
            

def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
