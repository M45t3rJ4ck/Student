import random
user_int = int(input("Please enter a number: "))
num = random.randint(1, 11)
if user_int == num and user_int % 2 == 0:
    print("True" and "True")
elif user_int != num and user_int % 2 == 0:
    print("False" and "True")
else:
    print("All False!")
