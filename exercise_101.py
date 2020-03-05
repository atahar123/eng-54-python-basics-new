# Practice string
# Welcome to Sparta = Exercise

# Version 1 specs
# Define a variable name, and assign a string
name = 'TestUser'

# Print a welcome message plus the name
print(f'Welcome {name}')

# Prompt the user for input and ask for his/her name
# re assign the original variable with this
name = input('Enter your name\n')

# Use concatenation to print a welcome message and use method to format the name/input (remove white spaces)
print(f'Welcome to our service {name}')


# Version 2

# Ask user for the first name and save it in a variable
firstname = input("Enter your first name\n")

# Ask user for the last name and save it in a variable
lastname = input("Enter your last name\n")

# Do the same but use a different message and
# use interpolation to print the message
print(f'Hello {firstname} {lastname}, this is another service')


# Version 3 ask for name and age and respond with "Oh cool, {name}, you were born in this year"
name3 = input('Enter your name\n')
age = int(input("Enter your age\n"))

print(f'OMG {name3}, you are {age} years. This means you were born in', 2020 - age)
