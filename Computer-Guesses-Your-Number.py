import random

def pickNumber(x) :
    print(f"Pick a Number Between 1 and {x}")
    low = 1
    high = x
    userFeedback = ''
    while userFeedback != 'c':
        guess = random.randint(low, high)
        userFeedback= input(f'Is {guess} your number? Answer c for correct, l for too low and h for too high... ')
        if userFeedback =='l':
            low = guess + 1
        elif userFeedback == 'h':
            high = guess - 1
    print(f'Thanks for playing! Your number was {guess}')

pickNumber(10)