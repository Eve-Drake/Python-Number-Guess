import random

def guess(x):
    ranNum = random.randint(1, x)
    userGuess = 0
    while userGuess != ranNum:
        userGuess = input('Guess a number...')
        print(f'You guessed {userGuess}')
        

guess(100)
