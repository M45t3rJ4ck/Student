# Create a new Python file in this folder called “Optional_task.py”
# Create a program that determines whether a String is a palindrome.
# A palindrome is a string which reads the same backwards as forward.
# Some examples of palindromes are: racecar, dad, level and noon
# Ask the user to enter a word and check if that word is a palindrome.
# If it is a palindrome, print out 'Your word is a palindrome'.
# If it is not a palindrome, print out 'Your word is not a palindrome'.

U_palin = list(input("Please enter your word for evaluation: \n"))
palin_U = U_palin[::-1]
if U_palin == palin_U:
    print("You're word is a palindrome!")
else:
    print("You're word isn't a palindrome!")
