# Dictionaries
# Work with key and value paird
# Work like a real dictionary, you just lookup the information for the specific key
# The big difference with list is they are organised with index and here we use keys

# We just make a list of cringe_landlords, but we need more information like their phone numbers and address

# Syntax
dict_variable_name = {'key': 'value'}

boris_dict = {
    'name': 'Boris',
    'l_name': 'Johnson',
    'phone': '07912333444',
    'address': '10 Downing Street',
}
print(boris_dict)
print(type(boris_dict))

# Access one key value pair
# Follow the same principle of a list, but use keys not indexes
print(boris_dict['name'])

last_name = boris_dict['l_name']
print(last_name)

# Change the value of one key value paid
boris_dict['phone'] = '+7 34534543'
print(boris_dict)

# Assign a new key value pair
print(boris_dict)

boris_dict['home_phone'] = '+44 33534534534'
print(boris_dict)

boris_dict['budgets_passed'] = 0
print(boris_dict)

# The following lines do the same thing, but just increase the value by 1
boris_dict['budgets_passed'] += 1
boris_dict['budgets_passed'] += 1
print(boris_dict)

# Get all the keys
print(boris_dict.keys())

# Get all the values
print(boris_dict.values())

# Nested structures

