from random import randint

print('Welcome to Rock Paper Scissors! ')
print('Rock...')
print('Paper...')
print('Scissors...')

player = input('Player, what do you choose? ').lower()
rand_num = randint(0, 2)
if rand_num == 0:
  computer = 'rock'
elif rand_num == 1:
  computer = 'paper'
else:
  computer = 'scissors'
print(f"Computer plays {computer}" )
  




if player == computer:
  print('It is a tie! ')
elif player == 'rock':
  if computer == 'scissors':
    print('player wins! ')
  elif computer =='paper':
    print('computer wins! ')
elif player == 'paper':
  if computer == 'rock':
    print('player wins! ')
  elif computer == 'scissors':
    print('computer wins! ')
elif player == 'scissors':
  if computer == 'rock':
    print('computer wins! ')
  elif computer == 'paper':
     print('player wins! ')
else:
  print('something terrible went wrong ): ')