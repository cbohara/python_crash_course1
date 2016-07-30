class Entertainer():
    def __init__(self, stage_name, act_type):
        self.stage_name = stage_name
        self.act_type = act_type

    def welcome_to_show(self):
        print("Welcome to the " + self.stage_name.title() + " show!")

    def inquiry(self):
        print("What type of show is this?  It's a " + self.act_type + " show!")
