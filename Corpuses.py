# =======Part 1: Working with the NLTK ===== #
from nltk.corpus import inaugural
print("\nPart 1:")
print(inaugural.words('2009-Obama.txt')[0:26])
print("End Part 1\n")
# ===  Part 2: Analysing tokens (words) of a text ===#
from nltk.book import *
print("\nPart 2:")
print(text1)
print(text6)
print("Printing first 100 words of text 1: \n" + str(list(text1)[0:100]))
print("Length of text 1: \n" + str(len(text1)))
print("Amount of unique words of text 1: \n" + str(len(set(text1))))
print("The lexical richness of a text 1: \n" + str(len(text1) / len(set(text1))))
print("The lexical richness of a text 6: \n" + str(len(text6) / len(set(text6))))
print("End Part 2\n")
# === Part 3: Analysing frequency of words ===#
from nltk import FreqDist
print("\nPart 3:")
fd = FreqDist(text1)
print("Amount of times 'the' appears in text 1: \n" + str(fd['the']))
print(fd.keys())
print(fd.items())
print("End Part 3\n")
# === Part 4: Your task ===#
print("\nPart 4:")
# 1.) Returns the 10 most frequent words in Obama's 2009 inaugural speech, including their frequencies
fd = FreqDist(inaugural.words('2009-Obama.txt'))
print(fd.most_common(10))
# 2.) Calculates the Lexical Richness of his speech
print(len('2009-Obama.txt') / len(set('2009-Obama.txt')))
# 3.) Calculate the average length of the sentences in his speech
print(len(inaugural.sents('2009-Obama.txt')))
print("\nOptional Part\n")


# 4.) Write a separate function called sent_length that takes in a string for the name of a text like '2009-Obama.txt', then finds the average
# length of the sentences in that speech. Compute the average length of sentences from the year of the first speech (1789) to the year of
# Obama's 2009 speech and see how the average length of sentences has changed over the time of the entire US's history. Remember that
# inaugural.fileids() will give you a list of all the String names of the speeches so you don't need to work out each name of each speech.
def sent_length():

    text_file = str(input("Enter the name of a text file : \n"))
    txt_fl = inaugural.sents(text_file)
    print(len(txt_fl))
    file_name = inaugural.fileids()
    print(len(inaugural.sents(file_name)))


print(sent_length())
print("End Part 4\n")
