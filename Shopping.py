#Ask user input:
print("All input expected to be: Product xx.xx")
prod1, prc1 = input("Please enter the 1st item and price: ").split()
prod2, prc2 = input("Please enter the 2nd item and price: ").split()
prod3, prc3 = input("Please enter the 3rd item and price: ").split()
#Define input:
prod1 = str(prod1)
prc1 = float(prc1)
prod2 = str(prod2)
prc2 = float(prc2)
prod3 = str(prod3)
prc3 = float(prc3)
#Define operation:
sum = prc1 + prc2 + prc3
avr = (prc1 + prc2 + prc3)/3
#Print out operations:
print("The total of {} & {} & {} is R{:.2f} and the average price is R{:.2f}".format(prod1, prod2, prod3, sum, avr))
