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

my_car = Car("subaru", "legacy", 2003)
my_car.get_descriptive_name()
my_car.read_odometer()
my_car.odometer_reading = 23
my_car.read_odometer()
my_car.update_odometer(50)
my_car.read_odometer()
my_car.update_odometer(20)
my_car.increment_odometer(100)
my_car.read_odometer()
my_car.increment_odometer(500)
my_car.read_odometer()
my_car.increment_odometer(-20)
