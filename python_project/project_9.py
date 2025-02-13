# python rock paper scissors game

import random
your_turn = input("Enter your choice (rock , paper , scissors): ")
option = ['rock','paper','scissors']
computer = random.choice(option)

while your_turn not in option:
    your_turn = input("Enter your choice (rock , paper , scissors): ")
print(f"player: {your_turn}")
print(f"computer:{computer}")    
if computer == your_turn:
    print('Draw')
elif your_turn == 'rock' and computer == 'scissors':
    print("Player Win!")
elif your_turn == 'Scissors' and computer == 'paper':
    print('Player Win!')
elif your_turn == 'paper' and computer == 'rock':
    print('Player Win!')
else:
    print("Computer Win! ")
