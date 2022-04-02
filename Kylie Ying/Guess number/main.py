import random

#person guess the number
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry guess again. Too Low')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f"You have current guess the correct number {random_number}")


#computer guessing the number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = random.randint(low, high)
        feedback = input(f'Is  {guess} too high (H), too low (L), or correct (C)?? '.lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"The computer guessed you umber correctly {guess}")
computer_guess(10)