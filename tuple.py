# values that cannot change are immutable
# tuple = immutable list
# a tuple looks just like a list except use parentheses instead of square brackets

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# attempt to change tuple?
#dimensions[0] = 500
# get back error
#print(dimensions[0])

# althought you can't modify a tuple, you can assign a new value to the variable that holds a tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

dimensions = (500, 10)
for dimension in dimensions:
    print(dimension)
