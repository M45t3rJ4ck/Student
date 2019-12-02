# Defining containers
Nums = []

# Colleting user input
U_num = int(input("Please enter a number: \n"))

Nums.append(U_num)

while U_num != -1:
    Nums.append(U_num)
    avg_nums = sum(Nums) / len(Nums)
    U_num = int(input("Please enter a number: \n"))
    if U_num == -1:
        print(avg_nums)
