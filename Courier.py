#Setting costs:
Air = 0.36
Freight = 0.25
Full_ins = 50
Lim_ins = 25
A_gift = 15
N_gift = 0
Priority = 100
Standard = 20
#Setting Account:
Travel = 0
Insurance = 0
Gift = 0
Importance = 0
Userf_cost = 0
#Determining cost to user
User_trav = False
User_sec = False
User_int = False
User_vip = False
#Getting the usr input
sending = input("How would you like to send the item by air? (Y or N) \n")
if sending == "Y":
    User_trav = True    
safety = input("Would you like full insurance? (Y or N) \n")
if safety == "Y":
    User_sec = True
needs = input("Will you be sending this item as a gift? (Y or N) \n")
if needs == "Y":
    User_int = True
urgency = input("Is this delivery important? (Y or N) \n")
if urgency == "Y":
    User_vip = True
User_dist = float(input("Please enter the total distance in kilometers: \n"))
#Calculate travel cost
if User_trav == True:
                Travel = float(Air * User_dist)
else:
                Travel = float(Freight * User_dist)
#Calculate insurance cost
if User_sec == True:
                  Insurance = Full_ins
else:

                  Insurance = Lim_ins
#Calculate gift
if User_int == True:
                  Gift = A_gift
else:
                  Gift = N_gift
#Calculate importance
if User_vip == True:
                  Importance = Priority
else:
                  Importance = Standard
#Calculate final cost to user
Userf_cost = (Travel + Insurance + Gift + Importance)
#Output Operations
print("Your total cost is: ", Userf_cost)
