# Collecting user input
U_num = int(input("Please enter a number above a 100: \n"))

# Defining operation
while U_num >= 100:
    U_num = int(input("I ment enter a number less than 100: \n"))
    if U_num % 2 == 0:
        print(int(U_num) * int("2"))
    else:
        print(int(U_num) * int("3"))
