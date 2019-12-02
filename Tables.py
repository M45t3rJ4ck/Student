# Collecting user input
tab_num = int(input("Please enter the number for the time table you want: \n"))

# Defining operations
print("The " + str(tab_num) + " times table is: \n")

for num in range(1, 13):
    ans_num = int(tab_num) * int(num)
    if num < 13:
        print(str(tab_num) + " x " + str(num) + " = " + str(ans_num))
