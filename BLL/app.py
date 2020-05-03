import sys
sys.path.append("../CardinalAIDSplus")
import random
from PyQt5 import QtWidgets, QtCore, QtGui
from UI.mainUi import Ui_MainWindow
from UI.login import Ui_LoginWindow
from DAL.database import Database
from bot import AIchat

import ctypes                                                           # allows for the taskbar icon image to appear
myappid = u'mycompany.myproduct.subproduct.version'                     # known problem with pyqt and windows;
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)  # will be ignored in linux systems

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, username='', user='', parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(540, 499)
        self.setWindowIcon(QtGui.QIcon('./UI/CardinalAIDS-icofile.ico'))
        
        self.username = username
        self.user = user
        self.db = Database()

        # store tab references for dynamic changing of main window tabs
        self.resetTabRef = self.cardinalTabWidget
        self.chatTabRef = self.chatTab
        self.historyTabRef = self.historyTab
        self.askedTabRef = self.askedTab
        self.invalidTabRef = self.invalidTab
        self.updateTabRef = self.updateTab
        self.accTabRef = self.accTab

        # button connections to functions
        self.logoutBtn.clicked.connect(self.logout)
        self.sendBtn.clicked.connect(self.chat)
        self.changePW.clicked.connect(self.change)
        self.invalidBtn.clicked.connect(self.invalid)
        self.deleteAskedBtn.clicked.connect(self.deleteAskedEntry)
        self.deleteInvalidBtn.clicked.connect(self.deleteInvalidEntry)
        self.addBtn.clicked.connect(self.addStudent)
        self.removeBtn.clicked.connect(self.removeStudent)
        self.updateBtn.clicked.connect(self.updateStudent)

        # connect pw text boxes to message to detect changes
        self.oldPWText.textEdited.connect(self.checkPW)
        self.newPWText.textEdited.connect(self.checkPW)
        self.confirmPWText.textEdited.connect(self.checkPW)

        # mask the password textboxes
        self.oldPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPWText.setEchoMode(QtWidgets.QLineEdit.Password)
        
        # widgets' parameters
        self.listWidget.setWordWrap(True)
        self.matchPassword.setVisible(False)
        self.incorrectChange.setVisible(False)
        self.updateMessage.setVisible(False)
        histHeader = self.historyTable.horizontalHeader()
        self.historyTable.setColumnCount(2)       
        histHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        histHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.historyTable.setHorizontalHeaderLabels(["QUESTIONS", "ANSWERS"])
        self.askedTable.verticalHeader().setVisible(True)
        self.askedTable.setColumnCount(3)
        self.askedTable.resizeColumnsToContents()
        askedHeader = self.askedTable.horizontalHeader()       
        askedHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        askedHeader.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        askedVertHeader = self.askedTable.verticalHeader()
        askedVertHeader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        invalidHeader = self.invalidTable.horizontalHeader()       
        invalidHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.askedTable.setColumnWidth(1, 60)
        self.invalidTable.verticalHeader().setVisible(True)
        self.invalidTable.setColumnCount(3)
        invalidHeader.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        invalidVertHeader = self.invalidTable.verticalHeader()
        invalidVertHeader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.invalidTable.setHorizontalHeaderLabels(["USER", "QUESTIONS", "ANSWERS"])
        self.askedTable.setHorizontalHeaderLabels(["USER", "QUESTIONS", "ANSWERS"])
        self.invalidTable.setColumnWidth(1, 60)

        # begin interface with login
        self.showLogin()

    # sets the tabs in the widget for a student login/user 
    @QtCore.pyqtSlot(str, str)
    def studentUser(self, std, user):
        self.username = std
        self.user = user
        self.bot = AIchat(self.username)
        self.giveGreeting()
        self.cardinalTabWidget.removeTab(2)
        self.cardinalTabWidget.removeTab(2)
        self.cardinalTabWidget.removeTab(2)
        self.load_stdData()                 # loads the history of the student's chats

    # sets the tabs in the widget for an admin login/user 
    @QtCore.pyqtSlot(str, str)
    def adminUser(self, adm, user):
        self.username = adm
        self.user = user
        self.cardinalTabWidget.removeTab(0)
        self.cardinalTabWidget.removeTab(0)
        self.load_askedData()               # loads the valid history of all student chats
        self.load_invalidData()             # loads the invalid history of the all student chats

    # shows the login
    def showLogin(self):
        login = LoginWindow(self.username, self.user)
        login.stdAccept.connect(self.studentUser)
        login.admAccept.connect(self.adminUser)
        if login.exec_() == QtWidgets.QDialog.Accepted:
            self.show()

    # clears tabs and resets them using references
    def resetTabs(self):
        self.cardinalTabWidget.clear()
        self.cardinalTabWidget.insertTab(0, self.chatTabRef, 'CHAT')
        self.cardinalTabWidget.insertTab(1, self.historyTabRef, 'HISTORY')
        self.cardinalTabWidget.insertTab(2, self.askedTabRef, 'ASKED QUESTIONS')
        self.cardinalTabWidget.insertTab(3, self.invalidTabRef, 'INVALID ANSWERS')
        self.cardinalTabWidget.insertTab(4, self.updateTabRef, 'UPDATE STUDENT INFO')
        self.cardinalTabWidget.insertTab(5, self.accTabRef, 'ACCOUNT')

    # first chat of the bot; greets the student
    def giveGreeting(self):
        self.listWidget.addItem("CardinalAIDS+: "+ self.bot.randomGreeting())
        replies = self.listWidget.findItems("CardinalAIDS+:", QtCore.Qt.MatchStartsWith)
        self.colorReply(replies)

    # changes the color of the bot's replies to distinguish messages
    def colorReply(self, replies):
        if len(replies)>0:
            for reply in replies:
                reply.setForeground(QtGui.QColor("white"))
                reply.setBackground(QtGui.QColor("#cc0000"))

    # prevents entering empty/no values in text boxes
    def checkWhiteSpace(self, word):
        checker = True
        if word.isspace() or word == '':
            checker = False
        else:
            checker = True
        return checker

    # accesses the database to get info and display it in the UI
    def load_stdData(self):
        self.historyTable.verticalHeader().setVisible(True)
        rows = self.db.loadStudentTableData(self.username)
        for row in rows:
            inx = rows.index(row)
            self.historyTable.insertRow(inx)
            self.historyTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.historyTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[2]))

    # next two functions used for admin users
    def load_askedData(self):
        rows = self.db.loadAdminTableData('valid')
        for row in rows:
            inx = rows.index(row)
            self.askedTable.insertRow(inx)
            self.askedTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.askedTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.askedTable.setItem(inx, 2, QtWidgets.QTableWidgetItem(row[2]))

    def load_invalidData(self):
        rows = self.db.loadAdminTableData('invalid')
        for row in rows:
            inx = rows.index(row)
            self.invalidTable.insertRow(inx)
            self.invalidTable.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.invalidTable.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.invalidTable.setItem(inx, 2, QtWidgets.QTableWidgetItem(row[2]))

    @QtCore.pyqtSlot() # processes the chat, adds in the list and the database
    def chat(self):
        self.question = self.questionText.text()
        checkQues = self.checkWhiteSpace(self.question)
        if checkQues:
            self.listWidget.addItem("You: "+self.question)
            self.answer = self.bot.getQues(self.question)
            self.listWidget.addItem("CardinalAIDS: "+self.answer)
            replies = self.listWidget.findItems("CardinalAIDS:", QtCore.Qt.MatchStartsWith)
            self.colorReply(replies)
            numRows = self.historyTable.rowCount()
            self.historyTable.insertRow(numRows)
            self.historyTable.setItem(numRows, 0, QtWidgets.QTableWidgetItem(self.question))
            self.historyTable.setItem(numRows, 1, QtWidgets.QTableWidgetItem(self.answer))
            self.historyTable.resizeRowsToContents()
            self.db.addToHistory(self.username, self.question, self.answer)
            self.questionText.clear()

    @QtCore.pyqtSlot() # sets the last two messages (question and answer) as invalid
    def invalid(self):
        row = self.listWidget.count()
        if row > 2:
            question = self.listWidget.item(row - 2).text().replace('You: ', '')
            answer = self.listWidget.item(row-1).text().replace('CardinalAIDS: ', '')
            self.db.makeInvalid(self.username, question, answer)

    @QtCore.pyqtSlot() # admin use; deletes entry when a row is selected
    def deleteAskedEntry(self):
        indexList = []
        indexes = self.askedTable.selectionModel().selectedRows()

        for index in sorted(indexes):
            user = index.sibling(index.row(),index.column()).data()
            question = index.sibling(index.row(),index.column() + 1).data()
            answer = index.sibling(index.row(),index.column() + 2).data()
            row = QtCore.QPersistentModelIndex(index)         
            indexList.append(row)   
            self.db.deleteTableData(user, question, answer)

        for rowIndex in indexList:                                      
            self.askedTable.removeRow(rowIndex.row())

    @QtCore.pyqtSlot() # admin use; deletes entry when a row is selected
    def deleteInvalidEntry(self):
        indexList = []
        indexes = self.invalidTable.selectionModel().selectedRows()
        
        for index in sorted(indexes):
            user = index.sibling(index.row(),index.column()).data()
            question = index.sibling(index.row(),index.column() + 1).data()
            answer = index.sibling(index.row(),index.column() + 2).data()
            row = QtCore.QPersistentModelIndex(index)         
            indexList.append(row)   
            self.db.deleteTableData(user, question, answer)

        for rowIndex in indexList:                                      
            self.invalidTable.removeRow(rowIndex.row())

    # retrieves info for adding, removing, updating student info
    def getStudentInfo(self):
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

    # changes update message colors and visibility
    def messageColors(self, message, check):
        if check:
            message.setStyleSheet('color: green; background: white')
        else:
            message.setStyleSheet('color: red; background: white')
        message.setVisible(True)
            
    @QtCore.pyqtSlot() # adds student to database with data from text fields
    def addStudent(self):
        self.getStudentInfo()
        if self.usernameStd == '' or self.passwordStd == '' or self.firstStd == '' or self.middleStd == '' or self.lastStd == '' or self.feesStd == '':
            self.updateMessage.setText('Required field(s) empty.')
            self.messageColors(self.updateMessage, False)
        else:
            existStd = self.db.checkStudent(self.usernameStd)
            if existStd:
                self.updateMessage.setText('Username already exists.')
                self.messageColors(self.updateMessage, False)
                self.updateUserText.setFocus()
            else:
                self.db.addToStudents(self.usernameStd, self.passwordStd, self.firstStd, self.middleStd, self.lastStd, self.feesStd)
                self.clearInfo()
                self.updateUserText.setFocus()
                self.updateMessage.setText('Added student info to database.')
                self.messageColors(self.updateMessage, True)

    @QtCore.pyqtSlot() # deletes a student's info from the database using their username
    def removeStudent(self):
        self.getStudentInfo()
        if self.usernameStd == '':
            self.updateMessage.setText('Requires username to remove student from database.')
            self.messageColors(self.updateMessage, False)
        else:
            existStd = self.db.checkStudent(self.usernameStd)
            if existStd:
                self.db.delFromStudents(self.usernameStd)
                self.clearInfo()
                self.updateUserText.setFocus()
                self.updateMessage.setText('Removed student info from database.')
                self.messageColors(self.updateMessage, True)
            else:
                self.updateMessage.setText('Username/Student does not exist.')
                self.messageColors(self.updateMessage, False)
                self.updateUserText.setFocus()

    @QtCore.pyqtSlot() # updates a student's info by getting username and at least one field
    def updateStudent(self):
        self.getStudentInfo()
        if self.usernameStd == '' or not self.canUpdate:
            self.updateMessage.setText('Requires username and another entry to update student info in database.')
            self.messageColors(self.updateMessage, False)
        else:
            existStd = self.db.checkStudent(self.usernameStd)
            if existStd:
                self.db.updateStudents(self.usernameStd, self.updateList)
                self.clearInfo()
                self.updateUserText.setFocus()
                self.updateMessage.setText('Updated student info from database.')
                self.messageColors(self.updateMessage, True)
            else:
                self.updateMessage.setText('Username/Student does not exist.')
                self.messageColors(self.updateMessage, False)
                self.updateUserText.setFocus()

    def checkPW(self): # checks if passwords entered are valid and displays messages
        check = False
        self.old = self.oldPWText.text()
        self.new = self.newPWText.text()
        if self.db.checkPassword(self.username, self.old, self.user):
            self.incorrectChange.setText("Current password correct.")
            self.messageColors(self.incorrectChange, True)
            if self.newPWText.text() != '' or self.confirmPWText.text() != '':
                if self.newPWText.text() == self.confirmPWText.text():
                    check = True
                    self.matchPassword.setText("Passwords match.")
                    self.messageColors(self.matchPassword, True)
                else:
                    check = False
                    if self.newPWText.text() == '' or self.confirmPWText.text() == '':
                        self.matchPassword.setText('Empty password field(s).')
                        self.messageColors(self.matchPassword, False)
                    else:
                        self.matchPassword.setText("Passwords do not match.")
                        self.messageColors(self.matchPassword, False)
            else:
                check = False
                self.matchPassword.setText('Empty password field(s).')
                self.messageColors(self.matchPassword, False)
        else:
            check = False
            self.incorrectChange.setText("Current password incorrect.")
            self.messageColors(self.incorrectChange, False)
        return check

    @QtCore.pyqtSlot() # handles the change of passwords by students and admins
    def change(self):
        if self.checkPW:
            self.db.changePassword(self.username, self.user, self.old, self.new)
            self.oldPWText.clear()
            self.newPWText.clear()
            self.confirmPWText.clear()
            self.incorrectChange.setVisible(False)
            self.matchPassword.setVisible(False)
            

    # resets tabs, tables within and messages
    def cleanUp(self):
        self.resetTabs()
        self.cardinalTabWidget.setCurrentIndex(0)
        self.historyTable.clearContents()
        self.historyTable.setRowCount(0)
        self.askedTable.clearContents()
        self.invalidTable.clearContents()
        self.askedTable.setRowCount(0)
        self.invalidTable.setRowCount(0)
        self.updateMessage.setVisible(False)

    @QtCore.pyqtSlot() # logout function; resets main window and call login again
    def logout(self):
        self.cleanUp()
        self.close()   
        self.showLogin()
 
