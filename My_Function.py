# Create a Python file called “myFunction.py” in this folder.
# Create your own function that prints all the days of the week
# Create your own function that takes in a sentence and replaces every second word with the word “Hello”

U_day = input("Pick a number between 1 and 7 to view the day of the week, q to quit: \n")


def day_name(U_day):
    days = {"1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday", "6": "Saturday", "7": "Sunday", "q": "Quit"}
    return days.get(U_day)


if U_day == "1":
    print(str(day_name("1")))
elif U_day == "2":
    print(str(day_name("2")))
elif U_day == "3":
    print(str(day_name("3")))
elif U_day == "4":
    print(str(day_name("4")))
elif U_day == "5":
    print(str(day_name("5")))
elif U_day == "6":
    print(str(day_name("6")))
elif U_day == "7":
    print(str(day_name("7")))
elif U_day == "q":
    exit()


sentence = str(input("Please enter a sentence: \n"))

lst = []
for idx, word in enumerate(sentence.split()):
    if idx % 2 == 0:
        lst.append(word)
        lst.append("Hello")

words = " ".join(lst)
print(words)
