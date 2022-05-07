import os
import random
import time     


HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']

#Generating Random word
def randomWord():
    file = open('words.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]

#Check Guesses
def checkLetter(word,guess,secretString):
    i = 0
    while i < len(word):
        if word[i] == guess:
            secretString = secretString [0:i] + guess + secretString [i+1:len(word)]
        i= i + 1
    return secretString

#Main
print('The game is HANGMAN.\n After 7 mistake before you guess the word you die.')
print('You also have 30 seconds to guess the word.')

def main_game():
    
    secretString = ""
    word = randomWord()
    j = 0
    i = 0

    while i < len(word):
        secretString = secretString + '#'
        i = i + 1

    print('Your secret word is:')
    print(secretString)
    
    time_limit = 30
    start_time = time.time()
       

    while j<7:
        elapsed_time = time.time() - start_time

        countd = time_limit - int(elapsed_time)
        
        mins, secs = divmod(countd, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        
        print("Time Left:", timeformat)
        
        if elapsed_time > time_limit:
            print("\n\n(^-^)You're out of time!(^-^)\nYour avatar blows up..")
            print('SORRY YOU DIED!')
            print("Game Over")
            os._exit(1)

        print('\nYour Mistakes: ')
        print(j)
        print("\nGuess a Letter")
        guess=input('>>> ')
        
        secretString=checkLetter(word,guess,secretString)
        
        print('Your PROGRESS: ')
        print(secretString)
        
        if secretString==word:
            print('Congratulation, YOU WIN!')
            os._exit(1)
        if j==6:
            print(HANGMAN_PICS[j])
            print('SORRY YOU DIED!')
            print("Game Over")
            print('The secret word is', word)
            os._exit(1)
        if guess in word:
            print("Your guess is correct")
        else:
            print("Your guess is wrong")
            j += 1
            print(HANGMAN_PICS[j-1])
        
        

main_game()