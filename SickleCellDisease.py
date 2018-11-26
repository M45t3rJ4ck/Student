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

def translate(DNA):
    DNA = list(DNA)
    slc = ""
    while len(DNA) > 0:
        if len(DNA) >= 3:
            codon = DNA[0:3]
            if codon == ["A","T","T"] or ["A","T","C"] or ["A","T","A"]:
                slc += "I"
                del DNA[0:3]
            elif codon == ["C","T","T"] or ["C","T","C"] or ["C","T","A"] or ["T","T","A"] or ["T","T","G"]:
                slc += "L"
                del DNA[0:3]
            elif codon == ["G","T","T"] or ["G","T","C"] or ["G","T","A"] or ["G","T","G"]:
                slc += "V"
                del DNA[0:3]
            elif codon == ["T","T","T"] or ["T","T","C"]:
                slc += "F"
                del DNA[0:3]
            elif codon == ["A","T","G"]:
                slc += "M"
                del DNA[0:3]
            elif codon == ["T","G","T"] or ["T","G","C"]:
                slc += "C"
                del DNA[0:3]
            elif codon == ["G","C","T"] or ["G","C","C"] or ["G","C","A"] or ["G","C","G"]:
                slc += "A"
                del DNA[0:3]
            elif codon == ["G","G","T"] or ["G","G","C"] or ["G","G","A"] or ["G","G","G"]:
                slc += "G"
                del DNA[0:3]
            elif codon == ["C","C","T"] or ["C","C","C"] or ["C","C","A"] or ["C","C","G"]:
                slc += "P"
                del DNA[0:3]
            elif codon == ["A","C","T"] or ["A","C","C"] or ["A","C","A"] or ["A","C","G"]:
                slc += "T"
                del DNA[0:3]
            elif codon == ["T","C","T"] or ["T","C","C"] or ["T","C","G"] or ["A","G","T"] or ["A","G","C"]:
                slc += "S"
                del DNA[0:3]
            elif codon == ["T","A","T"] or ["T","A","C"]:
                slc += "Y"
                del DNA[0:3]
            elif codon == ["T","G","G"]:
                slc += "W"
                del DNA[0:3]
            elif codon == ["C","A","A"] or ["C","A","G"]:
                slc += "Q"
                del DNA[0:3]
            elif codon == ["A","A","T"] or ["A","A","C"]:
                slc += "N"
                del DNA[0:3]
            elif codon == ["C","A","T"] or ["C","A","C"]:
                slc += "H"
                del DNA[0:3]
            elif codon == ["G","A","A"] or ["G","A","C"]:
                slc += "E"
                del DNA[0:3]
            elif codon == ["G","A","T"] or ["G","A","C"]:
                slc += "D"
                del DNA[0:3]
            elif codon == ["A","A","A"] or ["A","A","G"]:
                slc += "K"
                del DNA[0:3]
            elif codon == ["C","G","T"] or ["C","G","C"] or ["C","G","A"] or ["C","G","G"] or ["A","G","A"] or ["A","G","G"]:
                slc += "R"
                del DNA[0:3]
            elif codon == ["T","A","A"] or ["T","A","G"] or ["T","G","A"]:
                slc += "Stop"
                del DNA[0:3]
        else:
            break
    return slc
            
print("...Welcome to the DNA decoding app...")
DNA = input("Please enter the DNA sequence to decode: \n").upper()
print(str(translate(DNA)))





