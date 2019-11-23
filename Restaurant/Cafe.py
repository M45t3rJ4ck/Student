# Create a new Python file in this folder called cafe.py.
# Create a list called menu, which should contain at least 4 items in the cafe.
# Next, create a dictionary called stock, which should contain the stock value for each item on your menu.
# Create another dictionary called price, which should contain the prices for each item on your menu.
# Next, create a function which will calculate the total stock worth in the cafe. You will need to remember to loop through the appropriate dictionaries and lists to
# do this.
# Finally, print out the result of your function.

import re

def print_bill(filename):
    table = open(filename, "r")
    bill = table.read().split("\n")
    ordered = (len(bill))
    prices = []
    total = []
    cost = 0
    for line in bill:
        prices.append(re.compile("\d{2}").findall(line))
    total = [item for sublist in prices for item in sublist]
    for i in total:
        cost += int(i)
    print(f"The Total Items Ordered is: {ordered} and the Total Price is: {cost}.")
    print(f"Thank you for visiting {filename}, please come again.")

fb_menu = {
    "coffee" : 18,
    "tea" : 15,
    "sandwich" : 25,
    "waffle" : 22
}

stock = {
    "coffee_beans" : 100,
    "tea_bags" : 100,
    "bread" : 100,
    "ham" : 100,
    "cheese" : 100,
    "waffle_doug" : 100,
    "ice_cream" : 100,
    "suryp" : 100,
}

def print_menu():
    print("1. Start a new table?")
    print("2. Call customer table?")
    print("3. Place an order?")
    print("4. Print Bill")
    print("5. Print Stock Levels")
    print("6. Quit")
    

filename = ""
menu_choice = 0

def main_menu(filename, fb_menu, stock):
    while True:
        if filename == "":
            print_menu()
            menu_choice = int(input("Welcome, please enter a number: \n"))
        else:
            print_menu()
            menu_choice = int(input(f"Welcome {filename}, please enter a number: \n"))

        if menu_choice == 1:
            filename = input("Customer name to save: ")
            new_table = open(filename, "w")
            new_table.close()
        elif menu_choice == 2:
            filename = input("Customer name to load: ")

        elif menu_choice == 3:
            choice = int(input("Your options are: " + "\n1. Americano " + "\n2. Rooibos, " + "\n3. Sandwich, " + "\n4. Waffle" + "\n5. Enough ordered" + "\n"))
            
            if choice == 1:
                choice = "coffee"
                stock["coffee_beans"] -= 1
                table = open(filename, "a")
                table.write(f"Americano\t{fb_menu[choice]}\n")
                table.close()
            elif choice == 2:
                choice = "tea"
                stock["tea_bags"] -= 1
                table = open(filename, "a")
                table.write(f"Rooibos\t{fb_menu[choice]}\n")
                table.close()
            elif choice == 3:
                choice = "sandwich"
                stock["bread"] -= 1
                stock["ham"] -= 1
                stock["cheese"] -= 1
                table = open(filename, "a")
                table.write(f"Sandwich\t{fb_menu[choice]}\n")
                table.close()
            elif choice == 4:
                choice = "waffle"
                stock["waffle_doug"] -= 1
                stock["ice_cream"] -= 1
                stock["suryp"] -= 1
                table = open(filename, "a")
                table.write(f"Waffle\t{fb_menu[choice]}\n")
                table.close()
            elif choice == 5:
                break

        elif menu_choice == 4:
            print_bill(filename)
            exit()
        elif menu_choice == 5:
            print(stock)
        elif menu_choice == 6:
            print(f"Thank you for visiting {filename}, please come again.")
            exit()
        else:
            print_menu()

main_menu(filename, fb_menu, stock)