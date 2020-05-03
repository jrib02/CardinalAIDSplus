import sqlite3
import random

class AIchat():
    def __init__(self,user):
        conn = sqlite3.connect('CardinalAIDS.db')
        self.c = conn.cursor()
        self.flag = "yes"  
        self.c.execute("SELECT * FROM students WHERE username == ?",(user,))    
        data = self.c.fetchall()
        for entry in data:
            self.username = entry[0]
            self.password = entry[1]
            self.firstName = entry[2]
            self.middle = entry[3]
            self.lastName = entry[4]
            self.unsettled = entry[5]

    def convert(self, lst):
        bad_chars = [';', ':', '!', "*",'?','.',',']
        test_string = lst
        test_string = filter(lambda i: i not in bad_chars, test_string)  
        return ''.join(test_string).split()
    
    def unsettledFees(self, ln, fn, mi, uc):
        ans = "Unsettled charges for " + ln + ", "+ fn +" "+ mi + ". amounts to: " + str(uc)
        return ans
    

    def scholarship(self, lst1):
        def fallback():
            fallbackOptions = ["Can you be more specific for me?",
                     "I don't quite get what you're asking about scholarships.",
                     "Can you be more specific on scholarships?"]
            rngFallback = random.choice(fallbackOptions)
            return rngFallback

        for x in range (0,len(lst1)+1):
            if x == len(lst1):
                return fallback()
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
                self.c.execute("SELECT name FROM scholarships")
                data = self.c.fetchall()
                mes = "List of all scholarships: \n"
                for entry in data:
                    print(entry[0])
                return mes
            else:
                x = x + 1
        
        self.c.execute("SELECT * FROM scholarships WHERE code == ?",(code,))
        data = self.c.fetchall()
        
        for entry in data:
            code = entry[0]
            name = entry[1]
            deadline = entry[2]
            status = entry[3]
            requirements = entry[4]
        
        if deadline == "no data":
            response = "The " + name + " is " + status
        else:
            response = "The " + name + " is deadlined until " + deadline
        return response
    
    def schedEnroll(self, lst1):
        def fallback():
            fallbackOptions = ["You have either entered an invalid batch number or didn't specify one. Could you specify a valid batch number? ", 
                               "I don't think you've entered a valid batch number. Can you re-enter that?", 
                               "Please enter a valid batch number."]
            rngFallback = random.choice(fallbackOptions)
            return rngFallback
        
        for x in range(0,len(lst1)+1):
            if x == len(lst1):
                return fallback()
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
                
        self.c.execute("SELECT * FROM enrollmentsched WHERE number == ?",(number,))
        data = self.c.fetchall()
        
        for entry in data:
            number = entry[0]
            batch = entry[1]
            date = entry[2]
            time = entry[3]
        response = "The schedule of enrollment for Batch " + str(batch) + " is on " + date + " from " + time + " for all programs."
        
        return response
    
    
    def schedConsult(self, lst1):
        def fallback():
            fallbackOptions = ["You have either entered an invalid batch number or didn't specify one. Could you specify a valid batch number? ", 
                               "I don't think you've entered a valid batch number. Can you re-enter that?", 
                               "Please enter a valid batch number."]
            rngFallback = random.choice(fallbackOptions)
            return rngFallback

        for x in range(0,len(lst1)+1):
            if x == len(lst1):
                return fallback()
            
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
            
        self.c.execute("SELECT * FROM consultationsched WHERE number == ?",(number,))
        data = self.c.fetchall()    
            
        for entry in data:
            number = entry[0]
            batch = entry[1]
            date = entry[2]
            time = entry[3]
        response = "The schedule of consultations for Batch " + str(batch) + " is on " + date + " from " + time + " for all programs."
        return response
    
    
    def contact(self, lst1):
        def fallback():
            fallbackOptions = ["Can you be more specific for me?",
                     "I don't quite understand on  what you ask about the email/contact number of your desired department.",
                     "Can you be more specific on your inquiry?"]
            rngFallback = random.choice(fallbackOptions)
            return rngFallback
        
        for x in range (0,len(lst1)+1):
            if x == len(lst1):
                return fallback()
            if lst1[x] == "registrar":
                code = "registrar"
                break
            if lst1[x] == "treasurer" or lst1[x] == "treasury" or lst1[x] == "treasurers":
                code = "treasury"
                break
            if lst1[x] == "admissions" or lst1[x] == "admission":
                code = "admissions"
                break
            if lst1[x] == "bookstore" or lst1[x] == "store":
                code = "bookstore"
                break
            if lst1[x] == "cdmo" or lst1[x] == "maintenance":
                code = "cdmo"
                break
            if lst1[x] == "pe":
                code = "pe"
                break
            if lst1[x] == "math" or lst1[x] == "mathematics":
                code = "math"
                break
            if lst1[x] == "physics":
                code = "physics"
                break
            if lst1[x] == "doit" or lst1[x] == "development" or lst1[x] == "it":
                code = "doit"
                break
            if lst1[x] == "etybsm" or lst1[x] == "business" or lst1[x] == "yuchengco":
                code = "etybsm"
                break
            if lst1[x] == "aridbe" or lst1[x] == "architecture":
                code = "aridbe"
                break
            if lst1[x] == "cege" or lst1[x] == "civil" or lst1[x] == "geological" or lst1[x] == "environmental":
                code = "cege"
                break
            if lst1[x] == "cbmes" or lst1[x] == "chem" or lst1[x] == "chemical" or lst1[x] == "biological" or lst1[x] == "materials":
                code = "cbmes"
                break
            if lst1[x] == "eece" or lst1[x] == "electrical" or lst1[x] == "electronics" or lst1[x] == "computer" or lst1[x] == "cpe" or lst1[x] == "ee" or lst1[x] == "ece":
                code = "eece"
                break
            if lst1[x] == "gs" or lst1[x] == "graduate":
                code = "gs"
                break
            if lst1[x] == "ie-emg" or lst1[x] == "ieemg" or lst1[x] == "management" or lst1[x] == "industrial" or lst1[x] == "ie" or lst1[x] == "mfge":
                code = "ie-emg"
                break
            if lst1[x] == "soit":
                code = "soit"
                break
            if lst1[x] == "mme" or lst1[x] == "mechanical" or lst1[x] == "manufacturing":
                code = "mme"
                break
            if lst1[x] == "sms" or lst1[x] == "media":
                code = "sms"
                break
            if lst1[x] == "ssse" or lst1[x] == "social" or lst1[x] == "education":
                code = "ssse"  
                break
            if lst1[x] == "dal" or lst1[x] == "arts" or lst1[x] == "letters":
                code = "dal" 
                break
            else:
                x = x + 1

    
        self.c.execute("SELECT * FROM contactlist WHERE code == ?",(code,))
        data = self.c.fetchall()
        
        for entry in data:
            code = entry[0]
            department = entry[1]
            contact = entry[2]
            email = entry[3]
            
        mes = "Contact number of " + department + " is " + str(contact) + "\nAvailable email of " + department + " is " + email
        return mes
    
    def profSched(self, lst1):
        
        def fallback():
            fallbackOptions = ["Can you please be more specific on the class of the professor you're asking?",
                     "I can't seem to find the name of the professor you're asking.",
                     "Please make sure the name of the professor is correct."]
            rngFallback = random.choice(fallbackOptions)
            return rngFallback
        
        for x in range (0,len(lst1)+1):
            if x == len(lst1):
                return fallback()
            if lst1[x] == "rafael" or lst1[x] == "maramba":
                for x in range (0,len(lst1)+1):
                    if x == len(lst1):
                        fallback()
                        return
                    elif lst1[x] == "logic" or lst1[x] == "circuits" or lst1[x] == "cpe107" or lst1[x] == "107" or lst1[x] == "logics":
                        for x in range (0,len(lst1)+1):
                            if x == len(lst1):
                                fallback()
                                return
                            elif lst1[x] == "b1":
                                code = "maramba_107_b1"
                                break
                            elif lst1[x] == "b2":
                                code = "maramba_107_b2"
                                break
                            else:
                                x = x + 1
                        break
                    elif lst1[x] == "comorg" or lst1[x] == "organization" or lst1[x] == "architecture" or lst1[x] == "110" or lst1[x] == "cpe110":
                        for x in range (0,len(lst1)+1):
                            if x == len(lst1):
                                fallback()
                                return
                            elif lst1[x] == "b1":
                                code = "maramba_107_b1"
                                break
                            elif lst1[x] == "b1":
                                code = "maramba_107_b2"
                                break
                            else:
                                x = x + 1
                        break
                    else:
                        x = x + 1
                break
            else:
                x = x + 1
            
            if lst1[x] == "padilla" or lst1[x] == "dionis" or lst1[x] == "pads":
                for x in range (0,len(lst1)+1):
                    if x == len(lst1):
                        fallback()
                        return
                    if lst1[x] == "software" or lst1[x] == "design" or lst1[x] == "softdes" or lst1[x] == "106" or lst1[x] == "cpe106":
                        for x in range (0,len(lst1)+1):
                            if x == len(lst1):
                                fallback()
                                return
                            if lst1[x] == "b1":
                                code = "padilla_106_b1"
                                break
                            if lst1[x] == "b1":
                                code = "padilla_106_b2"
                                break
                            else:
                                x = x + 1
                        break
                    else:
                        x = x + 1
                break
            else:
                x = x + 1
            
            if lst1[x] == "manlises" or lst1[x] == "cyrel" or lst1[x] == "cy":
                for x in range (0,len(lst1)+1):
                    if x == len(lst1):
                        fallback()
                        return
                    if lst1[x] == "microproccesor" or lst1[x] == "microprocessors" or lst1[x] == "micro" or lst1[x] == "108" or lst1[x] == "cpe108":
                        for x in range (0,len(lst1)+1):
                            if x == len(lst1):
                                fallback()
                                return
                            if lst1[x] == "b1":
                                code = "manlises_108_b1"
                                break
                            if lst1[x] == "b1":
                                code = "manlises_108_b2"
                                break
                            else:
                                x = x + 1
                        break
                    else:
                        x = x + 1
                break
            else:
                x = x + 1
                            
        self.c.execute("SELECT * FROM profSched WHERE code == ?",(code,))
        data = self.c.fetchall()
        
        for entry in data:
            code = entry[0]
            profLast = entry[1]
            profFirst = entry[2]
            course = entry[3]
            section = entry[4]
            startTime = entry[5]
            endTime = entry[6]
            room = entry[7]
            day = entry[8]
        
        mes = "\nClass Information: \nProfessor: " + profLast + ", " + profFirst + "\nCourse and Section: " + course + "-" + section + "\nDay: " + day + "\nTime: " + startTime + "-" + endTime + "\nRoom: " + room
        return mes

    def news(self, lst1):
        def fallback():
            fallbackOptions = ["Can you be more specific for me?",
                     "I don't quite understand on  what you ask about that news.",
                     "Can you be more specific on your inquiry?"]
            rngFallback = random.choice(fallbackOptions)
            return rngFallback
        
        for x in range (0,len(lst1)+1):
            if x == len(lst1):
                return fallback()
            if lst1[x] == "medical" or lst1[x] == "assistance" or lst1[x] == "checkup" or lst1[x] == "check-up" or lst1[x] == "diagnosis":
                code = "medical"
                break
            if lst1[x] == "cybersecurity" or lst1[x] == "cybersec" or lst1[x] == "sophos":
                code = "cybersec"
                break
            if lst1[x] == "dole" or lst1[x] == "solidarity":
                code = "dole"
                break
            if lst1[x] == "alvin" or lst1[x] == "caparanga" or lst1[x] == "chemical" or lst1[x] == "engineer" or lst1[x] == "piche" or lst1[x] == "national" or lst1[x] == "convention":
                code = "caparanga"
                break
            if lst1[x] == "filmmaker" or lst1[x] == "donation" or lst1[x] == "donations" or lst1[x] == "frontliners":
                code = "filmmaker"
                break
            if lst1[x] == "rising" or lst1[x] == "challenge" or lst1[x] == "vea" or lst1[x] == "reynaldo" or lst1[x] == "covid-19" or lst1[x] == "covid":
                code = "rising"
            if lst1[x] == "ranking" or lst1[x] == "THE" or lst1[x] == "times" or lst1[x] == "higher" or lst1[x] == "impact" or lst1[x] == "rankings":
                code = "ranking"
                break
            
        self.c.execute("SELECT * FROM news WHERE code == ?",(code,))
        data = self.c.fetchall()
        
        for entry in data:
            code = entry[0]
            headline = entry[1]
            link = entry[2]
        
        mes = headline + "\nRead more at: " + link
        return mes

    def randomAsk(self):
        askResponses = ["What can I do for you?",
                        "What kind of assistance can I give?",
                        "What brought you to me?"]
        rngResponse = random.choice(askResponses)
        return rngResponse

    
    def getQues(self, question):
        while self.flag == "yes":
            
            lst1 = self.convert(question.lower())      
            
            for x in range (0,len(lst1)+1):
                if x == len(lst1):
                    return self.randomAsk()
            
                elif lst1[x] == "unsettled" or lst1[x] == "charges" or lst1[x] == "fees" or lst1[x] == "balance" or lst1[x] == "balances":
                    ans = self.unsettledFees(self.lastName, self.firstName, self.middle, self.unsettled)

                    return ans
                elif lst1[x] == "scholarships" or lst1[x] == "scholarship" or lst1[x] == "scho":
                    ans = self.scholarship(lst1)

                    return ans
                elif lst1[x] == "contact" or lst1[x] == "number" or lst1[x] == "email" or lst1[x] == "e-mail":
                    ans = self.contact(lst1)

                    return ans
                elif lst1[x] == "enrollment" or lst1[x] == "enrolment" or lst1[x] == "enrol" or lst1[x] == "enroll":
                    ans = self.schedEnroll(lst1)

                    return ans
                elif lst1[x] == lst1[x] == "consult" or lst1[x] == "consultation":
                    ans = self.schedConsult(lst1)
        
                    return ans
                elif lst1[x] == "professor" or lst1[x] == "prof" or lst1[x] == "mam" or lst1[x] == "ma'am" or lst1[x] == "ms." or lst1[x] == "ms" or lst1[x] == "miss" or lst1[x] == "sir" or lst1[x] == "mr." or lst1[x] == "mr" or lst1[x] == "mister" or lst1[x] == "engr" or lst1[x] == "engineer" or lst1[x] == "class":
                    ans = self.profSched(lst1)

                    return ans
                elif lst1[x] == "news" or lst1[x] == "updates" or lst1[x] == "info" or lst1[x] == "information":
                    ans = self.news(lst1)

                    return ans
                else:
                    x = x + 1
                    