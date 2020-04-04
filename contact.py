import pandas as pd

def convert(lst):
    return ''.join(lst).split()

def length(lst):
    return len(lst)

def getNumber(username):
    for x in range(0,6):
        if username == data.username[x]:
            number = x
        else:
            x = x + 1
    return number

def contact(lst):
    for x in range (0,length(lst1)):
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
        if lst1[x] == "eece" or lst1[x] == "electrical" or lst1[x] == "electronics" or lst1[x] == "computer":
            code = "eece"
        if lst1[x] == "gs" or lst1[x] == "graduate":
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
    flag = input("Do you have any more questions?").lower()
    return flag

data = pd.read_csv('C:/Users/Marvin/Desktop/Project/unsettled.csv')
contacts = pd.read_csv('C:/Users/Marvin/Desktop/Project/contactlist.csv', encoding='latin1')

username = input("Username: ")
number = getNumber(username)

flag = "yes"

while flag == "yes":
    ans1 = input("Hi! Welcome to CardinalAids+! What brought you here? \n").lower()
    lst1 = convert(ans1) 
    
    for x in range (0,length(lst1)):
        if lst1[x] == "contact" or lst1[x] == "number" or lst1[x] == "email" or lst1[x] == "e-mail":
            contact(lst1)
            flag = followUp()
            break
        else:
            x = x + 1
    
    
           
