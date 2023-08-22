alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# alien_0 = {'color': 'green'}
# print(alien_0['color'])

# points = alien_0['points']
# print(f"You just earned {points} points.")

# print(alien_0)

# alien_0['x_posit'] = 0
# alien_0['y_posit'] = 25
# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5

# alien_0['color'] = 'yellow'
# print(alien_0)

# alien_0 = {'x_posit': 0, 'y_posit': 25, 'speed': 'fast'}
# print(f"Original position: {alien_0['x_posit']}")
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# elif alien_0['speed'] == 'fast':
#     x_increment = 3

# alien_0['x_posit'] += x_increment
# print(f"New position: {alien_0['x_posit']}")

# print(alien_0)
# del(alien_0['points'])
# print(alien_0)

# value = alien_0.get('speed')
# print(value)

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'high'

for alien in aliens[:5]:
    print(alien)
print()

print(f"total number: {len(aliens)}")