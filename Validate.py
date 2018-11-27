numStr = str(input("Please enter your favourite number: "))
numInt1 = str("3")
numInt2 = str("2")
if numStr in numInt1:
    print("You're in luck...it was 3!")
elif numStr in numInt2:
    print("You're still in luck...it was 2!")
else:
    print("User must enter a number!!")
