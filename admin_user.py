from user import User
from admin import Privileges, Admin

user1 = User("bobby", "brown")
user1.print_name()
admin1 = Admin("alex", "admin")
admin1.print_name()
admin1.privileges.show_priv()
