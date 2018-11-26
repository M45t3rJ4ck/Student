#FUNCTION BASICS:
#To reduce code and improve understanding
def add_name(num1, num2):
    #Return values if needed
    return num1 + num2
#Call function by name followed by comma
print("5 + 4 = ",add_name(5, 4))

#FUNCTION VARIABLES:
#Any variable defined inside a function is only available in that function
#EXAMPLE 1:
#Varialbes created inside function isn't useable outside of it
def assign_name():
    name = "Dog"
assign_name()
#print(name)

#EXAMPLE 2:
#Unable to change global settings when passed into a function
def change_name(name):
    #Trying to change Tom
    name = "Mark"
#Variable defined outside function can't be changed inside
name = "Tom"
#Trying to change values
change_name(name)
#Print name
print(name)

#EXAMPLE 3:
#To change value pass it back
def change_name_2():
    return "Mark"
name = change_name_2()
print(name)

#EXAMPL 4:
#Use of global statement to change it
gdl_name = "Sally"
def change_name_3():
    global gdl_name
    gdl_name = "Sammy"
change_name_3()
print(gdl_name)

#RETURNING CODE:
#If you don't return a value, a fundtion will return NONE
def get_sum(num1, num2):
    sum = num1 + num2
print(get_sum(5, 4))

#PROBLEM - SOLVE X:
#Make a function to solve X (X + 4 = 9)
#X to be first value received and you to deal with addition
#Receive a string and split into variables
def equa_change(gdl_equa):
    x, add, num1, equal, num2 = gdl_equa.split()
#Convert string into integers
    num1, num2 = int(num1), int(num2)
#Convert it into a string and join to "X = "
    return "x = " + str(num2 - num1)
#Print()
print(equa_change("x + 4 = 9"))

#RETURN MULTIPLE VALUES
#By using a return statement
def mult_divide(num1, num2):
    return(num1 * num2), (num1 / num2)
mult, divide = mult_divide(5, 4)
print("5 * 4 =",mult)
print("5 / 4 = ",divide)

#RETURN A LIST OF PRIMES
#A prime can only be divided by itself and 1
#if modulus == 0 -> number isn't prime
def isprime(num):
    #Cycle with for loop (from 2 to value to check)
    for i in range(2, num):
        #if a divsion has no remainder -> not prime
        if (num % i) == 0:
            return False
    return True

def getprime(max_number):
    #Create a list to hold primes
    list_of_primes = []
    #Cycle with for loop (from 2 to max value requested)
    for num1 in range(2, max_number):
        if isprime(num1):
            list_of_primes.append(num1)
    return list_of_primes
max_num_to_check = int(input("Searchfor primes up to: "))
list_of_primes = getprime(max_num_to_check)
for prime in list_of_primes:
    print(prime)

#UNKNOWN NUMBER OF ARGUMENTS
# *->receive unknown number of arguments
def sumAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print("Sum = ",sumAll(1, 2, 3, 4, 5, 6, 7, 8, 9))

#Module needed to continue
import math
#Function to avoid duplicate coding
#OUR FUNCTIONS:
#Routs to the correct area function
def get_area(shape):
    #Switch to lowercase for easy comparison
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle: ")
#Create functions for areas
def rectangle_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print("The area of the rectangle is: ",area)
def circle_area():
    radius = float(input("Enter the radius: "))
    area = math.pi * (math.pow(radius, 2))
    print("the area of the circle is {:.2f}".format(area))
#Placing main programming logic in functions
def main():
    #Ask the user what shape they have
    shape_type = input("Get area for what shape: ")
    #Call a function to route to correct function
    get_area(shape_type)
#All definitions ignored and calls main() to start
main()