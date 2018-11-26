#STRING METHODS:
#Many various methods
rand_string = "   this is an important string   "
#Delete white spaces on left
rand_string = rand_string.lstrip()
#Delete white spaces on right
rand_string = rand_string.rstrip()
#Delete all white spaces
rand_string = rand_string.strip()
#Capitalize the 1st letter
print(rand_string.capitalize())
#Capitalize every letter
print(rand_string.upper())
#Lowercase all letters
print(rand_string.lower())
#Turn a list into a string
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))
#convert a list into a string
a_list_2 = rand_string.split()
for i in a_list_2:
    print(i)
#Count how many times a string occurs
print("How many is are there: ", rand_string.count("is"))
#Get index of matching string
print("Where is string:", rand_string.find("string"))
#Replace a substring
print(rand_string.replace("an", "a kind of"))

#PROBLEM -> ACRONYM GENERATOR
#Convert a string in uppercase acronym
user_string = str(input("Enter a sentence: "))
#Convert string into uppercase
a_string = user_string.upper()
#Convert string into a list
a_list = a_string.split()
#Cycle through the list
for word in a_list:
    #Get the 1st character and eliminate the rest
    print(word[0], end="")
#Add a new line
print()

#USEFUL STRING METHODS
letter_z = "z"
num_3 = "3"
a_space = " "
#Return True for letters or numbers, white space is false
print("is z a letter or number: ", letter_z.isalnum())
#Return True for letters
print("Is z a letter: ", letter_z.isalpha())
#Return True for numbers, floats are false
print("Is 3 a number: ", num_3.isdigit())
#Return True for lowercase
print("Is z in lowercase: ",letter_z.islower())
#Return True for uppercase
print("Is z in uppercase: ", letter_z.isupper())

#MAKE USE OF AN ISFLOAT
#Functions allow use to avoid repeating code
def isfloat(str_val):
    try:
#Will throw ValueError if not a float
        float(str_val)
#If value found return
        return True
    except ValueError:
        return False
pi = 3.14
print("Is pi a float: ",isfloat(pi))

#PROBLEM -> CEASAR'S CIPHER
#User to input a message
message = str(input("Enter your message now: "))
s_amount = int(input("Enter amount characters to shift with: "))
#Convert message into unicode
secret = " "
#Cycle through each character
for char in message:
    #If isn't a letter, keep it as is
    if char.isalpha():
        #Get character and shift amount
        char_code = ord(char)
        char_code += s_amount
        #If uppercase, compare to uppercase unicodes
        if char.isupper():
            #Bigger than Z - 26
            if char_code > ord("Z"):
                char_code -= 26
            #Smaller than A + 26
            elif char_code < ord("A"):
                char_code += 26
        #Do the same for lowercase
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        #Convert letters
        secret += chr(char_code)
    #If not a letter leave as is
    else:
        secret += char
print("Encrypted message: ",secret)
#To reverse the message
s_amount = -s_amount
orig_message = ""
for char in secret:
    #If isn't a letter, keep it as is
    if char.isalpha():
        #Get character and shift amount
        char_code = ord(char)
        char_code += s_amount
        #If uppercase, compare to uppercase unicodes
        if char.isupper():
            #Bigger than Z - 26
            if char_code > ord("Z"):
                char_code -= 26
            #Smaller than A + 26
            elif char_code < ord("A"):
                char_code += 26
        #Do the same for lowercase
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        #Convert letters
        orig_message += chr(char_code)
    #If not a letter leave as is
    else:
        orig_message += char
print("Decrypted message: ",orig_message)
# Redo in a function