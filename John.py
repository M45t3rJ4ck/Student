# Once you have read and completely understood ​example.py, ​write a Python program that takes in a user input as a String.
# While the String is not “John”, add every String entered to a  list until “John” is entered.
# Then print out the list.
# This program basically stores all incorrectly entered Strings in a list where “John” is the only correct String.
# Save this program as '​John.py' ​in this folder.
# Example program run:
#       Enter your name : <user enters Tim>  
#       Enter your name : <user enters Mark>  
#       Enter your name: <user enters John>  
#       Incorrect names: [‘Tim’, ‘Mark’]

name = "John"
names = []
In_name = str(input("Please enter a name: "))
names.append(In_name)
while In_name != name:
    In_name = str(input("Please enter a name: "))
    names.append(In_name)
    if In_name == name:
        print("Incorrect Names: ", names)
