#Collecting Libraries
import math
#Setting Variables & Collecting input
P = int(input("Please enter the initial deposit amount: \n"))
i = int(input("Please enter the initial interest rate: \n"))
t = int(input("Please enter the initial years of investment: \n"))
interest = str(input("Is this simple or compound investment: \n"))
r = (i) / 100
#Setting Operation
if interest == "simple":
    invest = (P) * (1 + (r) * (t))
    print(int(invest))
elif interest == "compound":
    invest = P * math.pow((1 + (r)), (t))
    print(int(invest))
else:
    print("Make sense please")
