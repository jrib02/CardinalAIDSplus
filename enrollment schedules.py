# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:58:07 2020

"""

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
        if lst1[x] == "eece" or lst1[x] == "electrical" or lst1[x] == "electronics" or lst1[x] == "computer":
            code = "eece"
        if lst1[x] == "mme" or lst1[x] == "mechanical" or lst1[x] == "manufacturing":
            code = "mme"
        else:
            x = x + 1
    
    for x in range(0,2): #PAPALITAN MO PA RITO YUNG END NG RANGE KUNG ILAN MAN DEPT
        if code == contacts.code[x]:
            department = contacts.department[x]
            contactNumber = contacts.contact[x]
        else:
            x = x + 1
    return print("Contact number of " + department + " is " + str(contactNumber))

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
          batch =  schedules.batch[x]
          date = schedules.date[x]
          time = schedules.time[x]
       else:
           x = x + 1
    return print("The schedule of enrollment for Batch " + str(batch) + " is on " + date + " from " + time + ".")

def followUp():
    flag = input("Do you have any more questions?").lower()
    return flag

data = pd.read_csv('unsettled.csv')
schedules = pd.read_csv('enrollmentschedule.csv')

username = input("Username: ")
number = getNumber(username)

flag = "yes"

while flag == "yes":
    ans1 = input("Hi! Welcome to CardinalAids+! What brought you here? \n").lower()
    lst1 = convert(ans1)
    
    for x in range (0,length(lst1)):
        if lst1[x] == "schedule" or lst1[x] == "enrollment":
            schedEnroll(lst1)
            flag = followUp()
            break
        else:
            x = x + 1
    
    
           
