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


def mutate():
    in_file = open("dna.txt", "r")
    dna_seq = in_file.read()
    in_file.close()
    
    regex = re.compile("a")
    for line in dna_seq:
        out_fl1 = open("normalDNA.txt", "w")
        nor_dna = regex.sub("A", dna_seq)
        out_fl1.write(nor_dna)
        out_fl1.close()

        out_fl2 = open("mutatedDNA.txt", "w")
        mut_dna = regex.sub("T", dna_seq)
        out_fl2.write(mut_dna)
        out_fl2.close()


def translate(dna):
    dna = list(dna.upper())
    slc = ""
    while len(dna) != 0:
        if len(dna) >= 3:
            codon = dna[0:3]
            if codon == ["A", "T", "T"] or codon == ["A", "T", "C"] or codon == ["A", "T", "A"]:
                slc += "I"
                del dna[0:3]
            elif codon == ["C", "T", "T"] or codon == ["C", "T", "C"] or codon == ["C", "T", "A"] or codon == ["T", "T", "A"] or codon == ["T", "T", "G"]:
                slc += "L"
                del dna[0:3]
            elif codon == ["G", "T", "T"] or codon == ["G", "T", "C"] or codon == ["G", "T", "A"] or codon == ["G", "T", "G"]:
                slc += "V"
                del dna[0:3]
            elif codon == ["T", "T", "T"] or codon == ["T", "T", "C"]:
                slc += "F"
                del dna[0:3]
            elif codon == ["A", "T", "G"]:
                slc += "M"
                del dna[0:3]
            elif codon == ["T", "G", "T"] or codon == ["T", "G", "C"]:
                slc += "C"
                del dna[0:3]
            elif codon == ["G", "C", "T"] or codon == ["G", "C", "C"] or codon == ["G", "C", "A"] or codon == ["G", "C", "G"]:
                slc += "A"
                del dna[0:3]
            elif codon == ["G", "G", "T"] or codon == ["G", "G", "C"] or codon == ["G", "G", "A"] or codon == ["G", "G", "G"]:
                slc += "G"
                del dna[0:3]
            elif codon == ["C", "C", "T"] or codon == ["C", "C", "C"] or codon == ["C", "C", "A"] or codon == ["C", "C", "G"]:
                slc += "P"
                del dna[0:3]
            elif codon == ["A", "C", "T"] or codon == ["A", "C", "C"] or codon == ["A", "C", "A"] or codon == ["A", "C", "G"]:
                slc += "T"
                del dna[0:3]
            elif codon == ["T", "C", "T"] or codon == ["T", "C", "C"] or codon == ["T", "C", "G"] or codon == ["A", "G", "T"] or codon == ["A", "G", "C"]:
                slc += "S"
                del dna[0:3]
            elif codon == ["T", "A", "T"] or codon == ["T", "A", "C"]:
                slc += "Y"
                del dna[0:3]
            elif codon == ["T", "G", "G"]:
                slc += "W"
                del dna[0:3]
            elif codon == ["C", "A", "A"] or codon == ["C", "A", "G"]:
                slc += "Q"
                del dna[0:3]
            elif codon == ["A", "A", "T"] or codon == ["A", "A", "C"]:
                slc += "N"
                del dna[0:3]
            elif codon == ["C", "A", "T"] or codon == ["C", "A", "C"]:
                slc += "H"
                del dna[0:3]
            elif codon == ["G", "A", "A"] or codon == ["G", "A", "C"]:
                slc += "E"
                del dna[0:3]
            elif codon == ["G", "A", "T"] or codon == ["G", "A", "C"]:
                slc += "D"
                del dna[0:3]
            elif codon == ["A", "A", "A"] or codon == ["A", "A", "G"]:
                slc += "K"
                del dna[0:3]
            elif codon == ["C", "G", "T"] or codon == ["C", "G", "C"] or codon == ["C", "G", "A"] or codon == ["C", "G", "G"] or codon == ["A", "G", "A"] or codon == ["A", "G", "G"]:
                slc += "R"
                del dna[0:3]
            elif codon == ["T", "A", "A"] or codon == ["T", "A", "G"] or codon == ["T", "G", "A"]:
                slc += "Stop"
                del dna[0:3]
        else:
            break
    return slc


print("...Welcome to the dna decoding app...")
question = input("Would you like to submit a file or type the sequence(file/sequence)? ")
if question == "file":
    mutate()
else:
    dna = input("Please enter the dna sequence to decode: \n")
    print(str(translate(dna)))
