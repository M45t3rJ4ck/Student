# DICTIONARIES:
# Lists organize data based on sequential indexes
# Dictionaries use keys/value pairs

# Create a dictionary
namedict = {"fname": "Riaan", "mname": "Willem Adriaan", "lname": "Voges", "address": "Bosmanstraat 48"}

# Get value using key
print("My Name: ", namedict["fname"])

# Change value with key
namedict["address"] = "48 Bosman Street"

# Dictionaries are created out of order and will print as such
print(namedict)

# Adding a key and value
namedict["city"] = "Kuilsrivier"

# Check in keys exists
print(namedict.values())

# Check list of keys
print(namedict.keys())

# Get keys and values of items
for k, v in namedict.items():
    print(k, v)

# Get value associated with keys
print(namedict.get("mname", "Not Here"))

# Delete a key value
del namedict["fname"]

# Loop through the keys
for i in namedict:
    print(i)

# Delete all entries
namedict.clear()

# Holding list dictionaries
employees = []

# Input employee data
fname, lname = input("Enter employee name: ").split()
employees.append({"fname": fname, "lname": lname})
print(employees)

# PROBLEM -> CREATE A CUSTOMER LIST:
# Create List(array) of customer outside for loop
customer = []

# Create a loop
while True:

    # Get input and make it work for y or n
    createntry = input("Enter a new customer?(Y/N): ")
    createntry = createntry[0].lower()
    if createntry == "n":

        # Check to leave loop
        break
    else:

        # Get customer data
        fname, lname = input("Enter new customer first and last name: ").split()

        # Add customer data to list
        customer.append({"fname": fname, "lname": lname})

# Print customer data
for cust in customer:
    print(cust["fname"], cust["lname"])


# RECURSIVE FUNCTIONS:
# A function refering to itself inside itself
def factorial(num):

    # Every function to contain condition to cease itself
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result


print(factorial(4))


# PROBLEM -> CALCULATE FIBONACCI NUMBERS:
# To calculate sum the previous 2 numbers
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fibonacci(num - 1) + fibonacci(num - 2)
        return result


print(fibonacci(3))
