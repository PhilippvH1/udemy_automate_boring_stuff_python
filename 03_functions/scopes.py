def musicians():
  global pop # Line below will overwrite old global variable
  pop = 'Britney Spears'
  print(pop)

pop = 'Robbie Williams'
musicians()
print(pop)
