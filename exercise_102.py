# # Create a little program that ask the user for the following details:
#  - Name
#  - height
#  - favourite color
#  - a secrete number

# Capture these inputs
# Print a tailored welcome message to the user
# print other details gathered, except the secret of course

# hint, think about casting your data type.

name = input('Enter your name\n')
height = int(input('Enter your height (cm)\n'))
color = input('Enter your favorite color\n')
number = int(input('Enter your secret number\n'))
# Line 16 is casting where I added an int to a string

print(f'Welcome {name}, your height is {height}cm, your favorite color is {color} and your number is a secret :)')