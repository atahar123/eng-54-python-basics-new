


# - You can vote and drivre
# - You can vote
# - You can driver
# - you can't leagally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


 #as a user I should be able to keep being prompted for input until I say 'exit'

# print('Welcome to the age verifier. Type exit to exit')
#
# while True:
#     driver_license = input('Do you have a drivers license? Type Y or N\n')
#     user_age = float(input('How old are you?\n'))
#     if (user_age >= 19) and (driver_license == 'Y' or 'y'):
#         print('You can vote and drive')
#     elif (user_age >= 19) and (driver_license == 'N' or 'n'):
#         print('You can vote')
#     elif driver_license == 'exit':
#         print('Successfully exited. Byeeee!')
#         break
#     else:
#         print('Go back to school')

user_input = ' '

while user_input != 'exit' or 'Exit':
    user_input = input('How old are you?')
    print('Hi')

