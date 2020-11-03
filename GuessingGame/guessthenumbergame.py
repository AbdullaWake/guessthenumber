# this is guess the number game

import random

print('What is your name:')
name = input()

print('Well, ' + name + ', I am thinking of number between 1 and 20')

secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low, take another guess')
    elif guess > secretNumber:
        print('Your guess is too high, take another guess')
    else:
        break # This is the condition for the correct guess!

if guess == secretNumber:
    print('Good Job,' + name + ' ! You guessed my number in ' + str(guessesTaken) + ', guesses !')
else:
    print('Nope. The number I was thinking about was , ' + str(secretNumber))
    


print('You took, ' + str(guessesTaken) + ' guesses.')
