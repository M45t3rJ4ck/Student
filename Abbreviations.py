# Create a new Python file in this folder called “Optional_task.py”
# Write a program that is able to give you the meaning of a given abbreviation.
# Create a dictionary that contains some abbreviations and their meanings.
# Let the abbreviation be the key and the meaning of the abbreviation be the value (e.g. ADSL: Asymmetric Digital Subscriber Line).
# Make sure that you dictionary has at least 4 abbreviations and their meanings.
# If you need ideas on some abbreviations, go to http://www.abbreviations.com/
# After you have created your dictionary add 2 more abbreviations and their meanings to it.
# Now ask the user to enter an abbreviation and check if that abbreviation is in your dictionary.
# If it is print out the abbreviation and it's meaning.
# If it is not in the dictionary, print out "Abbreviation not found"

abbreviations = {"asap": "as soon as possible",
                 "acrim": "active cavity radiometer irradiance monitor",
                 "acs": "advanced camera for surveys",
                 "adsl": "asymmetric digital subscriber line",
                 "acts": "advanced communications technology satellite",
                 }

print(abbreviations.keys())
u_abb = input("Enter an abbreviation: ")
if u_abb in abbreviations.keys():
    print(abbreviations.get(u_abb))
elif u_abb not in abbreviations.keys():
    print("Abbreviation not found.")
    add_abb = input("Would you like to add this abbreviation(Y/N)? ")
    add_abb = add_abb.upper()
    if add_abb == "Y":
        new_val = input("Enter the meaning: ")
        abbreviations[u_abb] = new_val
        print(abbreviations.keys())
        u_abb = input("Enter an abbreviation: ")
        if u_abb in abbreviations.keys():
            print(abbreviations.get(u_abb))
