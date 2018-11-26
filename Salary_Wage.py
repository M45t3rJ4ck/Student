import math

# User sales or management
User_ID = ""
Hours = 0
gross_sal = 0
Manager = False
Saleson = False

# Collecting user input
User_ID = input("Are you employed as Management?(Y or N) \n")
User_ID = User_ID.upper()
if User_ID == "Y":
    Hours = int(input("How many hours have you worked this month? \n"))
    Manager = True
else:
    gross_sal = int(input("What was your gross sales this month? \n"))
    Saleson = True

# Wage per employee
if Manager == True:
    print("Manager Salary = R", Hours * 40)
else:
    Saleson == True
    print("Saleson Wage = R", ((gross_sal * 8) / 100) + 2000)
