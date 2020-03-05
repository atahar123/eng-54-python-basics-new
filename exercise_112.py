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
            if (number % 3 == 0) and (number % 5 == 0):
                print("bizzzzuu")
            # if it is a multiple of 3 it returns bizz
            elif number % 3 == 0:
                print("bizz")
            # if a multiple of 5 it return zzuu
            elif number % 5 == 0:
                print("zzuu")
            # if a multiple of 3 and 5 it return bizzzzuu
            else:
                print(number)
    # else (input is not a number)
        # invalid input - give feedback
    elif user_input == 'pineapple':
        # handle exiting game
        print("Thank you for playing.")
    else:
        print("Please enter a valid input")#
