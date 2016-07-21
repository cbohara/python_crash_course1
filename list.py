# good idea to make list variable name plural
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# returns Trek
print(bicycles[0].title())
# also returns Trek
# special syntax for accessing last element of the list
print(bicycles[-4].title())

# insert list item in string
fruits = ['banana', 'apple', 'cherry']
hungry = "Damn I'd really like a " + fruits[0] + " right now!"
print(hungry)

# replace value at index
fruits[0] = 'mango'
hungry = "Damn I'd really like a " + fruits[0] + " right now!"
print(hungry)

# append() adds item to end of list
fruits.append('kiwi')
print(fruits)

# insert(index, value) adds new element at any position in the list
fruits.insert(0, 'banana')
print(fruits)

# del statement removes item from list but can no longer access the value that was removed
del fruits[0]
print(fruits)
del fruits[2]
print(fruits)

# pop() removes the last item of the list and allows us to access the value removed
# the term pop comes from the thinking of a list as a stack of items and popping one item off the top of the stack
# top of the stack corresponds to the end of the list
last_ate = fruits.pop()
print(fruits)
print(last_ate)
message = "The last fruit I ate was a " + last_ate + "."
print(message)

# can pop any item in a list at any position by specifying the index
first_ate = fruits.pop(0)
message = "I first fruit I ate was a " + first_ate + "."
print(message)

# use remove() method to remove the value when you don't know the position
# remove() will only delete the first occurance of the value in the list
fruits.remove('apple')
print(fruits)

# can save value we are searching for in a variable
fruits = ['banana', 'apple', 'cherry']
too_sweet = 'apple'
fruits.remove(too_sweet)
print("An " + too_sweet + " is too sweet for me.")


cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

# sorted() maintain original order of list but presents a sorted order
# takes a list as an argument
print("\nHere is the sorted list:")
print(sorted(cars))

# sort() permenantly sorts a list, in this instance reverse alphabetical
cars.sort(reverse=True)
print("\nHere is the reversed list:")
print(cars)

# sort() defaults to forwards alphabetical
cars.sort()
print("\nNow the cars are permenantly sorted alphabetically:")
print(cars)

# reverse reverses the order of the list permenantly
cars.reverse()
print("\nReverse method!")
print(cars)

# len() finds length of list
print(len(cars))
