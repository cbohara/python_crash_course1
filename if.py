cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# testing for equality is case sensitive
car = 'Audi'
print(car == 'audi')
# returns false
print(car.lower() == 'audi')
# returns true
# .lower() doesn't change the value originally stored in the variable

# booleans are uppercase True and False in python

# and statement is simply 'and'
# or statement is simply 'or'
# parentheses can improve readability but are not required
age_0 = 22
age_1 = 18
statement = age_0 >= 21 and age_1 >= 21
print(statement)
# returns False

# use 'in' statement to check if a value is in a list
request_toppings = ['mushroom', 'onions', 'pineapple']
if 'mushroom' in request_toppings:
    print("True")
elif 'pepperoni' in request_toppings:
    print("False")
else:
    print("Whomp whomp")

# use 'not in' statement to check if a value does not appear in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response!")

# if-elif-else chain appropriate when only need 1 test to pass
# as soon as that one test passes, it skips the rest of the tests
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
# don't forget to convert an int to a string with str()
print("Because you are " + str(age) + " years old, your price of admission is "
        + str(price) + " dollars.")

# python DOES NOT REQUIRE AN ELSE BLOCK at the end of if-elif chain!
age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Senior citizens can enjoy a discounted price of " + str(price) + " dollars.")

# act on every condition that is true with a series of if statements
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Mushrooms on top!")
if 'pepperoni' in requested_toppings:
    print("Pepperoni coming up!")
if 'extra cheese' in requested_toppings:
    print("Loads of cheese!")
print("Finished making your pizza!")

# checking for values in a list in a loop
print("\n")
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']
for topping in requested_toppings:
    if topping == 'green peppers':
        print("Sorry all out!")
    else:
        print("Adding " + topping + " to the pie!")
print("Your pizza is ready!")
print("\n")

# checking a list is not empty
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        if topping == 'green peppers':
            print("Sorry all out!")
        else:
            print("Adding " + topping + " to the pie!")
else:
    print("Are you sure you want a plain pizza?")
print("\n")
# using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print("Adding " + topping)
    else:
        print("Sorry we don't have " + topping)
print("Finished making your pizza!")

# ordinal numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
