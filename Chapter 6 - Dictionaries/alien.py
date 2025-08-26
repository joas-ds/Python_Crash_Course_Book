# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
#
# #Changing values in a dictionarie:
# alien_0['color'] = 'grey'
# print(f"The alien is now {alien_0['color']}.")

alien_0 = {'color': 'green', 'points': 5,'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position: {alien_0['x_position']}")

#Move the alien to the right
#Determine how far to move the alien based on its current speed.
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #Fast alien
    x_increment = 3

#The new alien position is the old position plus the increment based on its speed.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New alien x-position: {alien_0['x_position']}")

#Removing Key-value pairs:
#Removing 'points'
print(alien_0)
del alien_0['points']
print(alien_0)

