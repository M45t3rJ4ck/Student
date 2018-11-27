# Now write Python code to take the name of a users favourite restaurant and store it in a variable called favRest
# Now, below this, write a statement to take in the users favourite number. Use casting to store it in a variable called intFav
# Now print out both of these using two separate print statements below what you have written. Be careful!
# Now, once this is working, try cast favRest to an int. What happens? Add a comment in your code to explain why this is.

# Ask user for restaurant
favRest = input("Please enter your favourite restaurant: ")

# Ask user for numbers
intFav = int(input("Please enter your favourite number: "))

# Print out inputs
print("Your favourite kitchen is: {}!".format(favRest))
print("Your lucky number is: {}".format(intFav))

# Cast to int
if favRest == int(favRest):
    print("It works!")
elif favRest != int(favRest):
    print("It didn't work...")
else:
    print("You were right!")
