#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
from datetime import datetime

name = input("What is your name: ")
age = int(input("How old are you: "))
today = datetime.now()
year = str((today.year - age)+100)
print("Hi! "+name + ". You will be 100 years old in the year " + year)
