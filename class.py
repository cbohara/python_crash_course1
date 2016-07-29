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
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title() + " is a " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        print("Welcome to " + self.name.title() + "! We are open!")

    def set_number_served(self, number):
        if self.number_served < number:
            self.number_served += number
        else:
            print("This number can only increase!")


baby_moon = Restaurant('baby moon', 'italian')
baby_moon.describe_restaurant()
baby_moon.open_restaurant()
print(str(baby_moon.number_served))
baby_moon.number_served = 5
print(str(baby_moon.number_served))
baby_moon.set_number_served(10)
print(str(baby_moon.number_served))
baby_moon.set_number_served(5)

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'swirl']

    def flavor_listing(self):
        print("We have the following flavors:")
        for flavor in self.flavors:
            print(flavor)

banana_stand = IceCreamStand('banana stand', 'ice cream')
banana_stand.describe_restaurant()
banana_stand.flavor_listing()

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("This user's name is " + self.first_name.title() + " " +
                self.last_name.title() + ".")

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " +
                self.last_name.title() + "!")

    def increment_login_attempts(self, number):
        if self.login_attempts < number:
            self.login_attempts += number
        else:
            print("This can only be positive!")

    def reset_login_attempts(self):
        self.login_attempts = 0

me = User('charlie', 'omara')
me.describe_user()
me.greet_user()
print(str(me.login_attempts))
me.increment_login_attempts(10)
print(str(me.login_attempts))
me.reset_login_attempts()
print(str(me.login_attempts))

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privledges(self):
        print("The admin has the following privilege:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # make a Privileges instance as an attribute to the Admin class
        self.privileges = Privileges()

admin1 = Admin('charlie', 'boss')
admin1.greet_user()
admin1.privileges.show_privledges()

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # every attribute in a class needs an initial value, even if it's
        # 0 or an empty string
        # do not need to include a paramter for this attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#modifying an attribute's value directly
