import random as r
mylist = ['stone','paper','scissor']

player1 = r.choice(mylist)
player2 = r.choice(mylist)
print(f'player1 - {player1}')
print(f'player2 - {player2}')

if player1 == player2:
    print('MATCH DRAW')
elif player1=='scissor' and player2=='paper':
    print('Player 1 wins')
elif player1=='stone' and player2=='scissor':
    print('Player 1 wins')
elif player1=='paper' and player2=='stone':
    print('Player 1 wins')
else:
    print('Player 2 wins')