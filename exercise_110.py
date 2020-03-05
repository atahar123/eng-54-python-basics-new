# Movie Ratings!

#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for
  # children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.


user_input = input('Enter either Universal, PG, 12, 15 or 18\n')

if 'Universal' in user_input:
    print('Everyone can watch')
elif 'PG' in user_input:
    print('General viewing, some scenes may not be good for kids')
elif '12' in user_input:
    print('Films classified 12A and video works classified 12 contain material that is not generally suitable for kids under 12')
elif '15' in user_input:
    print('No one younger than 15 may see this movie')
elif '18' in user_input:
    print('No one younger than 18 may see an 18 film in a cinema')
