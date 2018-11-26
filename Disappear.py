# Write a Python program called “disappear” to strip a set of characters from
# a string.
# Ask the user to input a string and then ask the user which characters they
# would like to make disappear.                                                                                                            
# For example: The quick brown fox jumps over the lazy dog.                                                                                      
# After stripping a,e,i,o,u                                                                                                         
# Th qck brwn fx jmps vr th lzy dg.  

# Acquiring user input
U_in = list(input("Please enter a sentence to manipulate: \n"))
U_out = list(input("Please enter the characters to remove: \n"))
# Converting operation
for chr in U_out:
    for chr in U_in:
        occur = U_in.count(chr)
        case = U_out.count(chr)
    
    
for index in U_out:
    U_in.remove(index)
print(U_in)
input("Press enter to exit")