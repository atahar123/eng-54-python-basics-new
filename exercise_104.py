# Define the following variables
# name, last_name, species, eye_color, hair_color, age
# name = 'Lana'

# Prompt user for input and Re-assign these
# name = input('what new name would you like?')

## Calculate year of birth
# import time
# calculate the difference

# Print them back to the user as conversation including the year they were born!
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
# print something like: 'You said you we're 28 hence you were born in 1991!'
name = 'Lana'
last_name = 'Johnson'
species = 'Human'
eye_color = 'Blue'
hair_color = 'Blonde'

name = input('Enter a new name\n')
last_name = input('Enter a new last name\n')
species = input('Enter a new species\n')
eye_color = input('Enter a new eye color\n')
hair_color = input('Enter a new hair color\n')
age = int(input("Enter your age\n"))

print(f'Hello {name} {last_name}. Your species are {species}, your eye color is {eye_color}, and hair is {hair_color}')
print(f'Did I mention that you said your age is {age}. You were most likely born in ', 2020 - age)

# Section 2 - Calculate the Age difference!
# ask user for their name and age -- store these in variables
# ask user for their Mothers name and age

# calculate the difference and year of birth for each
# print out these formated. something along the lines of:
# your name is <name>, and you are <age> born on the year of <y_birth>. This is <difference_y> later than <mom_name> who
# was on on <y_birth_mon>

name = input('Enter your name\n')
age = int(input('Enter your age\n'))

m_name = input('Enter your mother\'s name\n')
m_age = int(input('Enter your mother\'s age\n'))

print(f'Your name is {name}, and you are {age} born on the year of ', 2020 - age, '. This is a difference of ', m_age -
      age, 'later than your mother ', m_name, 'who was born on', 2020 - m_age)
