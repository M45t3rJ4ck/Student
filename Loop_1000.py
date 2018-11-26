# Create a new Python file in this folder called 'loop1000.py'.
# Imagine I asked you to print out all the numbers from 1 to 1000.
# Either you'd be up all night writing a list of integers, or you can be smart and use the xrange command.
# Write 2 lines of code in your file to print out all numbers from 1 to 1000.
# Once you've got this to work, add logic inside your loop to only print out the numbers from 1 to 1000 that are even (i.e. divisible by 2).
# Remember the modulo command - i.e., %. 10%5 will give you the remainder of 10 divided by 5. 10 divided by 5 equals 2 with remainder of 0, hence this statement returns 0.
# Any even number is a number that can be divided by 2 with no remainder.

for num in range(1, 1001):
    if num % 2 == 0:
        print(num)
