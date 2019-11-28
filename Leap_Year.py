# Collecting user input
srt_yr = int(input("Please enter the year to start from: "))
chk_yr = int(input("For how many years do you want to check: "))

yr = srt_yr
leap = yr % 4

# Defining operations
for num in range(srt_yr, chk_yr):
    if yr % 4 != 0:
        print(str(yr) + " isn't a leap year")
        yr += 1
    elif yr % 4 == 0:
        print(str(yr) + " is a leap yr")
        yr += 1
