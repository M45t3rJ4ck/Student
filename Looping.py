#For loop and range
for i in (2, 4, 6, 8, 10):
    print("i = ", i)
for i in range(10):
    print("i = ",i)
for i in range(2, 10):
    print("i = ",i)
# For modulus
i = 2
print((i % 2)==0)

#Print odds from 1 - 20
for i in range(1, 21):
    if ((i %2)!=0):
        print("i =",i)

#Floating point numbers
your_float = input("Enter you decimal amount: ")
your_float = float(your_float)
print("Round to 2 decimals : {:.2f}".format(your_float))

#DEMONSTRATE COMPOUNDING INTEREST:
#Have user enter investment amount and interest rate
    #Ask for amount and interest rate
investment = input("Enter the intial investment amount: ")
interest_rate = input("Enter the current interest rate: ")
    #Convert the value to a float
investment = float(investment)
    #Convert the value to a float and round the percentage to 2 decimals
interest_rate = float(interest_rate) * .01
    #Cycle through 10 years with for loop and range 0->9
for i in range(10):
    investment = investment + (investment * interest_rate)
    #Output the result on screen for user
print("Future value after 10 years: {:.2f}".format(investment))

#WHILE LOOPS:
import random
rand_num = random.randrange(1, 51)
i = 1
while (i != rand_num):
    i += 1
print("The random number is: ",rand_num)

#DRAW A PINE TREE
#How tall is the tree in rows
tree_height = input("Enter a number: ")
#Convert into an interger
tree_height = int(tree_height)
#Get the starting spaces for the tree
spaces = tree_height - 1
#Get the starting hashes
hashes = 1
#Save the stump spaces
stump_spaces = tree_height - 1
#Check amount of rows printed
while tree_height != 0:
    #Print spaces
    for i in range(spaces):
        print(' ', end=" ")
    #Print hashes
    for i in range(hashes):
        print('#', end=" ")
    #Newline after each row
    print()
    #Decrement spaces
    spaces -= 1
    #Increment hashes
    hashes += 2
    #Decrement tree height
    tree_height -= 1
#Print spaces and stump
for i in range(stump_spaces):
    print(' ',end=" ")
print("#")