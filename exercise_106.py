# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# We should define/assign number to a variable called magic_number
# magic_number =

# I need to ask user for input


# I need to check if this input matches a magic_number


# I need to let the user know if the response was right or not
#self five

magic_number = 55
count = 10

user_guess = input('what is your guess')

print('your response was correct:', int(user_guess) == magic_number)



while count != 0: # True
    print(count)
    print(count != 0)
    user_input = int(input('Enter your number\n'))

    if user_input != magic_number:
        print('This is not the magic number. Please try again')
        count = count - 1

    else:
        print('Congratulations, you got the right number')
        break


