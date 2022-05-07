import time

a = ["a", "A", "(A)","(a)"]
b = ["b", "B", "(B)","(b)"]
c = ["c", "C", "(C)","(c)"]
d = ["d", "D", "(d)","(D)"]

#Storing the correct answers
correct = 0 

#Storing the user's name
name = input ("What's your name? ") 

print("\nHello, " +  name +", let's get started. \n\nRemember, \nthe following answers are only a, b, c or d.")
time.sleep(2)

print("1. Who is the creator of Python Programming Language.")
print("(A) Guido Van Damme")
print("(B) Guy Mc Guyver")
print("(C) Guido van Rossum")
choice = input(">>> ")
if choice in c:
  correct += 1 #If correct, the user gets one point
else:
  correct += 0
  
print("\nWhich parts of the computer were is used for calculating and comparing?")
print("(A) ALU")
print("(B) Modem")
print("(C) Control unit")
print("(D) Disk unit")
choice = input(">>> ")
if choice in a:
  correct += 1
else:
  correct += 0  

print("\n3. Program execution time would be minimum if the programs are written in")
print("(A) Assembly language")
print("(B) High level language")
print("(C) Machine language")
print("(D) None of the above")
choice = input(">>> ")
if choice in c:
  correct += 1
else:
  correct += 0 
  
print("\n4. A program used to detect overall system malfunction is")
print("(A) System diagnostics")
print("(B) Utilities")
print("(C) System analysis")
print("(D) System software")
choice = input(">>> ")
if choice in a:
  correct += 1
else:
  correct += 0  
  
print("\n5. Backup and recovery procedures are primarily implemented to")
print("(A) To provide data redundancy")
print("(B) Handle the contingency when a file gets corrupted")
print("(C) To show different versions of data and programs")
print("(D) All of these")
choice = input(">>> ")
if choice in b:
  correct += 1
else:
  correct += 0
  
print("\n6. A computer derives its basic strength from")
print("(A) Accuracy")
print("(B) Memory")
print("(C) Speed")
print("(D) All of these")
choice = input(">>> ")
if choice in d:
  correct += 1
else:
  correct += 0

print("\n7. Three main components of computer are")
print("(A) CPU, memory, tape")
print("(B) I/O, printer, mouse")
print("(C) Tape, I/O, floppy disk")
print("(D) CPU, I/O, memory")
choice = input(">>> ")
if choice in d:
  correct += 1
else:
  correct += 0

print("\n8. The process of putting data into a storage location is called")
print("(A) Hand shaking")
print("(B) Controlling")
print("(C) Writing")
print("(D) Reading")
choice = input(">>> ")
if choice in c:
  correct += 1
else:
  correct += 0

print("\n9. What is the data type of print(type(10))")
print("(A) float")
print("(B) integer")
print("(C) int")
choice = input(">>> ")
if choice in c:
  correct += 1
else:
  correct += 0

print("\n10. Did you enjoy this quiz?")
print("(A) Yes, of course")
print("(B) yes")
print("(C) Yes")
print("(D) YES")
choice = input(">>> ")

correct += 1

print("\nYou're finished, " + name)
print("Would you like to see your score?")
choice = input(">>> ")

NO_answer = ["n","N","NO","no","No"]
if choice in NO_answer:
  print("(^-^)\nThank you for participating...\n(^-^)")
  quit()
else:
  correct += 0
  print("You got", correct, "out of 10 correct.")
  print("(^-^)Thank you for participating...(^-^)")
  print("(^-^)You are so AWESOME(^-^)")