#Open file containing list of people details and sort
#Importing libraries
import os
#Open file in read & write mode
f = open("DOB.txt", "r+")
#Defining details
Fname = [] #4 characters after n/line chr
Lname = [] #4 characters after 1st w/space
Day = [] #2 integers after 2nd w/space
Month = [] #4 characters after 3rd w/space
Year = [] #4 intigers after 4th w/space
names = (Fname), (Lname)
dates = (Day), (Month), (Year)
content = [names, dates]
#Defining sorting operation
while True:
    line = f.readline()
    content.append(line)
    if not line:
        break
print(content)
