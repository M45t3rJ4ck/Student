#Triathlon Award Determiner
candidate = str(input("Welcome to the award ceremony, what is your name: \n"))
#Read Time(Minutes) - Swimming, Cycling, Running
tri_swi = 0
tri_cyc = 0
tri_run = 0
tri_swi = int(input("Please enter your time in minutes for 5km swimming: \n"))
tri_cyc = int(input("Please enter your time in minutes for 5km cycling: \n"))
tri_run = int(input("Please enter your time in minutes for 5km running: \n"))
#Calculate Total Triathlon Time
tri_time = 0
tri_time = (tri_swi) + (tri_cyc) + (tri_run)
tri_time = int(tri_time)
#Award Criteria
prov_col = 100
prov_half = 110
prov_scr = 115
prov_cer = 120
#Provincial Colours = -100min
if tri_time <= int(prov_col):
    print("Congratulations! " + str(candidate.upper()) + ", you're in 1st place with " + str(tri_time) + " minutes.")
#Provincial Half-Colours = -110min
elif tri_time <= int(prov_half):
    print("Nicely done! " + str(candidate.upper()) + ", you're in 2nd place with " + str(tri_time) + " minutes.")
#Provincial Scroll = -115min
elif tri_time <= int(prov_scr):
    print("Not bad! " + str(candidate.upper()) + ", you're in 3rd place with " + str(tri_time) + " minutes.")
#Provincial Certificate = -120min
elif tri_time <= int(prov_cer):
    print("Keep trying! " + str(candidate.upper()) + ", you're in 4th place with " + str(tri_time) + " minutes.")
#No Award = +120min
else:
    print("Maybe you should actually start practicing!?")
