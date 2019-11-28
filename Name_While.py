# Defining containers
names = []

name = str("hyper")

sum_names = sum(names)
uname_count = 0

# Collecting user input
uname = input("Please enter a name: \n")

names.append(uname)

uname_count += 1

while uname != name:
    uname = input("Please enter a name: \n")
    names.append(uname)
    uname_count += 1
    if uname == name:
        print(len(names))
    elif uname_count == 10:
        exit()
