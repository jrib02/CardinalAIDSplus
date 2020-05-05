import sqlite3
import random

conn = sqlite3.connect('CardinalAIDS.db')
c = conn.cursor()


usernameInput = input("Username: ")
passwordInput = input("Password: ")
    
c.execute("SELECT * FROM students WHERE username == ?",(usernameInput,))    
data = c.fetchall()
    
for entry in data:
    username = entry[0]
    password = entry[1]
    firstName = entry[2]
    middle = entry[3]
    lastName = entry[4]
    unsettled = entry[5]
    
if passwordInput == password:
    print("Welcome to CardinalAIDS+! \n")
    # OPEN NEW WINDOW

class AIchat():
    
    def convert(lst):
        return ''.join(lst).split()
    
    def unsettledFees():
        return print("Unsettled charges for " + lastName + ", "+ firstName +" "+ middle + ". amounts to: " + str(unsettled))
    
    def scholarship(lst1):
        def fallback():
            fallbackOptions = ["Can you be more specific for me?",
                     "I don't quite get what you're asking about scholarships.",
                     "Can you be more specific on scholarships?"]
            return print(random.choice(fallbackOptions))

        for x in range (0,len(lst1)):
            if x == len(lst1)-1:
                fallback()
                return
            elif lst1[x] == "keb" or lst1[x] == "hana" or lst1[x] == "kebhana":
                code = "keb"
                break
            elif lst1[x] == "refinitiv":
                code = "refinitiv"
                break
            elif lst1[x] == "maasd" or lst1[x] == "san" or lst1[x] == "diego" or lst1[x] == "sandiego" or lst1[x] == "alumni":
                code = "maasd"
                break
            elif lst1[x] == "ety" or lst1[x] == "et" or lst1[x] == "yuchengco":
                code = "ety"
                break
            elif lst1[x] == "list" or lst1[x] == "available" or lst1[x] == "all":
                print("Here are the available scholarships: \n")
                c.execute("SELECT name FROM scholarships")
                data = c.fetchall()
                for entry in data:
                    print(entry[0])
                return
            else:
                x = x + 1
        
        c.execute("SELECT * FROM scholarships WHERE code == ?",(code,))
        data = c.fetchall()
        
        for entry in data:
            code = entry[0]
            name = entry[1]
            deadline = entry[2]
            status = entry[3]
            requirements = entry[4]
        
        if deadline == "no data":
            response = print("The " + name + " is " + status)
        else:
            response = print("The " + name + " is deadlined until " + deadline)
        
        return response
    
    def schedEnroll(lst1):
        def fallback():
            fallbackOptions = ["You have either entered an invalid batch number or didn't specify one. Could you specify a valid batch number? ", 
                               "I don't think you've entered a valid batch number. Can you re-enter that?", 
                               "Please enter a valid batch number."]
            return print(random.choice(fallbackOptions))
        
        for x in range(0,len(lst1)+1):
            if x == len(lst1):
                fallback()
                return
            if (lst1[x].isdigit()):
                if int(lst1[x]) <= 2014 and int(lst1[x]) >= 2008:
                    number = 1
                    break
            if lst1[x] == "2015" or lst1[x] == "2016" or lst1[x] == "2017" or lst1[x] == "17" or lst1[x] == "16" or lst1[x] == "15":
                number = 2
                break
            if lst1[x] == "2018" or lst1[x] == "18":
                number = 3
                break
            if lst1[x] == "2019" or lst1[x] == "19":
                number = 4
                break
            else:
                x = x + 1
                
        c.execute("SELECT * FROM enrollmentsched WHERE number == ?",(number,))
        data = c.fetchall()
        
        for entry in data:
            number = entry[0]
            batch = entry[1]
            date = entry[2]
            time = entry[3]
        response = print("The schedule of enrollment for Batch " + str(batch) + " is on " + date + " from " + time + " for all programs.")
        
        return response
    
    
    def schedConsult(lst1):
        def fallback():
            fallbackOptions = ["You have either entered an invalid batch number or didn't specify one. Could you specify a valid batch number? ", 
                               "I don't think you've entered a valid batch number. Can you re-enter that?", 
                               "Please enter a valid batch number."]
            return print(random.choice(fallbackOptions))

        for x in range(0,len(lst1)+1):
            if x == len(lst1):
                fallback()
                return
            
            if (lst1[x].isdigit()):
                if int(lst1[x]) <= 2014 and int(lst1[x]) >= 2008:
                    number = 1
                    break
    
            if lst1[x] == "2015" or lst1[x] == "2016" or lst1[x] == "2017" or lst1[x] == "17" or lst1[x] == "16" or lst1[x] == "15":
                number = 2
                break
            if lst1[x] == "2018" or lst1[x] == "18":
                number = 3
                break
            if lst1[x] == "2019" or lst1[x] == "19":
                number = 4
                break
            else:
                x = x + 1
            
        c.execute("SELECT * FROM consultationsched WHERE number == ?",(number,))
        data = c.fetchall()    
            
        for entry in data:
            number = entry[0]
            batch = entry[1]
            date = entry[2]
            time = entry[3]
        response = print("The schedule of consultations for Batch " + str(batch) + " is on " + date + " from " + time + " for all programs.")
        return response
    
    
    def contact(lst1):
        for x in range (0,len(lst1)):
            if lst1[x] == "registrar":
                code = "registrar"
            if lst1[x] == "treasurer" or lst1[x] == "treasury" or lst1[x] == "treasurers":
                code = "treasury"
            if lst1[x] == "admissions" or lst1[x] == "admission":
                code = "admissions"
            if lst1[x] == "bookstore" or lst1[x] == "store":
                code = "bookstore"
            if lst1[x] == "cdmo" or lst1[x] == "maintenance":
                code = "cdmo"
            if lst1[x] == "pe":
                code = "pe"
            if lst1[x] == "math" or lst1[x] == "mathematics":
                code = "math"
            if lst1[x] == "physics":
                code = "physics"
            if lst1[x] == "doit" or lst1[x] == "development" or lst1[x] == "it":
                code = "doit"
            if lst1[x] == "etybsm" or lst1[x] == "business" or lst1[x] == "yuchengco":
                code = "etybsm"
            if lst1[x] == "aridbe" or lst1[x] == "architecture":
                code = "aridbe"
            if lst1[x] == "cege" or lst1[x] == "civil" or lst1[x] == "geological" or lst1[x] == "environmental":
                code = "cege"
            if lst1[x] == "cbmes" or lst1[x] == "chem" or lst1[x] == "chemical" or lst1[x] == "biological" or lst1[x] == "materials":
                code = "cbmes"
            if lst1[x] == "eece" or lst1[x] == "electrical" or lst1[x] == "electronics" or lst1[x] == "computer" or lst1[x] == "cpe" or lst1[x] == "ee" or lst1[x] == "ece":
                code = "eece"
            if lst1[x] == "gs" or lst1[x] == "graduate":
                code = "gs"
            if lst1[x] == "ie-emg" or lst1[x] == "ieemg" or lst1[x] == "management" or lst1[x] == "industrial" or lst1[x] == "ie" or lst1[x] == "mfge":
                code = "ie-emg"
            if lst1[x] == "soit":
                code = "soit"
            if lst1[x] == "mme" or lst1[x] == "mechanical" or lst1[x] == "manufacturing":
                code = "mme"
            if lst1[x] == "sms" or lst1[x] == "media":
                code = "sms"
            if lst1[x] == "ssse" or lst1[x] == "social" or lst1[x] == "education":
                code = "ssse"  
            if lst1[x] == "dal" or lst1[x] == "arts" or lst1[x] == "letters":
                code = "dal"  
            else:
                x = x + 1
    
        c.execute("SELECT * FROM contactlist WHERE code == ?",(code,))
        data = c.fetchall()
        
        for entry in data:
            code = entry[0]
            department = entry[1]
            contact = entry[2]
            email = entry[3]
        
        print("Contact number of " + department + " is " + str(contact))
        print ("Available email of " + department + " is " + email)
    
    def randomAsk():
        askResponses = ["What can I do for you?",
                        "What kind of assistance can I give?",
                        "What brought you to me?"]
        return random.choice(askResponses)
    
    def randomGreeting():
        greetings = ["Hi, welcome to CardinalAIDS+!",
                     "Hi, I hope you're doing well."]
        return print(random.choice(greetings))  
        
    def followUp():
        followUpReplies = ["Do you have more questions? ",
                           "Do you still have questions? ",
                           "Would you like to repeat it? "]
        flag = input(random.choice(followUpReplies)).lower()
        return flag
    
    randomGreeting()
    
    flag = "yes"
    
    while flag == "yes":
        
        ans1 = input(randomAsk() + "\n").lower()
        lst1 = convert(ans1)
        
        for x in range (0,len(lst1)):
            if lst1[x] == "unsettled" or lst1[x] == "charges" or lst1[x] == "fees" or lst1[x] == "balance" or lst1[x] == "balances":
                unsettledFees()
                flag = followUp()
                break
            if lst1[x] == "scholarships" or lst1[x] == "scholarship" or lst1[x] == "scho":
                scholarship(lst1)
                flag = followUp()
                break
            if lst1[x] == "contact" or lst1[x] == "number" or lst1[x] == "email" or lst1[x] == "e-mail":
                contact(lst1)
                flag = followUp()
                break
            if lst1[x] == "enrollment" or lst1[x] == "enrolment" or lst1[x] == "enrol" or lst1[x] == "enroll":
                schedEnroll(lst1)
                flag = followUp()
            if lst1[x] == lst1[x] == "consult" or lst1[x] == "consultation":
                schedConsult(lst1)
                flag = followUp()
                break
            else:
                x = x + 1

AIchat()

