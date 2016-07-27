# capitalized names refer to classes
class Dog():
    """A simple attempt to model a dog."""
    # self must be first and included in the class definition
    # self = reference to the instance of the class AKA object
    # every method call associated with the class automatically passes self
        # so only need to provide the name and age parameters
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # any variable prefixed with self is available to every method in the class
        # attributes = variables that are accessible through instances of a class
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

# when Python reads this line, it calls the __init__() method with the arguments
# 'ranger' and 14 and returns an instance representing this dog
ranger = Dog('ranger', 14)
print("My dog's name is " + ranger.name.title() + ".")
print("My dog is " + str(ranger.age) + " years old.")
ranger.sit()
ranger.roll_over()

lucy = Dog('lucy', 3)
print("I had a dog growing up, and her name was " + lucy.name.title() + ".")
print(lucy.name.title() + " is in doggy heaven but still like a puppy of age " +
        str(lucy.age) + " in my mind.")

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + " is a " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        print("Welcome to " + self.name.title() + "! We are open!")

baby_moon = Restaurant('baby moon', 'italian')
baby_moon.describe_restaurant()
baby_moon.open_restaurant()

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("This user's name is " + self.first_name.title() + self.last_name.title())

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")

me = User('charlie', 'omara')
me.describe_user()
me.greet_user()
