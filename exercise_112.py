# get user input

user_input = ''
while user_input != 'pineapplepen':
    user_input = input('Number:\n')

    if user_input.isdigit():
        user_input = int(user_input)

        for number in range(1, user_input + 1):
            if (number % 3 == 0) and (number % 5 == 0):
                print('bizzbuzz')
            elif number % 3 == 0:
                print('BIZZ')
            elif number % 5 == 0:
                print('BUZZ')
            else:
                print(number)

    elif user_input == 'pineapplepen':
        print('Thank you for playing. Goodbye!')
    else:
        print('Enter a valid number')


