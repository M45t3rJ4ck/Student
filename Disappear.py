# Write a Python program called “disappear” to strip a set of characters from a string.
# Ask the user to input a string and then ask the user which characters they would like to make disappear.                                                                                                            
# For example: The quick brown fox jumps over the lazy dog.                                                                                      
# After stripping a,e,i,o,u                                                                                                         
# Th qck brwn fx jmps vr th lzy dg.  

# Acquiring user input
U_in = list(input("Please enter a sentence to manipulate: \n"))
U_out = list(input("Please enter the characters to remove: \n"))

for letter in U_in:
    for chr in U_out:
        if letter == chr:
            U_in.remove(letter)

print(U_in)