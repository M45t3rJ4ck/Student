# Program to count characters, words, line and vowels from file:
# Open and indicate file and location
f = open("input.txt", "r+")
# Defining variable holders
crcount = 0
linenum = 0
# deining operation
while True:
    for line in f:
        linenum += 1
    print(linenum)
    for chr in f:
        crcount += 1
    print(crcount)

