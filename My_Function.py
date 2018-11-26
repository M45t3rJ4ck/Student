# Create a Python file called “myFunction.py” in this folder.
# Create your own function that prints all the days of the week
# Create your own function that takes in a sentence and replaces every second word with the word “Hello”

day = input("Pick a number between 1 and 7, q to quit: ")


def day_name():
    day = {"1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday", "6": "Saterday", "7": "Sunday", "q": "Quit"}
    return day


if day == "1":
    print(str(day_name.day("1")))
elif day == "2":
    print(str(day_name.day("2")))
elif day == "3":
    print(str(day_name.day("3")))
elif day == "4":
    print(str(day_name.day("4")))
elif day == "5":
    print(str(day_name.day("5")))
elif day == "6":
    print(str(day_name.day("6")))
elif day == "7":
    print(str(day_name.day("7")))
elif day == "q":
    exit()


sentence = str(input("Please enter a sentence: \n"))
               
lst = []
for idx, word in enumerate(sentence.split()):
    if idx % 2 == 0:
        lst.append(word)
        lst.append("hello")

words = " ".join(lst)
print(words)
