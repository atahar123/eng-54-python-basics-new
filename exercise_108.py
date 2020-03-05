# Dictionary basics :D
#1 - Define a dictionary call story1, it should have the followign keys:
        # start, middle and end
#2 - Print the entire dictionary
#3 - Print the type of your dictionary
#4 - Print only the keys
#4 - print only the values
#5 - print the individual values using the keys (individually, lots of printi commands)
#6 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero

story1 = {
    'start': 'A man named John Cena.',
    'middle': 'He couldn\'t be seen.',
    'end': 'He was very sad.'
}

print(story1)
print(type(story1))

print(story1.keys())

print(story1.values())

print(story1['start'])
print(story1['middle'])
print(story1['end'])

story1['superhero'] = 'Ironman'
print(story1)
