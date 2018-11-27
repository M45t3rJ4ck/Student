# Identify correct password
password = "rusty"
passList = []
Incorr_pass = open("wrongpasswords.txt", "w")
attempts = 0
countDifference = 0

# Collecting user input
U_password = input("Please enter your password: ")
if U_password != password:
    passList.append(U_password)
    attempts += 1
    countDifference = len(U_password) - len(password)
    Incorr_pass.write("Incorrect password " + str(attempts) + " : " + str(passList[attempts-1]) + " wrong by " + str(countDifference) + " characters." + "\n")
    while U_password != password:
            U_password = input("Please enter your password: ")
            passList.append(U_password)
            attempts += 1
            countDifference = len(U_password) - len(password)
            Incorr_pass.write("Incorrect password " + str(attempts) + " : " + str(passList[attempts-1]) + " wrong by " + str(countDifference) + " characters." + "\n")
            if U_password == password:
                    print("Success! Wrong password text updated.")
Incorr_pass.close()
