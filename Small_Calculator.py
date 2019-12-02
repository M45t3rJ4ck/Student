# Create a new Python file in this folder called “Optional_task.py”
# Write a program that will act as a calculator.
# Create functions named addNum, subtractNum, multiplyNum and divideNum that asks the user to enter 2 numbers and adds, subtracts, multiplies or divides them
# respectively.
# Print out the following menu and ask the user to input a number that corresponds to the option they would like to choose:
#       Option 1 - add
#       Option 2 - subtract
#       Option 3 - multiply
#       Option 4 - divide
# If the user enters 1 call the addNum function
# If the user enters 2 call the subtractNum function
# If the user enters 3 call the multiplyNum function
# If the user enters 4 call the divideNum function
# Make sure that the result of the caluation is printed out to the screen.


def print_menu():
    print("1. Add numbers")
    print("2. Subtract numbers")
    print("3. Multiply numbers")
    print("4. Devide numbers")
    print("5. Quit")


def addNum(num1, num2, num3):
    num3 = num1 + num2
    return str(num3)


def subNum(num1, num2, num3):
    num3 =  num1 - num2
    return str(num3)


def mulNum(num1, num2, num3):
    num3 = num1 * num2
    return str(num3)


def divNum(num1, num2, num3):
    num3 = num1 / num2
    return str(num3)


num1 = float(input("Enter 1st number for calculations: \n"))
num2 = float(input("Enter 2nd number for calculations: \n"))

num3 = float()

print_menu()

menu_choice = 0

while menu_choice != 5:
    menu_choice = int(input("Please enter a number between 1 and 5: \n"))
    if menu_choice == 1:
        print(addNum(num1, num2, num3))
    elif menu_choice == 2:
        print(subNum(num1, num2, num3))
    elif menu_choice == 3:
        print(mulNum(num1, num2, num3))
    elif menu_choice == 4:
        print(divNum(num1, num2, num3))
    else:
        exit()
