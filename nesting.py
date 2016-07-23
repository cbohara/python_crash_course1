aliens = []
# make a fleet of 30 aliens!
# create a list containing many dictionaries
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# slice list from index 0 up to but not including 3
# change the first 3 aliens
for alien in aliens[0:10]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))


# list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the follwing toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# dictionary with lists as values
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

# items() allows to access the key and value in the dictionary
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    # language is
    for language in languages:
        print("\t" + language.title())
