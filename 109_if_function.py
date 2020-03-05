# Control flow // if function and while loops
# if functions

#syntax
# if <condition>:
    # block of code that runs if condition returns True
# elif <condition>
    # block of code that runs if condition returns True
# else:
    # block of code that runs when all other conditions are false

# if functions will exit once a condition becomes True
# Build your if functions with the most specific thing at the top

weather = 'fish fingers rainy'

if 'rainy' in weather:
    print('take your umbrella')
elif weather == 'sunny':
    print('Take your sunglasses')
elif 'rainy' in weather and 'windy' in weather:
    print('it looks bad, stay in')
else:
    print('Did\'nt quite catch that. Please repeat again')

