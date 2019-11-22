# Create a program  called “alternative.py” that reads in a sting and makes each alternate character an Uppercase character and each other alternate character a lowercase character.

# Collecting user input
string = input("Please enter your sentence to convert: \n")

def alternating(string):
        result = ""
        index = 0 
        for letter in string:
            if index % 2 == 0:
                result += letter.upper()
                index += 1
            else:
                result += letter.lower()
                index += 1
        print(result)

alternating(string)
