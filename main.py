import random

def user_guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess a number between 1 and {}:'.format(x)))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again.Too high')
    print('Ya , You have guessed the number {} correctly!!'.format(random_number))
def computer_guess(x):
    low =1
    high = x
    feedback = ''
    while feedback != 'c':
        if low!= high:
            guess = random.randint(low,high)
        else:
            guess = low

        feedback = input("Is {} too high (h) , too low (L) , or correct(C)".format(guess))
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print("Ya , The computer guessed your number ,{},correctly".format(guess))
computer_guess(1000)