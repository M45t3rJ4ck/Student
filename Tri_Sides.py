# Get user input:
side1, side2, side3 = input("Please enter the 3 side of your triangle, separated by a space: \n").split()

# Define user input:
side1 = float(side1)
side2 = float(side2)
side3 = float(side3)

# Define Operations:
sides = (side1 + side2 + side3) / 2

# Print Operations:
print("{:.2f}".format(sides))
