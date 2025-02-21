alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

alien_0['color'] = 'yellow'

print(alien_0['color'])
print(alien_0['points'])

del alien_0['color']
print(alien_0)

print("Als de string om af te drukken te lang wordt \n" +
      "dan is het geen issue, om deze over " +
      "meerdere regels te verspreiden " + str(alien_0['points']))