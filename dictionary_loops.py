favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

# keys() method accesses keys only
for name in favorite_languages.keys():
    print(name.title())

# check if keys in dictionary match values in list
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# a dictionary always maintains a clear connection between each key and its
# associated value, but you never get the items in any particular order

# use sorted() to loop through a dictionary's keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# use values() to return list of values without keys
for language in favorite_languages.values():
    print(language.title() + " has been mentioned in our poll.")

# use set() to see the values in dictionary without repetition
for language in set(favorite_languages.values()):
    print(language.title())
