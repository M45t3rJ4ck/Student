# ---------- STATIC METHODS ----------
# Static methods allow access without the need to initialize
# a class. They should be used as utility methods, or when
# a method is needed, but it doesn't make sense for the real
# world object to be able to perform a task


class Sum:

    # You use the static method decorator to define that a method is static
    @staticmethod
    def getSum(*args):

        sum = 0

        for i in args:
            sum += i

        return sum


def main():

    # Call a static method by proceeding it with its class name
    print("Sum :", Sum.getSum(1, 2, 3, 4, 5))


main()


# ---------- STATIC VARIABLES ----------
# Fields declared in a class, but outside of any method
# are static variables. There value is shared by every
# object of that class

class Dog:

    # This is a static variable
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name
        # You reference the static variable by proceeding it with the class name
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():

    spot = Dog("Spot")
    doug = Dog("Doug")
    spot.getNumOfDogs()


main()


# ---------- MODULES ----------
# Your Python programs will contain a main program that includes your main function. Then you will create many
# modules in separate files. Modules also end with .py just like any other Python file 
# ————— sum.py —————
def getSum(*args):
    
    sum = 0

    for i in args:
        sum += i

    return sum

# ————— End of sum.py —————