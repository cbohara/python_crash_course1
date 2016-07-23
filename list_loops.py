magicians = ['alice', 'david', 'carolina']
# magician temporarily stores the string value in the list, not the index value!
for magician in magicians:
    print(magician)

for magician in magicians:
    print("Look " + magician.title() + "! I'm a magician too!")
    print("Wait " + magician.title() + "! Don't leave!")
print("Great magic show thank you!")

# range() generates series of numbers UP TO BUT NOT INCLUDING LAST NUMBER
# range(start value, stop value)
for value in range(0,5):
    print(value)
#prints 0 1 2 3 4

# use list() to convert the results of range() directly into a list
numbers = list(range(1,6))
print(numbers)

# use range() to tell Python to skip numbers in a given range
evens = list(range(2,11,2))
print(evens)
# [2, 4, 6, 8, 10]
every_fifth = list(range(0,21,5))
print(every_fifth)
# [0, 5 10, 15, 20]

# one way to make a list
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

# list comprehension makes a list in one line of code
squares = [value**2 for value in range(1,11)]
print(squares)

cubes = [value**3 for value in range(1,11)]
print(cubes)

#slicing a list works like range function
#list_name[start index:UP TO BUT NOT INCLUDING index]
players = ['charlie', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# ['charlie', 'martina', 'michael']
print(players[1:4])
# ['martina', 'michael', 'florence']

# automatically start at 0
print(players[:4])
# ['charlie', 'martina', 'michael', 'florence']

#automatically goes through rest of list
print(players[3:])
# ['florence', 'eli']

# last 3 values in list so -3 -2 -1
print(players[-3:])
# ['michael', 'florence', 'eli']

# looping through a slice
print("Here are the first 3 players on my team:")
for player in players[:3]:
    print(player.title())

# to copy a list, make a slice that includes the entire original list
my_foods = ['pizza', 'burgers', 'cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

# after the copy was made, now treat as two seperate lists in seperate places in memory
my_foods.append('bagels')
friend_foods.append('apples')
print(my_foods)
print(friend_foods)

# this doesn't create 2 seperate lists
# it just means both variable names point to the same list
friend_foods = my_foods
# so when we try to append to seperate lists, it actually is all one
my_foods.append('bagels')
friend_foods.append('apples')
print(my_foods)
print(friend_foods)
