# Create a new Python file in this folder called
# Create a new text file in this folder called input.txt
# In the input.txt file enter some text, making sure it is at least a few lines long.
# Write a program the will count the number of characters, words and lines in the file.
# Your program should also count the number of vowels (a's, e's, i's, o's and u's) in the file.
# Print out your results.

# Program to count characters, words, line and vowels from file:
import re

# Open and indicate file and location
file = open("input.txt", "r")

# Defining variable holders
lineNum = 0
wordNum = 0
charNum = 0
vowels = ["a", "e", "i", "o", "u"]
vowelsNum = 0

# Deining operation
f = file.read().split("\n")

for line in f:
    lineNum += 1
    regex_word = re.compile("[a-zA-Z?'s]+")
    wordList = regex_word.findall(line)
    for word in wordList:
        wordNum += 1
        regex_char = re.compile("[a-zA-Z'.,]")
        charList = regex_char.findall(word)
        for char in charList:
            charNum += 1
            regex_vowels = re.compile("[aeiouAEIOU]+")
            vowelList = regex_vowels.findall(char)
            for vowel in vowelList:
                vowelsNum += 1

print(f"Line Numbers: {lineNum}")
print(f"Word Numbers: {wordNum}")
print(f"Character Numbers: {charNum}")
print(f"Vowels Numbers: {vowelsNum}")
