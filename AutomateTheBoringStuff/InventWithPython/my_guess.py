#The guess the number game made by me

import random

guess_num = random.randint(1, 30)
guess_taken = 0

print('Hi! \nWhat is your name?')
name = input()

print('Well, '+name+" I am going to think of a number between 1 to 30 and I am going to give you 5 tries to guess what is.")
for guess_taken in range(5):
    print("Take a guess.")
    guess = input()
    # use try and except to avoid traceback error
    try:
        guess = int(guess)
        if guess < guess_num:
            print('Your guess is too low.') 
        if guess > guess_num:
            print('Your guess is too high.')
        if guess == guess_num:
            break
    except:
        print("Kindly use integers not letters")

if guess == guess_num:
    guess_taken = str(guess_taken + 1)
    print('Good job, ' + name + '! You guessed my number in ' +
      guess_taken + ' guesses!')
if guess != guess_num:
    guess_num = str(guess_num)
    print('Nope. The number I was thinking of was ' + guess_num + '.')
