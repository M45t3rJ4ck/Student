# Create a new Python file in this folder called 'listTypes.py'.
# Imagine you want to store the names of three of your friends in a list of Strings.
# Create a list variable called friends_names, and write the syntax to store the full names of three of your friends.
# Now write statements to print out the name of the first friend, then the name of the last friend, and finally the length of the list.
# Now define a list called friends_ages, that stores the age of each of your friends in a corresponding manner.
# i.e. the first entry of this list is the age of the friend named first in your other list.

full_names = []
age = []
name_count = 0
age_count = 0
friends_names = list(full_names)
friends_ages = list(age)
full_names = str(input("Please enter your name and surname: "))
age = int(input("Please enter there age: "))
friends_names.append(full_names)
friends_ages.append(age)
name_count += 1
age_count += 1
while name_count != 3:
    full_names = str(input("Please enter your name and surname: "))
    age = int(input("Please enter there age: "))
    friends_names.append(full_names)
    friends_ages.append(age)
    name_count += 1
    age_count += 1
print(friends_names)
print(friends_ages)
if name_count == 3:
    print(len(friends_names))
    print(len(friends_ages))
