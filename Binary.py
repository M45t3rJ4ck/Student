# Create a new Python file in this folder called “Binary.py”
# Write a program that can convert a binary number to a decimal number.
# A binary number is basically a number that is made up entirely of 0s and 1s (e.g 101101)
# You can represent any amount you would like using binary.
# Ask the user to enter a binary number and convert that number to a decimal number.
# You can visit the following site to find out how to convert from binary to decimal:
# Print out the decimal value of the number.
# Remember to make use of the built-in functions found in the math module as well as lists.

binary = []

bin2dec = int(input("Please enter your decimal number to convert: \n"))

remainder = int(bin2dec % 2)
binary.append(remainder)

while bin2dec != 1:
        bin2dec = int(bin2dec / 2)
        remainder = int(bin2dec % 2)
        binary.append(remainder)

binary = binary[::-1]

print("Binary: " + str(binary))
