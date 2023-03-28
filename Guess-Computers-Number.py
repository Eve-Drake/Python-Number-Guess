import random

def guess(x):
    ranNum = random.randint(1, x)
    userGuess = 0
    while userGuess != ranNum:
        userGuess = int(input('Guess a number...'))
        print(f'You guessed {userGuess}')
        if userGuess > ranNum:
            print('That is too high')
        elif userGuess < ranNum:
            print('That is too low')
    print(f"Correct! The number was {ranNum}")
guess(100)
