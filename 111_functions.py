# Functions
# A function is like a machine.
# It can take in inputs and do some work (block of code)
# and it can output something different
# They need to be called
# Calling a function is just writing the name and passing the arguments it needs

# Good practices
# They do one job
# They should be testable and maintainable
# This avoids stringy code/spaghetti code
# Good naming conventions
# Reduce technical debt
# Never print in a function. use 'return' instead

# Concept of DRY: Don't repeat yourself

# Syntax

# def name_of_function(arg1, arg2)
#     # Block of code
#     return 'block of code'

# Defining a simple function
def say_hello_zeus():
    return 'hello zeus'

# Calling and printing a function
print(say_hello_zeus())

# # calling but not printing
# say_hello_zeus()
# 'hello zeus'

# defining a function with arguments
# arguments are variables that exist in the scope of a function

def full_name_formatter(f_name, l_name):
    formatted_f_name = f_name.strip().capitalize()
    formatted_l_name = l_name.strip().capitalize()
    # Format each name nicely
    # I can use .strip and .capitalized
    # I have access to the name via the arguments f_name and l_name
    # save these into variables
    formatted_f_name = f_name.strip().capitalize()
    formatted_l_name = l_name.strip().capitalize()

    # Return a joint full name that is correctly formatted
    # Join the two variables into one string
    full_name = formatted_f_name + ' ' + formatted_l_name
    # return said string
    return full_name

# call function with names
print(full_name_formatter('Shannon ', ' Greyhound'))


def add_funt(num1, num2):
    # I want to return the result of adding the two numbers
    # I have access to num1 and num2. I can add them
    # I can save the result in a variable
    # I can return said variable
    result = num1 + num2
    return result

    # calling function with two arguments
    print(add_funt(10, 300))

