# Python Number Guessing Game

import random
answer = random.randint(1,100)
guess_count = 0
while True:
    guess = (input('Enter your number 1 to 100: '))
    if(guess.isdigit()):
        guess = int(guess)
        guess_count+=1
        if guess == answer:
            print(f'correct! The correct answer is {answer}')
            print(f"You guess the number in {guess_count} terms")
            break
        elif guess < 0 or guess > 100:
            print("Out of range!Enter number between 1 to 100") 
        elif guess > answer:
            print("Too High! Try again")
        elif guess < answer:
            print("Too Low! Try again")
    else :
        print("Invalid Guess")
        print('Please select a number between 1 to 100: ')
        