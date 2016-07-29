class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # every attribute in a class needs an initial value, even if 0 or ""
        # setting a default value for a car?
        # do not need to include as a parameter
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print(str(self.year) + " " + self.make.title() + " " + self.model.title())

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rollback the odometer!")

    def increment_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("You cannot rollback the odometer!")

    def fill_gas_tank(self, miles):
        print("You need to fill the tank every " + str(self.miles) + " miles.")

# my_car = Car("subaru", "legacy", 2003)
# my_car.get_descriptive_name()
# my_car.read_odometer()
# my_car.odometer_reading = 23
# my_car.read_odometer()
# my_car.update_odometer(50)
# my_car.read_odometer()
# my_car.update_odometer(20)
# my_car.increment_odometer(100)
# my_car.read_odometer()
# my_car.increment_odometer(500)
# my_car.read_odometer()
# my_car.increment_odometer(-20)

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        # special function that makes connections between parent and child class
        # aka inherit from super class, and electric car is the subclass
        super().__init__(make, model, year)
        # inherit attributes and methods from parent battery class
        self.battery = Battery()

    # override method from parent class by making a method of the same name
    # in the child class
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
"""
when we want to describe the battery, we need to work through the car's battery attribute

this line tells python to look at the instance of my_tesla, find its battery
attribute, and call the method describe_battery() that's associated with the
Battery instance stored in the attribute
"""
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
