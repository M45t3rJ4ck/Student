# collecting user input
Weight = float(input("Please enter your weight in kilograms: \n"))
Hight = float(input("Please enter your hight in meters: \n"))

# Formula for BMI
BMI = (Weight) / ((Hight) * (Hight))
if BMI >= 30:
    print("You're qualified as obese, BMI: {:.2f} ".format(BMI))
elif BMI >= 25:
    print("You're qualified as overweight, BMI: {:.2f} ".format(BMI))
elif BMI >= 18.5:
    print("You're in the normal range, BMI: {:.2f} ".format(BMI))
else:
    print("You're underweight, BMI: {:.2f} ".format(BMI))
