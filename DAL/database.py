import sqlite3

conn = sqlite3.connect('CardinalAIDS.db')
c = conn.cursor()

def addToStudents(username, password, fname, midinitial, lname, fees):
    c.execute("INSERT INTO students VALUES (?,?,?,?,?,?)", (username, password, fname, midinitial, lname, fees))
    conn.commit()
    conn.close()

def delFromStudents(username):
    c.execute("DELETE FROM students WHERE username=?", (username,))
    conn.commit()
    conn.close()

def updateStudents(username, updateList):
    counter = 0
    while counter < len(updateList):
        query = "UPDATE students SET "
        query = query + str(updateList[counter]) + "=? WHERE username=?"
        c.execute(query, (updateList[counter+1], username))
        conn.commit()

def checkPassword(username, password, user):
    check = list(c.execute("SELECT * FROM " + user + " WHERE username=? and password=?", (username, password)))
    if check:
        return True
    else:
        return False

def changePassword(username, user, current, new):
    if checkPassword(username, current, user):
        query = "UPDATE " + user + " SET password=? WHERE username=?"
        c.execute(query, (new, username))
        conn.commit()
    else:
        return False

def loadStudentTableData(username):
    c.execute("SELECT * FROM history WHERE user=?", (username,))
    data = c.fetchall()
    return data

def loadAdminTableData(validity):
    c.execute("SELECT * FROM history WHERE validity=?", (validity,))
    data = c.fetchall()
    return data
    
def makeInvalid(username, question, answer):
    c.execute("UPDATE history SET validity=(?) WHERE user=? AND questions=? AND answers=?", ('invalid', username, question, answer))
    conn.commit()

def deleteTableData(username, question, answer):
    c.execute('DELETE FROM history WHERE user=? and questions=? and answers=?', (username, question, answer))
    conn.commit()

def addToHistory(username, question, answer):
    c.execute("INSERT INTO history (user, questions, answers, validity) VALUES (?,?,?,?)", (username, question, answer, 'valid'))
    conn.commit()

conn.commit()