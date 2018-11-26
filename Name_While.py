# Defining containers
Names = []
name = str("hyper")
sum_names = sum(Names)
uname_count = 0

# Collecting user input
U_name = input("Please enter a name: \n")
Names.append(U_name)
uname_count += 1
while U_name != name:
    U_name = input("Please enter a name: \n")
    Names.append(U_name)
    uname_count += 1
    if U_name == name:
        print(len(Names))
    elif uname_count == 10:
        exit()
