# Identify parameters
password = "rusty"
passList = []
attempts = 0
Incorr_pass = open("wrongpasswords.txt", "w")

# Collecting user input
U_password = str(input("Please enter your password: "))
if U_password != password:
    passList.append(U_password)
    attempts += 1
    Incorr_pass.write("Incorrect password " + str(attempts) + " : " + str(passList) + "\n")
    while U_password != password:
        U_password = str(input("Please enter your password: "))
        passList.append(U_password)
        attempts += 1
        Incorr_pass.write("Incorrect password " + str(attempts) + " : " + str(passList) + "\n")
        if U_password == password:
            print("Success! Wrong password text updated.")
Incorr_pass.close()
