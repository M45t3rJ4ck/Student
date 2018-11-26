#User can enter any random number or letter, letter will kick out an error
number = int(input("Please enter a number: "))
print(number)

#User can only enter a number
while True:
    try:
        number = int(input("please enter a number:"))
        break
    except ValueError:
        print("You didn't enter a number!")
    except:
        print("An unkown error occured!")
print("Thank you for entering a number!")

#IMPLIMENT DO WHILE LOOP:
#do
#   ...CODING...
#while(condition)
#Make user guess a number between 1 -> 10:
secret_number = 6
while True:
    try:
        guess_number = int(input("Please guess a number between 1 and 10: "))
    except ValueError:
        print("You didn't guess a number!")
    except:
        print("An unkown error occured!")
    if guess_number != secret_number:
        print("Your choice was incorrect, please guess again!")
    if guess_number == secret_number:
        print("You guessed the correct number!!")
        break
print("Thank you for playing!")

#MATH MODULE
#To access math function in python
import math
#Reference to different functions in module
print("ceil(9.6)= ",math.ceil(9.6))
print("floor(9.6)= ",math.floor(9.6))
print("fabs(-9.6)= ",math.fabs(9.6))
#Factorial = 1*2*3*4(up to number set)
print("factorial(9)= ",math.factorial(9))
#Return remainder of division
print("fmod(9,6)= ",math.fmod(9, 6))
#Receive a float and return an integer
print("trunc(9.6)= ",math.trunc(9.6))
#Returns x^y
print("pow(9.6)= ",math.pow(9, 6))
#Return square root
print("sqrt(9)= ",math.sqrt(9))
#Special Values
print("math e= ",math.e)
print("math pi= ",math.pi)
#Return e^x
print("exp(9)= ",math.factorial(9))
#Return logarithm
print("log(9)= ",math.log(9))
#Defining the base
print("log(900, 60)= ",math.log(900, 60))
print("log10(900)= ",math.log10(900))
#Converts degrees to radians and vise versa
print("degrees(9.63)= ",math.degrees(9.63))
print("radians(90)= ",math.radians(90))
#Other trig functions
#sin, cos, tan, asin, acos, atan, atan2, asinh, a cosh, atanh, sinh, cosh, tanh

#ACCURATE FLOATING POINT CALCULATIONS
#Decimal module that provides accurate calculations
from decimal import Decimal as D

sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")
print("sum = ",sum)
#Stirng -> store text as data type
print(type(9))
print(type(9.63))
#Single or double quotes used for strings
print(type("9"))
print(type('9'))

samp_string = "This is a very important string"
#Get character by referencing the index
print(samp_string[0])
#Last character
print(samp_string[-1])
#Addition to set character
print(samp_string[9 + 6])
#Get a slice of index
print(samp_string[0:6])
#Starting at set index
print(samp_string[9:])
#Join strings
print("Green" + "Egg")
#Repeat strings
print("Hello" * 6)
#Cycle through each character
for char in samp_string:
    print(char)
#Cycle through characters in pairs
#Subtract 1 from index length as string index starts at 0
#Use range and increment by 2
for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i + 1])
#Unicode assigned to characters
#A-Z = 65 -> 90 and a-z = 91 -> 122
#Get the Unicode with ord
print("A = ", ord("A"))
#Convert the Unicode with chr
print("66 = ", chr(66))

#PROBLEM - THE SECRET STRING:
#Receive uppercase string and hide meaning in Unicode
norm_string = input("In uppercase, enter a sentence: ")
secret_string = ""
for char in norm_string:
    secret_string += str(ord(char))
print("Secret Message is: ", secret_string)
#Then translate back into original meaning
norm_string = ""
for i in range(0, len(secret_string) - 1, 2):
    char_code = secret_string[i] + secret_string[i + 1]
    norm_string += chr(int(char_code))
print("Original Message was: ",norm_string)

#SUPER PROBLEM:
#Make it work with upper- and lower-case
#norm_string = input("In uppercase, enter a sentence: ")
norm_string = input("Enter a sentence: ")
secret_string = ""
for char in norm_string:
    secret_string += str(ord(char) - 23)
print("Secret Message is: ", secret_string)
#Then translate back into original meaning
norm_string = ""
for i in range(0, len(secret_string), 2):
    char_code = secret_string[i] + secret_string[i + 1]
    norm_string += chr(int(char_code) + 23)
print("Original Message was: ",norm_string)