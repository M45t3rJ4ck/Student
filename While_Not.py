import random
num = random.randint(1, 1001)
numGuess = int(input("Please enter a number: "))
while numGuess != num:
    numGuess = int(input("Please enter another number: "))
print("You guessed correctly!")
