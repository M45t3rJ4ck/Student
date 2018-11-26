print ("Hello World")
import sys
print (sys.version_info)

#Ask the user to input their name and asign it ot a variable named name
name = input('What is your name? ')
#Print out Hello followed by the name they entered
print ('Hello' , name)

#Ask the user to input 2 numbers and store them in variables named num1 and num2
num1, num2 = input('Enter 2 numbers: ').split()
#Convert the strings into regular number integers
num1 = int(num1)
num2 = int(num2)
#Add the values entered and store them in variable named sum
sum = num1 + num2
#Subtract the values entered and store them in variable named difference
difference = num1- num2
#Multiply the values entered and store them in variable named product
product = num1 * num2
#Divide the values entered and store them in variable named quotient
quotient = num1 / num2
#Use modulus on the values entered to find the remainder and store them in variable named remainder
remainder = num1 % num2
#Print results on screen for user
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

#Problem: Convert Miles into Kilometers
miles = input('Enter your Miles completed: ')
#Convert the string into regular number integers
miles = int(miles)
#Convert Miles to Kilometers
kilometers = miles * 1.60934
#Print result on screen for user
print("Kilometers are {}".format(kilometers))

#Store the user input of 2 numbers and an operator
num1, operator, num2 = input('Enter your calculations: ').split()
#Convert strings into integers
num1 = int(num1)
num2 = int(num2)
#Provide output based on operator
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print ("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print ("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print ("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
    print ("{} % {} = {}".format(num1, num2, num1 % num2))
else:
    print("Use either + - * / % next time please!")

#To provide different outputs based on age
#1 - 18 = Important
#21, 50, 65 = Important
#All other = Not Important
#Receive user age and store it as a variable named age
age = eval(input("Enter your age: "))
#and: if both are true = return true
#or: if either conditions are true = return true
#not: convert a true condition to false
#If age is both greater than or equal to 1 and less or equal to 18 = print message
if (age >= 1) and (age <= 18):
    print("Your Brithday is Important!!")
#If age is either 21 or 50 = print important message
elif (age == 21) or (age == 50):
    print("You have an Important Birthday!!")
#To check if an age is less than 65 and then convert to false or vise versa
elif not (age < 65):
    print("Important Birthday Coming up for You!!")
#For every other birthday = print message
else:
    print("Not an Important Birthday After all!!")

#Age and Grade Test
age = eval(input("Enter Your age: "))
#If age is <= 5 -> go to kindergarden
if (age >= 1) and (age <= 5):
    print("Go To Kindergarden!!")
#If age is 6 - 18 -> go to grade 1 - 12
elif (age >= 6) and (age <= 18):
    grade = age - 5
    print("Get Your Ass To Grade {}!!".format(grade))
#If age is 19 - 25 -> go to college
elif (age >= 19) and (age <= 25):
    print("Why aren't you in College?!")
#if age is 25+ -> go to work
else:
    print("You Lazy Dog...Get To Work!!")


