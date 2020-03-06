# get user input
# def is_fizz(number):
#     return number % 3 == 0
#
# def is_buzz(number):
#     return number % 5 == 0

def is_div_by(number, mod):
    return number % mod == 0

def play_fizzbuzz(number):
    if is_div_by(number, 3) and is_div_by(number, 5):
        return("FizzBuzz")
    # if it is a multiple of 3 it returns bizz
    elif is_div_by(number, 3):
        return("FIZZ")
    # if a multiple of 5 it return zzuu
    elif is_div_by(number, 5):
        return("BUZZ")
    # if a multiple of 3 and 5 it return bizzzzuu
    else:
        return(number)
