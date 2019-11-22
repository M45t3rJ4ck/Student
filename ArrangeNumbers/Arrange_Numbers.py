# Create a new Python file in this folder called “Optional_task.py”
# Create a text file called "numbers1.txt" that contains Integers which are sorted from smallest to largest.
# Create another text file called "numbers2.txt" which also contains Integers that are sorted from smallest to largest.
# Write the numbers from both files to a third file called "allNumbers.txt"
# All the numbers in "allNumbers.txt" should be sorted from smallest to largest.

file1 = open("numbers1.txt", "r+")
file2 = open("numbers2.txt", "r+")
file3 = open("allNumbers.txt", "w+")

anum = []

line1 = file1.read().strip(".")
anum.append(line1.split(","))

line2 = file2.read().strip(".")
anum.append(line2.split(","))

anum = anum[1] + anum[0]

file3.write(str(anum))

file1.close()
file2.close()
file3.close()
