# Write a program called “seperation.py” which inputs a sentence and displays
# each word of the sentence on a separate line.

U_sep = input("Please enter a sentence: \n")
sep = U_sep.split()
for word in sep:
    print(word, end="\n")
