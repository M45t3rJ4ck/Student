import random
import math
#With lists we can refer to groups of data in 1 name
#[0:"string"][1:1.1234][2:28]["c"]
#Python list can grow and contain data of any type
randList = ["string", 1.1234, 28]
#Create a list with range
oneToTen = list(range(10))
#Can use same functions for lists as with strings
#Conbine Lists
randList = randList + oneToTen
#Get ht e1st item with an index
print(randList[0])
#Get the length
print("List Length: ",len(randList))
#Slice list for 1st 3 items
first3 = randList[0:3]
#Cycle through list and print indexs
for i in first3:
    print("{} : {}".format(first3.index(i), i))
#To repeat an list item
print(first3[0] * 3)
#To check for item in lists
print("string" in first3)
#Get index of matching item
print("Index number of string: ",first3.index("string"))
#How many times an item appeares
print("How many strings are there: ",first3.count("string"))
#To change a list item
first3[0] = "New String"
for i in first3:
    print("{} : {}".format(first3.index(i), i))
#Append a value to end of list
first3.append("Another")
for i in first3:
    print("{} : {}".format(first3.index(i), i))

#PROBLEM -> CREATE A RANDOM LIST:
#Generate a random list of 5 values (1 - 9)
numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))
for i in numList:
    print(i)

#BUBBLE SORT A LIST:
numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))
i = len(numList) - 1
while i > 1:
    j = 0
    while j < i:
        #Tracking comparison of values
        print("\nls {} > {}".format(numList[j], numList[j + 1]))
        #If value on left bigger...switch
        if numList[j] > numList[j + 1]:
            print("Switching")
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Not Switching")
        j += 1
        #Track changes to list
        for k in numList:
            print(k, end= ", ")
        print()
    print("End Of Round")
    i -= 1
for k in numList:
    print(k, end= ", ")
print()

#MORE FUNCTIONS
numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))
#To sort a list
numList.sort()
#To reverse a list
numList.reverse()
#To insert values
numList.insert(5, 10)
#To delete a value
numList.remove(10)
#To remove index item
numList.pop(2)
for k in numList:
    print(k, end=", ")
print()

#LIST COMPREHENSIONS
#To construct a list
evenList = [i * 2 for i in range(10)]
for k in evenList:
    print(k, end=",")
print()
#List of lists
numList = [1, 2, 3, 4, 5]
listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]
for k in listOfValues:
    print(k)
print()
#Create a 10x10 list
multiDlist = [[0] * 10 for i in range(10)]
#Change a value
multiDlist[0][1] = 10
#Get the 2nd item in list 1
print(multiDlist[0][1])
#Get the 2nd item in list 2
print(multiDlist[1][1])

#MULTIDIMENSIONAL LISTS
#Show how indexes work
listTable = [[0] * 10 for i in range(10)]
for i in range(10):
    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)
for i in range(10):
    for j in range(10):
        print(listTable[i][j], end="||")
    print()

#PROBLEM -> CREATE MULTIPLICATION TABLE:
#With 2 for loops fill cells using values (1 -> 9)
#Create a multidimensional list
ListTable = [[0] * 10 for i in range(10)]
#To increment for each row
for i in range(1, 10):
    #To incement for each item in the row
    for j in range(1, 10):
        #Assign value to a cell
        ListTable[i][j] = i * j
#Output data as assigned
for i in range(1, 10):
    for j in range(1, 10):
        print(ListTable[i][j], end=" , ")
    print()