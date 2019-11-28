import random

num1 = input("Please enter your 1st number for the lottery: ")
num2 = input("Please enter your 2nd number for the lottery: ")

randnum = random.randrange(10, 100)

strong_mtch = num1 + num2.format(num1, num2)
revers_mtch = num2 + num1.format(num2, num1)
weak_mtch = num1, num2.format(num1, num2)

if strong_mtch == str(randnum):
    print("Congratulations you have an exact match, you win R10 000.00")
elif revers_mtch == str(randnum):
    print("Congratulations you have all digits, you win R5 000.00")
elif weak_mtch == str(randnum):
    print("Congratulations you have one correct digit, you win R1 000.00")
else:
    print("Sorry no match")
