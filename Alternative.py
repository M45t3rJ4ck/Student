# Create a program  called “alternative.py” that reads in a sting and makes each alternate character an Uppercase character and each other alternate character a lowercase character.

# Collecting user input
U_string = input("Please enter your sentence to convert: \n")
print(U_string[::2].upper())

input("Press enter to exit")
