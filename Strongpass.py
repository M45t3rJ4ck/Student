# Declareing Boolean & variables
upCase = False
up_caseChk = ""
lowCase = False
low_caseChk = ""
haveNum = False
hav_numChk = ""
haveLenght = True
hav_lengChk = ""
Three_case = False
PassCorr = False

# Operations
print("Welcome to password checker")

# Calculating user input
up_caseChk = input("Does password contain 2 uppercase letters?(Y or N): \n")
up_caseChk = up_caseChk.upper()
if up_caseChk == "Y":
    upCase = True

low_caseChk = input("Does password contain 2 lowercase letters?(Y or N): \n")
low_caseChk = low_caseChk.upper()
if low_caseChk == "Y":
    lowCase = True

hav_numChk = input("Does password contain 2 numbers?(Y or N): \n")
hav_numChk = hav_numChk.upper()
if hav_numChk == "Y":
    haveNum = True

hav_lengChk = input("Does password contain 6 or more characters?(Y or N): \n")
hav_lengChk = hav_lengChk.upper()
if haveLenght == "Y":
    haveLenght = True

# Formating user input
if upCase and lowCase and haveNum == True:
    Three_case = True
if upCase and lowCase and haveLenght == True:
    Three_case = True
if upCase and haveNum and haveLenght == True:
    Three_case = True
if lowCase and haveNum and haveLenght == True:
    Three_case = True

# Validating user input
if Three_case == True:
    PassCorr = True
    print("Suitable password choosen")
else:
    print("You have not choosen a suitable password")
