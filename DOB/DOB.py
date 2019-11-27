# Write a program that reads the data from the text file called DOB.txt and prints it out in two different sections in the format displayed below:
# Name                 
#       1. A Masinga           
#       Etc.
# Birth date
#       1. 21 July 1988
#       Etc.

import re

# Open file containing list of people details in read & write mode and sort
file = open("DOB.txt", "r")

# Defining details
content = []
names = {}
name_num = 1
dates = {}
date_num = 1
line = file.read()

# Defining sorting operation
content.append(line.split("\n"))
content = [details for sublist in content for details in sublist]
content.sort()

for details in content:
    regex_name = re.compile("[a-zA-Z]+\s[a-zA-Z]+")
    name = regex_name.findall(details)
    names[name_num] = str(name).strip("['']")
    name_num += 1

    regex_date = re.compile("\d+\s\w+\s\d{4}")
    date = regex_date.findall(details)
    dates[date_num] = str(date).strip("['']")
    date_num += 1

print(names)
print(dates)
