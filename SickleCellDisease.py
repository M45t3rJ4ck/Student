#Part 1...
# Create a program called SickleCellDisease.py .
# We will simulate the effects of the Single Nucleotide Polymorphism that leads to this genetic disease. 
# Visit the website: http://www.cbs.dtu.dk/courses/27619/codon.html 
# Note the 'SLC' code for each Amino Acid.
# Write a function called translate that, when given a DNA sequence of arbitrary length,
# identifies and returns the amino acid sequence of the DNA using the amino acid SLC code found in that table.
# So basically, you would use an if - elif - elif .... else structure to translate each codon of DNA into the correct Amino Acid
# Note that the program must be able to handle DNA sequences that are not of a length dividible by 3.
# EG   DNA = Input : ATTATTATT
#            Output: III
# Remember: 
#	- len(DNA)  Will return the length of a String
#	- DNA[0:3]  Will get the first 3 characters of the string stored in DNA
#	- num = 3
#	- DNA[0:num]  Will also get the first till num characters of the string stored in DNA

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

print("...Welcome to the DNA decoding app...")
dna = input("Please enter the DNA sequence to decode: \n")
print(str(translate(dna)))





