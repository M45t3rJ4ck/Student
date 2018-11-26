'''
    After you've read and under all of example.py, create a new python file called amazon.py inside this folder. This programming problem is one posed to new
    software developer applicants to Amazon, the software development company you've probably bought a book or dvd from once in your life. Inside amazon.py, write
    Python code to read in the input of the textfile 'input.txt', and for each line in input.txt, write out a new line in a new text file output.txt that computes
    the answer to some operation on a list of numbers.

    If the input.txt file has the following:

    min: 1,2,3,5,6
    max: 1,2,3,5,6
    avg: 1,2,3,5,6

    Your program should generate an output.txt file as following:

    The min of [1, 2, 3, 5, 6] is 1
    The max of [1, 2, 3, 5, 6] is 6
    The avg of [1, 2, 3, 5, 6] is 3.4

    Assume that the only operatings given in the input file as 'min', 'max' and 'avg', and that the operation is always followed by a list of comma seperated integers.

    You should define a functions min, max and average that take in a list of integers and return the max, min or average of the list. 
    Your program should handle any combination of operations, any lengths of input numbers. You can assume that the list of input numbers are always valid ints, and is never empty.

'''

import re
import os
input_file = open("Input.txt", "r")
output_file = open("Output.txt", "w")
regex = re.compile(r"(?<=\w:)*\d")
nums = input_file.readline()
nums = re.findall(regex, nums)
Snums = [int(i) for i in nums]
from functools import reduce
Snums = reduce(lambda x, y: x + y, Snums)
maximum = max(nums)
minimum = min(nums)
average = (Snums / len(nums))
output_file.write(" The max of " + str(nums) + " is " + str(maximum) + ". \n")
output_file.write(" The min of " + str(nums) + " is " + str(minimum) + ". \n")
output_file.write(" The avg of " + str(nums) + " is " + str(average) + ". \n")
input_file.close()
output_file.close()
