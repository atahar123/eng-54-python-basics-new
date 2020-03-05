# Whileloops

# Syntax


# while <condition>:
    # run block of code
    # if <condition>:
        # break

# counter = 0
#
# while counter <= 10:
#     print(counter)
#     print('this is cool')
#     counter += 1

# reserved words
# break - used to break the while loop
# continue - skips to the next iteration without running the following code/blocks

# user_input = input('You want to play?')

# while user_input == 'yes' or user_input == 'y':
#     random_num = 10
#     print('Welcome to the random game')
#     user_input = input('what is your guess?\n')
#     if int(user_input) == random_num:
#         print('CONGRATS BRO')
#     else:
#         print('sorry you lost')
#     user_input = input('Play again?')

while True:
    user_input = input('Choose 1 for pancakes, 2 for cake, 3 to exit.. or just exit\n')
    if user_input == '1':
        print('pancakes')
    elif user_input == '2':
        print('cakes')
    elif 'exit' in user_input or user_input == '3':
        print('goodbye')
        break
    else:
        print('use numbers or keyword')
