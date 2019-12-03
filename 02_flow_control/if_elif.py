
print('What‘s your name?')
userName = input()
print('How old are you?')
age = input()
if userName == 'Phil':
  print('Hi Phil')
if int(age) > 18:
  print('You are old!')
elif int(age) < 18:
  print('You are too young!')
elif int(age) > 200:
  print('I doubt it.')
