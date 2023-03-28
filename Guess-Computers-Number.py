import random

def guess(x):
    ranNum = random.randint(1, x)
    userGuess = 0
    while userGuess != ranNum:
        userGuess = input('Guess a number...')
        print(f'You guessed {userGuess}')
        if int(userGuess) > ranNum:
            print('That is too high')
        elif int(userGuess) < ranNum:
            print('That is too low')
    print(f"Correct! The number was {ranNum}")
guess(100)
