class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Welcome to " + self.name.title() + "!")
        print("We are an " + self.cuisine_type.title() + " restaurant.")
