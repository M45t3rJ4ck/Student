#   Create a new Python file in this folder called funcpractice.py.
#   Inside it, create a function called 'addthree', that takes as input three parameters - num1, num2, num3.
#   Then, write logic to create a new variable, y, that is the sum of all three of these numbers.
#   Then, return the result y.
#   Now, after you've defined this function, write a function call to return the sum of the numbers 52, 25, and 1403.
#   Store this result in a variable called sumFunc.
#   Print out sumFunc. Don't forget to cast to a String!


def addthree(num1, num2, num3):
    y = num1 + num2 + num3
    return y


print("You will be asked for 3 numbers")
num1 = int(input("Please enter the 1st number: \n"))
num2 = int(input("Please enter the 2nd number: \n"))
num3 = int(input("Please enter the 3rd number: \n"))
print("The sum of your numbers are: " + str(addthree(num1, num2, num3)))
nums = [52, 25, 1403]


def sumFunc(nums):
    sumFunc = sum(nums)
    return sumFunc


print("sumFunc output: " + str(sumFunc(nums)))
