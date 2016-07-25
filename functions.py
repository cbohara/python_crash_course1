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
def describe_pet(pet_name, animal_type="dog"):
    """Display info about a pet"""
    print(animal_type, pet_name)

# same output
describe_pet(pet_name="ranger")
describe_pet("ranger")
# same output
describe_pet("sally", "salamander")
describe_pet(pet_name="sally", animal_type="salamander")
describe_pet(animal_type="salamander", pet_name="sally")

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
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing mode: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed):
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'unicorn glitter']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

"""
prevent functions from modifying the original list
pass in a copy of the list calling_function_name(list[:])
"""
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing mode: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed):
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

def print_original(unprinted_designs):
    print("Show that original list still exists")
    for design in unprinted_designs:
        print(design)

unprinted_designs = ['iphone case', 'robot pendant', 'unicorn glitter']
completed_models = []
print_models(unprinted_designs[:], completed_models)
# pass in a copy of the list   ^
show_completed_models(completed_models)
print_original(unprinted_designs)

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    while magicians:
        current_magician = magicians.pop()
        great_magicians.append(current_magician + " the Great!")

magicians = ['alex', 'houdini', 'magic mike']
great_magicians = []
show_magicians(magicians)
make_great(magicians[:])
print("magicians")
show_magicians(magicians)
print("great magicians")
show_magicians(great_magicians)

"""
passing an arbitrary number of arguments
using a tuple

* in the parameter name tells python to create an empty tuple and pack whatever
values it receives into the tuple (a list that cannot be changed)
if the function accepts several types of arguments, the parameter that wishes to
accept an arbitrary number of arguments must be placed last in the function definition
"""
def make_pizza(size, *toppings):
    print("Making a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

"""
using arbitrary keyword arguments
using a dictionary

in example below, function expects first and last name
then accepts as many key-value pairs as the calling statement provides!
**user_info causes Python to create an empty dictionary called user_info
and packs whatever name value pairs it receives in a dictionary
"""
# build a dictionary containing everything we know about the user
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    # items() allows us to access key, value in dictionary
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton', field='physics')
print(user_profile)

def build_sandwich(*noms):
    print("Building a sandwich with:")
    for nom in noms:
        print(nom)
build_sandwich('lettuce', 'tomato', 'mayo')

def build_user(first, last, **additional_info):
    user = {}
    user['first'] = first
    user['last'] = last
    for key, value in additional_info.items():
        user[key] = value
    return user

new_user = build_user('charlie','ohara', language='python', sport='swimming')
print(new_user)
