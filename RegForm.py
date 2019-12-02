# ================= Compulsory Task ==================
# We will write a program that allows students to register for an exam venue.
# First ask the user how many students are registering.
# Create a for loop that runs for that amount of students
# Each loop asks for the student to enter their ID numbers.
# Write each of the ID numbers to a Text File called “RegForm.txt”
# This will be used as an attendance register that they will sign when they arrive at the exam venue


Indnum = int(input("How many students are registering: \n"))

Fname = ()
Lname = ()
IDnum = ()
Ssign = ("Sign:_________")

studnum = 0

file = open("RegForm.txt", "w")

for num in range(Indnum):
    if studnum < Indnum:
        Fname, Lname = input("Please enter your name and surname: \n").split()
        IDnum = input("Please enter your ID number: \n")
        student = [Fname, Lname, IDnum, Ssign]
        file.write(str(student) + "\n")
        studnum += 1
    elif studnum == Indnum:
        print("\nRegistration completed")

file.close()
