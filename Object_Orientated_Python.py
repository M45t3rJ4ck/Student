# ---------- LEARN TO PROGRAM 9 ----------
# Real world objects have attributes and capabilities
# A dog for example has the attributes of height, weight
# favorite food, etc.
# It has the capability to run, bark, scratch, etc.
# In object oriented programming we model real world objects
# be defining the attributes (fields) and capabilities (methods)
# that they have.
# A class is the template used to model these objects
# Here we will model a Dog object
import random
import math


class Dog:
    # The init method is called to create an object
    # We give default values for the fields if none are provided
    def __init__(self, name="", height=0, weight=0):
        # self allows an object to refer to itself
        # It is like how you refer to yourself with my
        # We will take the values passed in and assign
        # them to the new Dog objects fields (attributes)
        self.name = name
        self.height = height
        self.weight = weight
        # Define what happens when the Dog is asked to
        # demonstrate its capabilities

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))


def main():
    # Create a new Dog object
    spot = Dog("Spot", 66, 26)
    spot.bark()
    bowser = Dog("Bowser", 81, 46)
    bowser.bark()


main()


# ---------- GETTERS & SETTERS ----------
# Getters and Setters are used to protect our objects from assigning bad fields or for providing improved output
class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # This is the getter for height
    @property
    def height(self):
        print("Retrieving the height")
        # Put a __ before height to make this private field
        return self.__height

    # This is the setter for height
    @height.setter
    def height(self, value):
            # We protect the height from receiving a bad value
            if value.isdigit():
                # Put a __ before height to make this private field
                self.__height = value
            else:
                print("Please only enter numbers for height")

    # This is the getter for width
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    # This is the setter for width
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def get_area(self):
        return int(self.__width) * int(self.__height)


def main():
    a_square = Square()
    height = input("Enter height : ")
    width = input("Enter width : ")
    a_square.height = height
    a_square.width = width
    print("Height : ", a_square.height)
    print("Width : ", a_square.width)
    print("The Area is : ", a_square.get_area())


main()


# ---------- WARRIORS BATTLE ----------
# We will create a game with this sample output
'''
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious
Game Over
'''
# We will create a Warrior & Battle class
# Warriors will have names, health, and attack and block maximums
# They will have the capabilities to attack and block random amounts


class Warrior:
    def __init__(self, name="warrior", health=0, attk_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attk_max = attk_max
        self.block_max = block_max
    
    def attack(self):
        # Randomly calculate the attack amount
        # random() returns a value from 0.0 to 1.0
        attk_amt = self.attk_max * (random.random() + .5)
        return attk_amt
    
    def block(self):
        # Randomly calculate how much of the attack was blocked
        block_amt = self.block_max * (random.random() + .5)
        return block_amt


# The Battle class will have the capability to loop until 1 Warrior dies
# The Warriors will each get a turn to attack each turn
class Battle:
    def start_fight(self, warrior1, warrior2):
        # Continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        while True:
            if self.get_attack_result(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.get_attack_result(warrior2, warrior1) == "Game Over":
                print("Game Over")
            break
    
    # A function will receive each Warrior that will attack the other
    # Have the attack and block amounts be integers to make the results clean
    # Output the results of the fight as it goes
    # If a Warrior dies return that result to end the looping in the
    # above function
    # Make this method static because we don't need to use self
    @staticmethod
    def get_attack_result(warrior_a, warrior_b):
        warrior_a_attk_amt = warrior_a.attack()
        warrior_b_block_amt = warrior_b.block()
        damage2_warrior_b = math.ceil(warrior_a_attk_amt - warrior_b_block_amt)
        warrior_b.health = warrior_b.health - damage2_warrior_b
        print("{} attacks {} and deals {} damage".format(warrior_a.name, warrior_b.name, damage2_warrior_b))
        print("{} is down to {} health".format(warrior_b.name, warrior_b.health))
        if warrior_b.health <= 0:
            print("{} has Died and {} is Victorious".format(warrior_b.name, warrior_a.name))
            return "Game Over"
        else:
            return "Fight Again"


def main():
    # Create 2 Warriors
    paul = Warrior("Paul", 50, 20, 10)
    sam = Warrior("Sam", 50, 20, 10)
    # Create Battle object
    battle = Battle()
    # Initiate Battle
    battle.start_fight(paul, sam)


main()
