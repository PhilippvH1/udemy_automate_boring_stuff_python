print('How many bikes do you have?')
numBikes = input()
try:
  if int(numBikes) >= 4:
    print('That is a lot of bikes...')
  elif int(numBikes) < 0:
    print('That seems unlikely.')
  else:
    print('That seems ok.')
except:
  print('That was not a number!')
