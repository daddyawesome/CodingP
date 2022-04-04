import random

rand_number = random.randint(1,20)

win = False
Turns =0
list_of_guesses =[]

while win==False:
    guess = input("Enter a number between 1 and 20: ")
    list_of_guesses.append(guess)
    Turns +=1
    if rand_number==int(guess):
        print("You got it!")
        print("Number of turns you have used: ",Turns)
        win == True
        break
    else:
     if rand_number>int(guess):
        print("The guess is too low! ")
     else:
        print("The guess is too high! ")

print ("You guessed the following numbers: ", list_of_guesses)