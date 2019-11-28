# Edit the above program to allow the user to enter an integer before they enter the name.
# This  integer defines how many ‘tries’ the user will get to enter the right name.
# If the user exceeds the number of tries, the program must stop. 

name = "John"

names = []
tries = 0

In_try = int(input("Please enter a number: "))
In_name = str(input("Please enter a name: "))

names.append(In_name)

tries += 1

while In_name != name:
    In_name = str(input("Please enter a name: "))
    names.append(In_name)
    tries += 1
    if In_name == name:
        print("Incorrect Names: ", names)
    elif In_try == tries:
        exit()
