import sqlite3
import random

conn = sqlite3.connect('CardinalAIDS.db')
c = conn.cursor()

class AI():
    
    def convert(lst):
        return ''.join(lst).split()
    
    def profSched(lst1):
        
        def fallback():
            fallbackOptions = ["Can you please be more specific on the class of the professor you're asking?",
                     "I can't seem to find the name of the professor you're asking.",
                     "Please make sure the name of the professor is correct."]
            return print(random.choice(fallbackOptions))
        
        for x in range (0,len(lst1)+1):
            if x == len(lst1):
                fallback()
                return
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

            
            elif lst1[x] == "padilla" or lst1[x] == "dionis":
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

            
            if lst1[x] == "manlises" or lst1[x] == "cyrel":
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
                            
        c.execute("SELECT * FROM profSched WHERE code == ?",(code,))
        data = c.fetchall()
        
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
        
        return print("\nClass Information: \nProfessor: " + profLast + ", " + profFirst + "\nCourse and Section: " + course + "-" + section + "\nDay: " + day + "\nTime: " + startTime + "-" + endTime + "\nRoom: " + room)

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

            if lst1[x] == "professor" or lst1[x] == "prof" or lst1[x] == "mam" or lst1[x] == "ma'am" or lst1[x] == "ms." or lst1[x] == "ms" or lst1[x] == "miss" or lst1[x] == "sir" or lst1[x] == "mr." or lst1[x] == "mr" or lst1[x] == "mister" or lst1[x] == "engr" or lst1[x] == "engineer" or lst1[x] == "class":
                profSched(lst1)
                flag = followUp()
                break
            else:
                x = x + 1

AI()