class LoginWindow(QtWidgets.QDialog, Ui_LoginWindow):
    stdAccept = QtCore.pyqtSignal(str, str)
    admAccept = QtCore.pyqtSignal(str, str)

    def __init__(self, username='', user='', parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(341, 481)

        # icons and images
        self.setWindowIcon(QtGui.QIcon('./UI/CardinalAIDS-icofile.ico'))
        self.logo.setPixmap(QtGui.QPixmap('./UI/CardinalAIDS-full.jpg'))
        self.logoAdmin.setPixmap(QtGui.QPixmap('./UI/CardinalAIDS-full.jpg'))
        self.logo_3.setPixmap(QtGui.QPixmap('./UI/CardinalAIDS-full.jpg'))

        # connects the login buttons to respective functions
        self.loginBtn.clicked.connect(self.authenticateStd)
        self.loginAdBtn.clicked.connect(self.authenticateAdm)

        # masks the password text fields
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passAdText.setEchoMode(QtWidgets.QLineEdit.Password)

        # enables the use of the 'ENTER' key to activate function
        self.userText.returnPressed.connect(self.authenticateStd)
        self.passText.returnPressed.connect(self.authenticateStd)
        self.userAdText.returnPressed.connect(self.authenticateAdm)
        self.passAdText.returnPressed.connect(self.authenticateAdm)
        
        # enables use of the 'TAB' key to move between widgets/elements in the window
        tabFocus = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Tab), self)
        tabFocus.activated.connect(self.changeFocus)

        # messages initially not visible 
        self.incorrrectLbl.setVisible(False)
        self.incorrrecAdmLbl.setVisible(False)

        #initialize database
        self.db = Database()
        if user == 'students':                  # applicable after logging out and seeing login screen
            self.userText.setText(username)     # puts the previous username on text field and 
            self.passText.setFocus()            # sets the current tab to recent user
            self.tabWidget.setCurrentIndex(0)
        if user == 'admins':
            self.userAdText.setText(username)
            self.passAdText.setFocus()
            self.tabWidget.setCurrentIndex(1)

    @QtCore.pyqtSlot() # called by 'TAB' keypress to allow next focus on widget/element
    def changeFocus(self):
        self.focusNextChild()

    # prevents entering empty/no values in text boxes
    def checkWhiteSpace(self, word):
        checker = True
        if word.isspace() or word == '':
            checker = False
        else:
            checker = True
        return checker

    # gets the student info from respective text fields
    def getStudentInfo(self, username, password):
        username = self.userText.text()
        password = self.passText.text()

    # gets the student info from respective text fields
    def getAdminInfo(self, username, password):
        username = self.userAdText.text()
        password = self.passAdText.text()

    @QtCore.pyqtSlot() # function for logging in a student account
    def authenticateStd(self):
        userStd = self.userText.text()
        passStd = self.passText.text()
        checkUser = self.checkWhiteSpace(userStd)
        checkPass = self.checkWhiteSpace(passStd)
        if checkUser and checkPass:
            if self.db.checkPassword(userStd, passStd, 'students'):
                self.stdAccept.emit(userStd, 'students')
                self.accept()
            else:
                self.passText.clear()
                self.incorrrectLbl.setVisible(True)
        else:
            self.userText.clear()
            self.passText.clear()
            self.incorrrectLbl.setVisible(True)

    @QtCore.pyqtSlot() # function for logging in an admin account
    def authenticateAdm(self):
        userAdm = self.userAdText.text()
        passAdm = self.passAdText.text()
        checkAdmUser = self.checkWhiteSpace(userAdm)
        checkAdmPass = self.checkWhiteSpace(passAdm)
        if checkAdmUser and checkAdmPass:
            if self.db.checkPassword(userAdm, passAdm, 'admins'):
                self.admAccept.emit(userAdm, 'admins')
                self.accept()
            else:
                self.passAdText.clear()    
                self.incorrrecAdmLbl.setVisible(True)
        else:
            self.userAdText.clear()
            self.passAdText.clear()
            self.incorrrecAdmLbl.setVisible(True)

def main(): # function of main program
    try:
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = MainWindow() # initializes main window but login will show first
        sys.exit(app.exec_())
    finally:
        db = Database()    # terminates database by instantiating and closing manually
        db.closeDatabase()

if __name__ == '__main__':
    main()