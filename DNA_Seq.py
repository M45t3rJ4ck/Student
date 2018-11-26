# Part 2...
# Add another function to the program SickleCellDisease.py called 'mutate'.
# This function must read in the contents of the text file named 'dna.txt' 
# It must then identify the first occurrence of the lowercase letter 'a' in 'dna.txt'.
# You must then write two new text files, one named normalDNA.txt and the other named mutatedDNA.txt.
# The normalDNA.txt must have the same dna sequence as dna.txt with the 'a' changed to an 'A'.
# The mutatedDNA.txt must have the same dna sequence as dna.txt with the 'a' changed to a 'T'.
# Now create a new function, txtTranslate, that calls the translate function that you wrote in Part 1, to take in text
#  file input.
# Call it on both mutatedDNA.txt and normalDNA.txt, and output both Amino Acid sequences to the user.

import re

in_file = open("dna.txt", "r")
dna = in_file.readlines()
in_file.close()
dna = str(dna)
print(dna)
lowerCS = re.compile(r"[a]?\n")
matches = re.findall(lowerCS, dna)
print(str(matches))
out_fl1 = open("mutatedDNA.txt", "w")
out_fl2 = open("normalDNA.txt", "w")


def mutate():
    dna = re.sub(r"(\w{0+}) + (a) + (\w{0+})\n", r"T", dna)
    out_fl1.write(str(translate(dna)))
    dna = re.sub(r"(\w[0+]) + (a) + (\w[0+])\n", r"A", dna)
    out_fl2.write(str(translate(dna)))


def translate(dna):
    dna = list(dna)
    slc = ""
    while len(dna) > 0:
        if len(dna) >= 3:
            codon = dna[0:3]
            if codon == ["A", "T", "T"] or ["A", "T", "C"] or ["A", "T", "A"]:
                slc += "I"
                del dna[0:3]
            elif codon == ["C", "T", "T"] or ["C", "T", "C"] or ["C", "T", "A"] or ["T", "T", "A"] or ["T", "T", "G"]:
                slc += "L"
                del dna[0:3]
            elif codon == ["G", "T", "T"] or ["G", "T", "C"] or ["G", "T", "A"] or ["G", "T", "G"]:
                slc += "V"
                del dna[0:3]
            elif codon == ["T", "T", "T"] or ["T", "T", "C"]:
                slc += "F"
                del dna[0:3]
            elif codon == ["A", "T", "G"]:
                slc += "M"
                del dna[0:3]
            elif codon == ["T", "G", "T"] or ["T", "G", "C"]:
                slc += "C"
                del dna[0:3]
            elif codon == ["G", "C", "T"] or ["G", "C", "C"] or ["G", "C", "A"] or ["G", "C", "G"]:
                slc += "A"
                del dna[0:3]
            elif codon == ["G", "G", "T"] or ["G", "G", "C"] or ["G", "G", "A"] or ["G", "G", "G"]:
                slc += "G"
                del dna[0:3]
            elif codon == ["C", "C", "T"] or ["C", "C", "C"] or ["C", "C", "A"] or ["C", "C", "G"]:
                slc += "P"
                del dna[0:3]
            elif codon == ["A", "C", "T"] or ["A", "C", "C"] or ["A", "C", "A"] or ["A", "C", "G"]:
                slc += "T"
                del dna[0:3]
            elif codon == ["T", "C", "T"] or ["T", "C", "C"] or ["T", "C", "G"] or ["A", "G", "T"] or ["A", "G", "C"]:
                slc += "S"
                del dna[0:3]
            elif codon == ["T", "A", "T"] or ["T", "A", "C"]:
                slc += "Y"
                del dna[0:3]
            elif codon == ["T", "G", "G"]:
                slc += "W"
                del dna[0:3]
            elif codon == ["C", "A", "A"] or ["C", "A", "G"]:
                slc += "Q"
                del dna[0:3]
            elif codon == ["A", "A", "T"] or ["A", "A", "C"]:
                slc += "N"
                del dna[0:3]
            elif codon == ["C", "A", "T"] or ["C", "A", "C"]:
                slc += "H"
                del dna[0:3]
            elif codon == ["G", "A", "A"] or ["G", "A", "C"]:
                slc += "E"
                del dna[0:3]
            elif codon == ["G", "A", "T"] or ["G", "A", "C"]:
                slc += "D"
                del dna[0:3]
            elif codon == ["A", "A", "A"] or ["A", "A", "G"]:
                slc += "K"
                del dna[0:3]
            elif codon == ["C", "G", "T"] or ["C", "G", "C"] or ["C", "G", "A"] or ["C", "G", "G"] or ["A", "G", "A"] \
                    or ["A", "G", "G"]:
                slc += "R"
                del dna[0:3]
            elif codon == ["T", "A", "A"] or ["T", "A", "G"] or ["T", "G", "A"]:
                slc += "Stop"
                del dna[0:3]
        else:
            break
    return slc


print("...Welcome to the dna decoding app...")
dna = input("Please enter the dna sequence to decode: \n")
print(str(translate(dna)))
out_fl1.close()
out_fl2.close()
