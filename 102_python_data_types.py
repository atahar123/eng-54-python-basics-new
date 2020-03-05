# Strings
# text and characters
# Syntax
# "" and ''

# Define a string
my_string = 'Hey, I\'m a string. '
print(my_string)

# check its type
print(type(my_string))

# concatenation
# adding of two strings
joint_string = my_string + 'This is also a string'
print(joint_string)

# example 2 of concat
name = 'Mohamed'
welcome_text = 'WELCOME TO SPARRRRTAAA (300)'
print(welcome_text + ' ' + name)
print(welcome_text, name) #overloading the print method

# interpolation
# inserting a string inside another string
# or running Python inside a string
print(f'WELCOME {name} TO CLASS 54, WE ARE CONTESTED TERRAIN')

print('WELCOME {} to Class 54 '.format(name))

# useful methods
# are like functions but belong to a specific data type
# for example, it would not make sense to try to capitalize integers
example_long_string = '  HELLO, THIS IS A VERY  BadLy FormATTEd text?    '
print(example_long_string)

# Remove trailing white spaces
print(example_long_string.strip())

# Make it lower case
print(example_long_string.lower())

# Make it upper case
print(example_long_string.upper())

# make only the first character capitalized
print(example_long_string.capitalize())

# make the first character of each word capitalized
print(example_long_string.title())

# change the '?' into a '!'
print(example_long_string.replace('?', '!'))

# chain some methods and:
    # remove trailing white spaces
    # make it nicely formatted with only the first letter capitalized
print(example_long_string.strip().capitalize())

# create a list with individual words
print(example_long_string.split())

# Casting
print(type(str(24234234234243)))