'''import random

top_of_range=input('Type a number >> ')

if top_of_range.isdigit():
  top_of_range=int(top_of_range)
  if top_of_range ==0 :
    print('please type a number greater than 0 next time')
    quit()

else:
  print('Type a positive number next time')
  quit()

random_number=random.randint(0,top_of_range)
guessess=0

while True:
  guessess+=1
  user_guess=input('Make a guess :')
  if user_guess.isdigit():
    user_guess=int(user_guess)
  else:
    print('Type a positive number next time')
    continue 

  if user_guess==random_number:
    print('you got it!')
    break
  else : 
    print('you got it wrong !')
  
print(f'you for it in,{guessess}')'''

import random

# Prompt user for the range
top_of_range = input('Type a number >> ')

# Check if the input is a positive integer
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please type a number greater than 0 next time.')
        quit()
else:
    print('Type a positive number next time.')
    quit()

# Generate a random number
random_number = random.randint(1, top_of_range)  # Starts from 1 to avoid 0
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Type a positive number next time.')
        continue

    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess < random_number:
        print('Too low! Try again.')
    else:
        print('Too high! Try again.')

print(f'You got it in {guesses} guesses.')




