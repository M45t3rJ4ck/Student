# Write a Python program called “counting.py” to count the number of characters (character frequency) in a string. 
# Store each letter followed by the number of occurrences in a list and print
# it out. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

U_in = list(input("Enter characters to count: \n"))
for chr in U_in:
    occur = U_in.count(chr)
    print(f"{chr} : {occur}", end=", ")
