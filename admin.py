from user import User

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_priv(self):
        print("The admin has the following privilege:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # make a Privileges instance as an attribute to the Admin class
        self.privileges = Privileges()
