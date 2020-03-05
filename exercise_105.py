# Lists!

# Fine a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _______????? SQUARE BRACKETS
country_list = ['UK', 'USA', 'Portugal', 'Spain', 'Italy']

# Print the lists and check it's type
print(country_list)
print(type(country_list))

# Print the list's first object
print(country_list[0])

# Print the list's second object
print(country_list[1])

# Print the list's last object
print(country_list[4])

# Re-define the first item on the list and
country_list.insert(0, 'NewItem1')

# Re-define another item on the list and print all the list
country_list.insert(3, 'NewItem2')
print(country_list)

# Add an item to the list and print the list
country_list.append('NewItem3')
print(country_list)

# Remove an item from the list and print the list
country_list.remove('USA')
print(country_list)

# Add two items to list and print the list
country_list.append('NewItem4')
country_list.append('NewItem5')
print(country_list)

# Remove the last item of the list
# Remove index item 4

country_list.pop()
print(country_list)

country_list.pop(4)
print(country_list)

# Check the number of items inside a list
len(country_list)
print(len(country_list))