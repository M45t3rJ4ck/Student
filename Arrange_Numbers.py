# ================= BONUS Optional Task ==================
# Create a new Python file in this folder called “Optional_task.py”
# Create a text file called "numbers1.txt" that contains Integers which are sorted from smallest to largest.
# Create another text file called "numbers2.txt" which also contains Integers that are sorted from smallest to largest.
# Write the numbers from both files to a third file called "allNumbers.txt"
# All the numbers in "allNumbers.txt" should be sorted from smallest to largest.

file1 = open("numbers1.txt", "r+")
file2 = open("numbers2.txt", "r+")
file3 = open("allNumbers.txt", "r+")
anum = []
while True:
    line = file1.read
    anum.append(line)
    line = file2.read
    anum.append(line)
    if not line:
        break
    print(anum)
print("Operation completed")
file1.close()
file2.close()
file3.close()
