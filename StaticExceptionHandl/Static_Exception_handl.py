# You can import by listing the file name minus the py
import sum

# Get access to functions by proceeding with the file
# name and then the function you want
print("Sum :", sum.getSum(1,2,3,4,5))

# ---------- FROM ---------- 
# You can use from to copy specific functions from a module
# You can use from sum import * to import all functions
# You can import multiple functions by listing them after
# import separated by commas
from sum import getSum

# You don't have to reference the module name now
print("Sum :", getSum(1,2,3,4,5))


# ---------- EXCEPTION HANDLING ----------
# Exceptions are triggered either when an error occurs
# or when you want them to.
# We use exceptions are used to handle errors, execute
# specific code when code generates something out of
# the ordinary, to always execute code when something
# happens (close a file that was opened),
# When an error occurs you stop executing code and jump
# to execute other code that responds to that error 
# Let's handle an IndexError exception that is
# triggered when you try to access an index in a list
# that doesn't exist 
# Surround a potential exception with try
try:
    aList = [1,2,3]
    print(aList[3])

# Catch the exception with except followed by the exception you want to catch. You can catch multiple exceptions by
# separating them with commas inside parentheses except (IndexError, NameError):
except IndexError:
    print("Sorry that index doesn't exist")

# If the exception wasn't caught above this will
# catch all others
except:
    print("An unknown error occurred")

# ---------- CUSTOM EXCEPTIONS ----------
# Lets trigger an exception if the user enters a
# name that contains a number
# Although you won't commonly create your own exceptions
# this is how you do it
# Create a class that inherits from Exception
class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name : ")

    if any(char.isdigit() for char in dogName):

        # Raise your own exception
        # You can raise the built in exceptions as well
        raise DogNameError

except DogNameError:
    print("Your dogs name can't contain a number")

# ---------- FINALLY & ELSE ----------
# finally is used when you always want certain code to
# execute whether an exception is raised or not

num1, num2 = input("Enter to values to divide : ").split()

try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You can't divide by zero")

# else is only executed if no exception was raised
else:
    print("You didn't raise an exception")

finally:
    print("I execute no matter what")

# ---------- PROBLEM EXCEPTIONS & FILES ----------
# 1. Create a file named mydata2.txt and put data in it. Using what you learned in part 8 and Google to find out how to
# open a file without with try to open the file in a try block. Catch the FileNotFoundError exception. In else print
# the file contents. In finally close the file. Try to open the nonexistent file mydata3.txt and test to see if you
# caught the exception

try:
    myFile = open("mydata2.txt", encoding="utf-8")

# We can use as to access data and methods in the
# exception class
except FileNotFoundError as ex:
    print("That file was not found")

    # Print out further data on the exception
    print(ex.args)

else:
    print("File :", myFile.read())
    myFile.close()

finally:
    print("Finished Working with File")
