aliens = []

# make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

# show the total number of aliens
print("total number of aliens: " + str(len(aliens)))

