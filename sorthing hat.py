# Sorting Hat
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('1. Do u like Dawn or Dusk?')
print('1) Dawn')
print('2) Dusk')
user = int(input('Enter ur answer [1 or 2]:'))
if user == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif user == 2:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1
else:
  print('Wrong input')
print('==================================================================')
print('2. When I’m dead, I want people to remember me as:')
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print(' 4) The Bold')
user = int(input('Enter ur answer [1 or 4]:'))
if user == 1:
  hufflepuff = hufflepuff + 2
elif user == 2:
  slytherin = slytherin + 2
elif user == 3:
  ravenclaw = ravenclaw + 2
elif user == 4:
  gryffindor = gryffindor + 2
else:
  print('Wrong input')
print('==================================================================')
print('3. Which kind of instrument most pleases your ear?')
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')
user = int(input('Enter ur answer [1 or 4]:'))
if user == 1:
  slytherin = slytherin + 4
elif user == 2:
  hufflepuff = hufflepuff + 4
elif user == 3:
  ravenclaw = ravenclaw + 4
elif user == 4:
  gryffindor = gryffindor + 4
else:
  print('Wrong input')

print(f'The total points for Gryffindor is', gryffindor)
print('==================================================================')
print(f'The total points for Ravenclaw is', ravenclaw)
print('==================================================================')
print(f'The total points for Hufflepuff is', hufflepuff)
print('==================================================================')
print(f'The total points for Slytherin is', slytherin)
print('==================================================================')
print('Bonus')
if gryffindor >= ravenclaw >= hufflepuff >= slytherin:
  print('🦁 Gryffindor')
elif ravenclaw >= hufflepuff >= slytherin:
  print('🦅 Ravenclaw')
elif hufflepuff >= slytherin:
  print('🦡 Hufflepuff')
else:
  print('🐍 Slytherin')