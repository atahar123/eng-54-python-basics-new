# mr Miyagi trainee

# make a mr miyagi virtual assistant

# as a user I should be able to speak with mr miyagi and get appropriate response s as I go

# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'


# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')

while True:
    user_input = input('Enter something, but use your wisdom for the most beautiful answers\n')

    if 'Sensei, I am at peace' in user_input:
        print('Sometimes, what heart know, head forget\n')
        break

    elif 'Sensei' not in user_input:
        print('You are smart, but not wise - address me as Sensei please\n')

    elif ('Sensei ' and 'sensei ') and ('block' or 'blocking') in user_input:
        print('Remember, best block, not to be there...\n')

    elif 'Sensei ' or 'Sensei' in user_input:
        print('Questions are wise, but for now. Wax on, and Wax off!\n')

    else:
        print('Do not lose focus. Wax on. Wax off.')
