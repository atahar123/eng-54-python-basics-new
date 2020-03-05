# Define the following variables
# name, last_name, species, eye_color, hair_color
# name = 'Lana'

# Prompt user for input and Re-assign these
# name = input('what new name would you like?')

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.


name = 'Lana'
last_name = 'Johnson'
species = 'Human'
eye_color = 'Blue'
hair_color = 'Blonde'

name = input('Enter a new name')
last_name = input('Enter a new last name\n')
species = input('Enter a new species\n')
eye_color = input('Enter a new eye color\n')
hair_color = input('Enter a new hair color\n')

print(f'Hello {name} {last_name}. Your species are {species}, your eye color is {eye_color}, and hair is {hair_color}')