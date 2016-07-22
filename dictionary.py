# dictionaries - data structure with key value pairs
# order doesn't matter! access via key, not an index like a list

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# create an empty dictionary
alien_0 = {}
# then add key value pairs to it
alien_0['x_position'] = 0
alien_0['y_position'] = 0
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 23, 'speed': 'medium'}
print(alien_0)

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

new_position = alien_0['x_position'] + x_increment
print("Old position was " + str(alien_0['x_position']) + " but it moved to  position"
        + str(new_position))
