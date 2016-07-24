# function definition - tells python the name of the function + arguments needed
def greet_user():
    # docstring = special comment python looks for when it generates
    # documentation for functions in the program
    """Display a simple greeting."""
    print("Hello!")
# call the function with ()
# greet_user()

# username is the parameter
def greet_user(username):
    """ Display greeting for specific user"""
    print("Hello " + username + "!")
# "Charlie" is the argument for the greet_user function
# greet_user("Charlie")

# pass arguments in a number of ways
# positional arguments - need to be in the same order the parameters were written
def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# correct order of arguments
describe_pet('hampster', 'harry')
# will not return desired results
describe_pet('harry', 'hampster')

# keyword arguments - pass in name-value pair into a function
def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# specify argument associated with parameter
describe_pet(animal_type = "hampster", pet_name = "harry")
# now doesn't have to be in any particular order
describe_pet(pet_name = "ranger", animal_type = "dog")

# default values have to listed after all parameters that don't have defaults
def describe_pet(pet_name, animal_type = "dog"):
    """Display info about a pet"""
    print(animal_type, pet_name)

# same output
describe_pet(pet_name = "ranger")
describe_pet("ranger")
# same output
describe_pet("sally", "salamander")
describe_pet(pet_name = "sally", animal_type = "salamander")
describe_pet(animal_type = "salamander", pet_name = "sally")

# return data
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    # return data
    return full_name.title()

# stores function return into variable
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# passing a list into a function
def greet_user(names):
    """Print a simple greeting to each using in a list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ["hannah", "ty", "margot"]
greet_user(usernames)

# modifying a list in a function
unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
completed = []
# prints design
def print_models(unprinted, completed):
    while unprinted:
        current_project = unprinted.pop()
        print("Printing model: \n" + current_project)
        completed.append(current_project)

# summarize which prints have been made
def show_completed_models(completed):
    for complete in completed:
        print(completed)

print_models(unprinted, completed)
show_completed_models(completed)
