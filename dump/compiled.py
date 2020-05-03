import pandas as pd

data = pd.read_csv('C:/Users/CJ7/Desktop/unsettled.csv')
scholarships = pd.read_csv('C:/Users/CJ7/Desktop/scho.csv')
contacts = pd.read_csv('C:/Users/CJ7/Desktop/contactlist.csv', encoding='latin1')
schedules = pd.read_csv('C:/Users/CJ7/Desktop/enrollmentschedule.csv')

def convert(lst):
    return ''.join(lst).split()

def length(lst):
    return len(lst)

def getNumber(username):
    for x in range(0,7):
        if username == data.username[x]:
            number = x
        else:
            x = x + 1
    return number

def unsettled():
    return print("Unsettled charges for " + data.lastname[number] + ", "+data.firstname[number]+" "+data.middle[number]+ ". amounts to: " + str(data.unsettled[number]))

def scholarship(lst):
    
    for x in range (0,length(lst1)):
        if lst1[x] == "keb" or lst1[x] == "hana" or lst1[x] == "kebhana":
            code = "keb"
        elif lst1[x] == "refinitiv":
            code = "refinitiv"
        elif lst1[x] == "maasd" or lst1[x] == "san" or lst1[x] == "diego" or lst1[x] == "sandiego" or lst1[x] == "alumni":
            code = "maasd"
        elif lst1[x] == "ety" or lst1[x] == "et" or lst1[x] == "yuchengco":
            code = "ety"
        elif lst1[x] == "list" or lst1[x] == "available":
            print("List of available scholarships: \n")
            for x in range (0,4):
                print(scholarships.name[x])
            return
        else:
            x = x + 1
    
    for x in range(0,4):
        if code == scholarships.code[x]:
            name = scholarships.name[x]
            deadline = scholarships.deadline[x]
            reqs = scholarships.requirements[x]
            status = scholarships.status[x]
        else:
            x = x + 1
    
    if deadline == "no data":
        response = print("The " + name + " is " + status)
    else:
        response = print("The " + name + " is deadlined until " + deadline)
    
    return response

def schedEnroll(lst):
    for x in range(0,length(lst1)):
        num = 1
        if lst1[x] == "2015" or lst1[x] == "2016" or lst1[x] == "2017" or lst1[x] == "17" or lst1[x] == "16" or lst1[x] == "15":
            num = 2
        if lst1[x] == "2018" or lst1[x] == "18":
            num = 3
        if lst1[x] == "2019" or lst1[x] == "19":
            num = 4
        else:
            x = x + 1
    for x in range(0,4):
       if num == schedules.number[x]:
          batch = schedules.batch[x]
          date = schedules.date[x]
          time = schedules.time[x]
       else:
           x = x + 1
    return print("The schedule of enrollment for Batch " + str(batch) + " is on " + date + " from " + time + ".")

def contact(lst):
    for x in range (0,length(lst1)):
        if lst1[x] == "registrar":
            code = "registrar"
        if lst1[x] == "treasurer" or lst1[x] == "treasury" or lst1[x] == "treasurers" or lst1[x] == "accounting":
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
        if lst1[x] == "doit" or lst1[x] == "Development" or lst1[x] == "it":
            code = "doit"
        if lst1[x] == "etybsm" or lst1[x] == "business" or lst1[x] == "yuchengco":
            code = "etybsm"
        if lst1[x] == "aridbe" or lst1[x] == "architecture":
            code = "aridbe"
        if lst1[x] == "cege" or lst1[x] == "civil" or lst1[x] == "geological" or lst1[x] == "environmental":
            code = "cege"
        if lst1[x] == "cbmes" or lst1[x] == "chem" or lst1[x] == "chemical" or lst1[x] == "biological" or lst1[x] == "materials":
            code = "cbmes"
        if lst1[x] == "eece" or lst1[x] == "electrical" or lst1[x] == "electronics" or lst1[x] == "computer":
            code = "eece"
        if lst1[x] == "gs" or lst1[x] == "Graduate":
            code = "gs"
        if lst1[x] == "ie-emg" or lst1[x] == "ieemg" or lst1[x] == "management" or lst1[x] == "industrial":
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
    
    for x in range(0,21):
        if code == contacts.code[x]:
            department = contacts.department[x]
            contactNumber = contacts.contact[x]
            emailDept = contacts.email[x]
        else:
            x = x + 1
    print("Contact number of " + department + " is " + str(contactNumber))
    print ("Available email of " + department + " is " + emailDept)

def followUp():
    flag = input("Do you have any more questions? ").lower()
    return flag

username = input("Username: ")
number = getNumber(username)

flag = "yes"

while flag == "yes":
    ans1 = input("Shoot your question! \n").lower()
    lst1 = convert(ans1)
    
    for x in range (0,length(lst1)):
        if lst1[x] == "unsettled" or lst1[x] == "charges" or lst1[x] == "balance" or lst1[x] == "payables" or lst1[x] == "balances":
            unsettled()
            flag = followUp()
            break
        if lst1[x] == "scho" or lst1[x] == "scholarships" or lst1[x] == "scholarship":
            scholarship(lst1)
            flag = followUp()
            break
        if lst1[x] == "contact" or lst1[x] == "number" or lst1[x] == "email" or lst1[x] == "e-mail":
            contact(lst1)
            flag = followUp()
            break
        if lst1[x] == "schedule" or lst1[x] == "enrollment" or lst1[x] == "enrolment" or lst1[x] == "enrol" or lst1[x] == "enroll":
            schedEnroll(lst1)
            flag = followUp()
            break
        else:
            x = x + 1
    
    
           
