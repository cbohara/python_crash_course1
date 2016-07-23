current = 1
while current <= 5:
    print(current)
    current += 1

# use a flag to act as a signal to the program
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
# flag is active variable
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# break statement to exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# for loop - traverse data
# while loop - better to use for modifying data
uncon = ['alice', 'brian', 'candace']
con = []

while uncon:
    current = uncon.pop()
    con.append(current)
for con in con:
    print(con.title())

# remove all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'cat', 'goldfish', 'rabbit']
print(pets)
# enter the while loop because it finds the value 'cat' at least once
# removes first 'cat'
# reenters the loop while 'cat' still in list
# removes the second cat
# exits the list
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# filling a dictionary with user input
responses = {}
active = True
while active:
    # remember input => string
    name = input("\nWhat is your name? ")
    mountain = input("Which mountain would you like to climb one day? ")
    # store the response for a user in the dictionary
    responses[name] = mountain
    # changes flag, otherwise keep looping
    repeat = input("Would you like to let another person share? (yes/no) ")
    if repeat == 'no':
        active = False

# items allows us to access key and value in the dictionary
for name, mountain in responses.items():
    print(name + " would like to climb " + mountain + ".")
