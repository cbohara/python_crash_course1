from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = randint(1,6)
        print(str(x))

die = Die()
die.roll_die()
