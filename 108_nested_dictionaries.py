# nest_data_structures

crazy_landl_1 = {
    'name': 'Boris',
    'phone': '072423423',
    'address_of_rent': 'Chelsea',
    'age': 55
}

crazy_landl_2 = {
    'name': 'Filipe',
    'phone': '0646343434',
    'address_of_rent': 'Comporta, Portugal',
    'age': 28
}

nested_dictionary = {'boris': crazy_landl_1,
                     'filipe': crazy_landl_2
                     }

print(nested_dictionary.keys())

for key in nested_dictionary:
    print(key)
    for nest_key in nested_dictionary[key]:
        print(nest_key, nested_dictionary[key][nest_key])
    print(nested_dictionary[key])

for key in nested_dictionary
    print(key)
    data_nested = nested_dictionary[key]
    print(data_nested)
    print(data_nested['name'])
    print(data_nested['address_of_rent'])

nest_list = [[1, 2, 3],[4, 5, 6]]

print(nest_list[0])
print(nest_list[1])
print(nest_list[1][0])

for data in nest_list:
    print(data)
    for num in data:
        print(num * 20)
