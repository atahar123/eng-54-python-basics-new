from fizzbuzz_function import *

# get user input
user_input = ''
while user_input != 'pineapple':
    user_input = input("Input?\n> ")
    print(type(user_input))
    # check if input is a number
    if user_input.isdigit():
        # play the game
        user_input = int(user_input)
        print(type(user_input))

        # print all numbers from 1 to input_number
        for number in range(1, user_input + 1):
            print(play_fizzbuzz(number))
    # else (input is not a number)
        # invalid input - give feedback
    elif user_input == 'pineapple':
        # handle exiting game
        print("Thank you for playing.")
    else:
        print("Please enter a valid input")#

