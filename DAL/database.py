import sqlite3
import sys
sys.path.append("../CardinalAIDSplus")

class Database():
    def __init__(self):
        self.conn = sqlite3.connect('./DAL/CardinalAIDS.db')
        self.c = self.conn.cursor()

    def addToStudents(self, username, password, fname, midinitial, lname, fees):
        self.c.execute("INSERT INTO students VALUES (?,?,?,?,?,?)", (username, password, fname, midinitial, lname, fees))
        self.conn.commit()

    def delFromStudents(self,username):
        self.c.execute("DELETE FROM students WHERE username=?", (username,))
        self.conn.commit()

    def updateStudents(self, username, updateList):
        counter = 0
        while counter < len(updateList) - 1:
            query = "UPDATE students SET "
            query = query + str(updateList[counter]) + "=? WHERE username=?"
            self.c.execute(query, (updateList[counter+1], username))
            self.conn.commit()
            counter = counter + 1

    def checkStudent(self, username):
        self.c.execute("SELECT * FROM students WHERE username=?", (username,))
        if list(self.c.fetchall()):
            return True
        else:
            return False

    def checkPassword(self, username, password, user):
        check = list(self.c.execute("SELECT * FROM " + user + " WHERE username=? and password=?", (username, password)))
        if check:
            return True
        else:
            return False

    def changePassword(self,username, user, old, new):
        if self.checkPassword(username, old, user):
            query = "UPDATE " + user + " SET password=? WHERE username=?"
            self.c.execute(query, (new, username))
            self.conn.commit()
        else:
            return False

    def loadStudentTableData(self,username):
        self.c.execute("SELECT * FROM history WHERE user=?", (username,))
        data = self.c.fetchall()
        return data

    def loadAdminTableData(self,validity):
        self.c.execute("SELECT * FROM history WHERE validity=?", (validity,))
        data = self.c.fetchall()
        return data
        
    def makeInvalid(self, username, question, answer):
        self.c.execute("UPDATE history SET validity=(?) WHERE user=? AND questions=? AND answers=?", ('invalid', username, question, answer))
        self.conn.commit()

    def deleteTableData(self, username, question, answer):
        self.c.execute('DELETE FROM history WHERE user=? and questions=? and answers=?', (username, question, answer))
        self.conn.commit()

    def addToHistory(self, username, question, answer):
        self.c.execute("INSERT INTO history (user, questions, answers, validity) VALUES (?,?,?,?)", (username, question, answer, 'valid'))
        self.conn.commit()

    def getStudentInfo(self, username):
        self.c.execute("SELECT * FROM students WHERE username=?", (username,))
        data = self.c.fetchall()
        return data

    def getScholarshipList(self):
        self.c.execute("SELECT name FROM scholarships")
        data = list(self.c.fetchall())
        return data

    def getScholarship(self, code):
        self.c.execute("SELECT * FROM scholarships WHERE code == ?",(code,))
        data = self.c.fetchall()
        return data

    def getEnrollment(self, number):
        self.c.execute("SELECT * FROM enrollmentsched WHERE number == ?",(number,))
        data = self.c.fetchall()
        return data

    def getConsultation(self, number):
        self.c.execute("SELECT * FROM consultationsched WHERE number == ?",(number,))
        data = self.c.fetchall()
        return data
    
    def getContact(self, code):
        self.c.execute("SELECT * FROM contactlist WHERE code == ?",(code,))
        data = self.c.fetchall()
        return data

    def getProfSched(self, prof):
        self.c.execute("SELECT * FROM profSched WHERE code == ?",(prof,))
        data = self.c.fetchall()
        return data

    def getNews(self, code):
        self.c.execute("SELECT * FROM news WHERE code == ?",(code,))
        data = self.c.fetchall()
        return data

    def closeDatabase(self):
        self.conn.commit()
        self.conn.close()

