# Welcome to the number guess game

import random

print('How should I call you?')
userName = input()

print('Generating secret number')
secretNum = random.randint(1,30)

for guessTaken in range(1,8):
  print('Alright ' + userName + '. Take a guess.')
  userGuess = int(input())
  if userGuess < secretNum:
    print('Get high, brotha!')
  elif userGuess > secretNum:
    print('Get low, get low, get loooow')
  else:
    break

if userGuess == secretNum:
  print('You did it you magnificient little kiddo and it took you just ' + str(guessTaken) + ' guesses to guess ' + str(secretNum) + ' I guess.')
else:
  print('NO YOU FOOL!')
