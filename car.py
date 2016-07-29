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

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85

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
