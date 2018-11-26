# logical error - new lines inbetween code has been removed, operations got defined.
# Defining operation - no indications off operation logic was used to set application apart

# I'm 24 years old - moved to it's own line
ageStr = str("24 years old")  # compilation error due to indintation and casting was not used, moved up;
age = int(ageStr[0:2])  # compilation error due to indintation and incorrect casting value indicated, moved up;
three = int("3")  # compilation error due to indintation and casting was not used, moved up;
answerMonths = (int(age) * int("12")) + (int(three) * int("12")) + int("6")  # logical error and compilation error operation was undefined and maths was incorrect, moved up;
answerYears = int(answerMonths) / int("12")  # compilation error due to indintation and logical error due to location and maths error, moved up;

# Operation
print("Welcome to the error program.")  # logical error, moved down to follow a logical order for operations and compilation error, parenthasis was left out including new line removed;
print("I'm "+ str(age) +" years old.")  # logical error, moved down to follow a logical order for operations and compilation error, casting was done incorrectly;
print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old")  # logical error, moved up to follow a logical order for operations and compilation error, casting was done incorrectly;
print("The total number of years: " + str(answerYears))  # logical error, moved down to follow a logical order for operations and compilation error, casting was done incorrectly;
# HINT, 330 months is the correct answer
