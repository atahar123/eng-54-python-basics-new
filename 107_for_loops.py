# for loops

# Syntax

# for item in iterable:
  # block of code

import time

cool_cars = ['Skoda fun', 'Fiat old one', 'Toyota Corolla', 'Fiat Panda 4x4', 'Fiat Multipla']

count = 1

for car in cool_cars:
    print(count, '-', car)
    count += 1
    time.sleep(1)



#### For loops for dictionaries
boris_dict = {
    'name': 'Boris',
    'l_name': 'Johnson',
    'phone': '07912333444',
    'address': '10 Downing Street',
}

for key in boris_dict:
    print(key)

for key in boris_dict:
    print(key)
