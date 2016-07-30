from entertainer import Entertainer

class Magician(Entertainer):
    def __init__(self, stage_name, act_type, specialty):
        super().__init__(stage_name, act_type)
        self.specialty = specialty

    def print_magician(self):
        print("Welcome to the magic show!  I specialize in " + self.specialty + "!")
