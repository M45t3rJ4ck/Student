# Create a new Python file in this folder called “Optional_task.py”
# Create a program to check if a number inputted by the user is prime.
# A prime number is a positive integer greater than 1, whose only factors are 1 and the number itself.
# Examples of prime numbers are: 2, 3, 5, 7, etc.
# Ask the user to enter an integer.
# First check if the number is greater than 1.
# If it is greater than 1, check to see if it has any factors besides one and itself.
# i.e if there are any numbers between 2 and the number itself that can divide the number without any remainders 
# If the number is a prime number, print out the number and ' is a prime number!'
# If the number is not a prime number, print out the number and ' is not a prime number'

U_prime = int(input("Please enter a number to check if it is prime: "))
primed = ()
for x in range(2, U_prime):
    if (x % 2) == 0:
        primed = str(U_prime) + " isn't a prime number." + "\n"
    else:
        primed = str(U_prime) + " is a prime number." + "\n"

print(primed)
input("Press enter to exit")
